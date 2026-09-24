import SwiftUI
import UIKit

struct ConceptVisual: View {
    let kind: String
    var body: some View {
        VStack(alignment: .leading, spacing: 18) {
            Eyebrow(text: caption)
            switch kind {
            case "eq":
                EQCurve(kind: "Bell", frequency: 900, gain: -5).stroke(Palette.ink, style: StrokeStyle(lineWidth: 2.5, lineCap: .round)).frame(height: 105)
                HStack { Text("BODY"); Spacer(); Text("PRESENCE"); Spacer(); Text("AIR") }.font(.system(.caption2, design: .monospaced))
            case "dynamics", "levels":
                HStack(alignment: .bottom, spacing: 8) {
                    ForEach(0..<24) { i in RoundedRectangle(cornerRadius: 3).fill(i > 20 ? Palette.clay : Palette.ink.opacity(0.4 + Double(i % 4) * 0.15)).frame(height: CGFloat(25 + (i * 37 % 81))) }
                }.frame(height: 110)
                Text(kind == "levels" ? "LEAVE ROOM FOR THE LOUDEST MOMENT" : "CONTROL THE PEAKS. KEEP THE PERFORMANCE.").font(.system(size: 9, weight: .medium, design: .monospaced))
            case "automation", "space":
                Canvas { ctx, size in
                    var line = Path(); let points: [CGPoint] = [CGPoint(x: 0, y: size.height * 0.8), CGPoint(x: size.width * 0.48, y: size.height * 0.8), CGPoint(x: size.width * 0.5, y: size.height * 0.2), CGPoint(x: size.width * 0.68, y: size.height * 0.2), CGPoint(x: size.width * 0.7, y: size.height * 0.8), CGPoint(x: size.width, y: size.height * 0.8)]
                    line.addLines(points); ctx.stroke(line, with: .color(Palette.ink), lineWidth: 2.5)
                    for point in points { ctx.fill(Path(ellipseIn: CGRect(x: point.x - 4, y: point.y - 4, width: 8, height: 8)), with: .color(Palette.ink)) }
                }.frame(height: 100)
                HStack { Text("DRY"); Spacer(); Text("THE LAST WORD"); Spacer(); Text("TAIL") }.font(.system(size: 9, design: .monospaced))
            case "arrangement", "comping", "edit":
                VStack(spacing: 7) {
                    ForEach(0..<3) { row in
                        HStack(spacing: 6) {
                            Text(kind == "comping" ? "TAKE \(row + 1)" : ["BEAT", "LEAD", "TEXTURE"][row]).font(.system(size: 8, weight: .bold, design: .monospaced)).frame(width: 49, alignment: .leading)
                            ForEach(0..<6) { col in RoundedRectangle(cornerRadius: 4).fill((row + col) % 3 == 0 ? Palette.ink : Palette.ink.opacity(0.13)).frame(height: 27).overlay { if (row + col) % 3 == 0 { Image(systemName: "waveform").font(.caption2).foregroundStyle(.white) } } }
                        }
                    }
                }
                Text(kind == "comping" ? "CHOOSE THE PERFORMANCE, PHRASE BY PHRASE" : "GIVE EVERY PART A PURPOSE").font(.system(size: 9, design: .monospaced))
            case "stereo":
                HStack(spacing: 16) { node("L", icon: "speaker.wave.2"); Spacer(); node("VOICE", icon: "mic"); Spacer(); node("R", icon: "speaker.wave.2") }
                Text("A SOLID CENTER. SPACE AT THE SIDES.").font(.system(size: 9, design: .monospaced))
            case "export":
                HStack { node("SESSION", icon: "slider.horizontal.3"); Image(systemName: "arrow.right"); node("LISTEN", icon: "headphones"); Image(systemName: "arrow.right"); node("DELIVER", icon: "waveform") }
            default:
                HStack { node("SOURCE", icon: "mic"); Image(systemName: "arrow.right"); node("SHAPE", icon: "slider.horizontal.3"); Image(systemName: "arrow.right"); node("LISTEN", icon: "headphones") }
                Text("FOLLOW THE SOUND, ONE STAGE AT A TIME").font(.system(size: 9, design: .monospaced))
            }
        }.accessibilityElement(children: .ignore).accessibilityLabel(caption + ". An illustrative learning diagram; not a screenshot of the DAW.")
    }
    private var caption: String {
        switch kind { case "eq": return "Sculpt the spectrum"; case "levels": return "Headroom is your friend"; case "dynamics": return "Loudness over time"; case "space", "automation": return "A moment of movement"; case "comping": return "Build the best take"; case "arrangement", "edit": return "The shape of the song"; case "stereo": return "The stereo field"; case "export": return "Finish with intention"; default: return "The signal journey" }
    }
    private func node(_ text: String, icon: String) -> some View { VStack(spacing: 13) { Image(systemName: icon).font(.title2); Text(text).font(.system(size: 9, weight: .bold, design: .monospaced)) }.frame(maxWidth: .infinity).padding(.vertical, 22).background(.white.opacity(0.7), in: RoundedRectangle(cornerRadius: 16)) }
}

struct DelayLab: View {
    @AppStorage("stufo.bpm") private var bpm = 90.0
    @State private var taps: [Date] = []
    @State private var copied: String?
    let names = ["1/1", "1/2", "1/4", "1/8", "1/16", "1/32"]
    var body: some View {
        ScrollView { VStack(alignment: .leading, spacing: 24) {
            Eyebrow(text: "Interactive studio tool")
            Text("Find your pocket.").font(.system(.largeTitle, design: .rounded, weight: .bold))
            Card(color: Palette.lime) {
                VStack(spacing: 18) {
                    HStack(alignment: .firstTextBaseline) { Text("\(Int(bpm))").font(.system(size: 70, weight: .bold, design: .rounded)).monospacedDigit().accessibilityIdentifier("bpmValue"); Text("BPM").font(.caption.bold()); Spacer(); Button(action: tap) { VStack(spacing: 6) { Image(systemName: "hand.tap").font(.title2); Text("TAP").font(.caption.bold()) }.frame(width: 65, height: 70).background(Palette.ink, in: RoundedRectangle(cornerRadius: 20)).foregroundStyle(.white) }.accessibilityLabel("Tap tempo") }
                    Slider(value: $bpm, in: 40...220, step: 1).accessibilityLabel("Tempo")
                    Stepper("Fine adjust tempo", value: $bpm, in: 40...220, step: 1).font(.subheadline)
                }
            }
            Text("Tap four or more steady beats, or match your session’s BPM. Values below are milliseconds. Tap any value to copy it.").font(.subheadline).foregroundStyle(Palette.muted).lineSpacing(4)
            VStack(spacing: 0) {
                HStack { Text("NOTE").frame(width: 46, alignment: .leading); column("STRAIGHT"); column("DOTTED"); column("TRIPLET") }.font(.system(size: 9, weight: .bold, design: .monospaced)).padding(.bottom, 14)
                ForEach(Array(names.enumerated()), id: \.offset) { index, name in
                    let base = 60000.0 / bpm * 4 / pow(2, Double(index))
                    HStack { Text(name).font(.caption.bold()).frame(width: 46, alignment: .leading); value(base); value(base * 1.5); value(base * 2 / 3) }.padding(.vertical, 15)
                    Divider()
                }
            }.padding(18).background(.white, in: RoundedRectangle(cornerRadius: 22))
            if let copied { Label("Copied \(copied) ms", systemImage: "checkmark.circle").font(.caption).accessibilityIdentifier("copiedDelay") }
            Card { VStack(alignment: .leading, spacing: 12) { Text("Try this on a rap vocal").font(.headline); Text("Start with a quarter-note throw at the end of a phrase. Keep the delay return fully wet, automate how much you send into it, and listen for the repeat’s rhythm against the next line. A dotted eighth gives a more syncopated answer.").font(.subheadline).lineSpacing(4); Text("Quarter note = 60,000 ÷ BPM. Dotted = ×1.5. Triplet = ×⅔. These are beat divisions, not a prescribed reverb decay.").font(.caption).foregroundStyle(Palette.muted) } }
        }.padding(22) }.pageStyle().navigationTitle("Delay & tempo").navigationBarTitleDisplayMode(.inline)
    }
    private func column(_ name: String) -> some View { Text(name).frame(maxWidth: .infinity) }
    private func value(_ ms: Double) -> some View { let text = String(format: "%.1f", ms); return Button { UIPasteboard.general.string = text; copied = text } label: { Text(text).font(.system(.caption, design: .monospaced)).frame(maxWidth: .infinity).frame(minHeight: 32) }.accessibilityLabel("Copy \(text) milliseconds") }
    private func tap() {
        let now = Date()
        if let last = taps.last, now.timeIntervalSince(last) > 2 { taps = [] }
        taps.append(now); taps = Array(taps.suffix(8))
        if taps.count >= 2 { let seconds = now.timeIntervalSince(taps[0]) / Double(taps.count - 1); bpm = min(220, max(40, (60 / seconds).rounded())) }
        UIImpactFeedbackGenerator(style: .light).impactOccurred()
    }
}

struct EQCurve: Shape {
    let kind: String
    let frequency, gain: Double
    func path(in rect: CGRect) -> Path {
        var path = Path()
        let center = log10(frequency / 20) / 3
        for i in 0...220 {
            let x = Double(i) / 220
            let db: Double
            switch kind {
            case "Low cut": db = max(-18, min(0, (x - center) * 65))
            case "High shelf": db = gain / (1 + exp(-(x - center) * 22))
            default: db = gain * exp(-pow((x - center) / 0.12, 2))
            }
            let point = CGPoint(x: x * rect.width, y: rect.height * (0.5 - db / 40))
            if i == 0 { path.move(to: point) } else { path.addLine(to: point) }
        }
        return path
    }
}
struct EQLab: View {
    @State private var kind = "Low cut"
    @State private var logFrequency = log10(90.0)
    @State private var gain = -4.0
    var frequency: Double { pow(10, logFrequency) }
    var body: some View {
        ScrollView { VStack(alignment: .leading, spacing: 24) {
            Text("Shape, don’t guess.").font(.system(.largeTitle, design: .rounded, weight: .bold))
            Picker("Filter shape", selection: $kind) { ForEach(["Low cut", "Bell", "High shelf"], id: \.self) { Text($0).tag($0) } }.pickerStyle(.segmented)
            Card(color: Palette.teal.opacity(0.5)) {
                VStack(spacing: 16) {
                    ZStack {
                        VStack { ForEach(0..<5) { _ in Divider(); Spacer(minLength: 0) } }
                        EQCurve(kind: kind, frequency: frequency, gain: gain).stroke(Palette.ink, style: StrokeStyle(lineWidth: 3, lineCap: .round))
                    }.frame(height: 190).clipped().accessibilityLabel("Illustrative \(kind) response, frequency \(Int(frequency)) hertz")
                    HStack { Text("20 Hz"); Spacer(); Text("630 Hz"); Spacer(); Text("20 kHz") }.font(.caption.monospaced())
                }
            }
            Text("\(Int(frequency)) Hz").font(.system(.title, design: .rounded, weight: .bold)).monospacedDigit()
            Slider(value: $logFrequency, in: log10(20)...log10(20000)).accessibilityLabel("Filter frequency")
            if kind != "Low cut" { HStack { Text("Gain"); Spacer(); Text(String(format: "%+.1f dB", gain)).monospacedDigit() }; Slider(value: $gain, in: -12...12, step: 0.5).accessibilityLabel("Filter gain") }
            Card { VStack(alignment: .leading, spacing: 12) { Text(kind == "Low cut" ? "Low cut = high pass" : kind == "Bell" ? "A focused tonal move" : "A broad change above the corner").font(.headline); Text(kind == "Low cut" ? "These are two names for the same job: reduce lows and let higher frequencies pass. In FabFilter Pro-Q, choose Low Cut. Bring the frequency up slowly in the full mix; stop before the voice loses body, then back off." : kind == "Bell" ? "A bell boosts or cuts around its center frequency. In a real EQ, Q sets its width. Use a small broad move for tone and a narrower move for a clearly identified resonance. There is no frequency that every vocal must lose." : "A high shelf changes the upper range as a whole. A little can add openness; too much can reveal hiss and sharp consonants. Compare at the same perceived loudness.").lineSpacing(4); Text("Illustrative curve only; no audio is being processed. Actual filter slopes and resonance depend on the plug-in.").font(.caption).foregroundStyle(Palette.muted) } }
            ForEach([("20–80 Hz", "Sub energy & rumble"), ("80–250 Hz", "Weight & warmth"), ("250–800 Hz", "Body, boxiness & mud"), ("1–5 kHz", "Intelligibility & bite"), ("5–10 kHz", "Consonants & brightness"), ("10–20 kHz", "Air & noise")], id: \.0) { band in HStack { Text(band.0).font(.caption.monospaced()).frame(width: 105, alignment: .leading); Text(band.1).font(.subheadline); Spacer() } }
        }.padding(22) }.pageStyle().navigationTitle("Frequency map").navigationBarTitleDisplayMode(.inline)
    }
}

struct CompressionLab: View {
    @State private var threshold = -18.0
    @State private var ratio = 4.0
    @State private var input = -6.0
    var output: Double { input <= threshold ? input : threshold + (input - threshold) / ratio }
    var body: some View {
        ScrollView { VStack(alignment: .leading, spacing: 22) {
            Text("Tame the peak.\nKeep the feeling.").font(.system(.largeTitle, design: .rounded, weight: .bold))
            Card(color: Palette.purple.opacity(0.5)) {
                VStack(alignment: .leading, spacing: 10) {
                    Eyebrow(text: "Output ↑  /  Input →  · dBFS")
                    Canvas { ctx, size in
                        func point(_ x: Double, _ y: Double) -> CGPoint { CGPoint(x: (x + 60) / 60 * size.width, y: (1 - (y + 60) / 60) * size.height) }
                        var diagonal = Path(); diagonal.move(to: point(-60, -60)); diagonal.addLine(to: point(0, 0)); ctx.stroke(diagonal, with: .color(Palette.ink.opacity(0.2)), style: StrokeStyle(lineWidth: 1, dash: [4, 4]))
                        var curve = Path(); curve.move(to: point(-60, -60)); curve.addLine(to: point(threshold, threshold)); curve.addLine(to: point(0, threshold + (0 - threshold) / ratio)); ctx.stroke(curve, with: .color(Palette.ink), lineWidth: 3)
                        let dot = point(input, output); ctx.fill(Path(ellipseIn: CGRect(x: dot.x - 6, y: dot.y - 6, width: 12, height: 12)), with: .color(Palette.ink))
                    }.frame(height: 200)
                    HStack { Text("−60"); Spacer(); Text("0") }.font(.caption.monospaced())
                }
            }
            control("Threshold", value: $threshold, range: -48 ... -3, label: String(format: "%.0f dB", threshold))
            control("Ratio", value: $ratio, range: 1...10, label: String(format: "%.1f:1", ratio))
            control("Input level", value: $input, range: -60...0, label: String(format: "%.0f dBFS", input))
            Card(color: Palette.ink) { HStack { VStack(alignment: .leading, spacing: 5) { Text("OUTPUT").font(.caption); Text(String(format: "%.1f dBFS", output)).font(.title2.bold()).monospacedDigit() }; Spacer(); VStack(alignment: .trailing, spacing: 5) { Text("REDUCTION").font(.caption); Text(String(format: "%.1f dB", input - output)).font(.title2.bold()).monospacedDigit() } }.foregroundStyle(.white) }
            Text("At 4:1, 12 dB above the threshold becomes 3 dB above it: 9 dB of gain reduction. Below the threshold, the level is unchanged in this idealized hard-knee model.").lineSpacing(4)
            Text("Real compressors also have attack, release, knee, detector behavior, and makeup gain. This graph shows the steady-state level relationship, not the timing or sound of a plug-in. Faster attack catches more of a transient; slower attack lets more of its front edge through.").font(.subheadline).foregroundStyle(Palette.muted).lineSpacing(4)
        }.padding(22) }.pageStyle().navigationTitle("Compression lab").navigationBarTitleDisplayMode(.inline)
    }
    private func control(_ name: String, value: Binding<Double>, range: ClosedRange<Double>, label: String) -> some View { VStack { HStack { Text(name).font(.headline); Spacer(); Text(label).monospacedDigit() }; Slider(value: value, in: range, step: 1).accessibilityLabel(name) } }
}

struct SignalLab: View {
    @State private var fader = -6.0
    @State private var send = -12.0
    @State private var pre = false
    var body: some View {
        ScrollView { VStack(alignment: .leading, spacing: 22) {
            Text("Follow the sound.").font(.system(.largeTitle, design: .rounded, weight: .bold))
            Card(color: Palette.teal.opacity(0.4)) {
                VStack(spacing: 12) {
                    block("Lead vocal", detail: "Recorded audio", icon: "waveform")
                    Image(systemName: "arrow.down")
                    block("Insert chain", detail: "EQ → compressor → tone", icon: "slider.horizontal.3")
                    Image(systemName: "arrow.down")
                    HStack(alignment: .top, spacing: 12) {
                        block("Dry path", detail: String(format: "Fader: %.0f dB", fader), icon: "mic")
                        block("Send → FX", detail: String(format: "Relative feed: %.0f dB", send + (pre ? 0 : fader)), icon: "repeat")
                    }
                    Image(systemName: "arrow.down")
                    block("Main output", detail: "Dry vocal + wet delay return", icon: "headphones")
                }
            }
            Toggle("Pre-fader send", isOn: $pre).tint(Palette.ink)
            Text(pre ? "The send branches before the fader. Moving the vocal fader leaves the send feed unchanged. In Studio Pro, pre-fader sends are still after the inserts." : "The send follows the fader. Lowering the vocal also lowers what reaches the delay. This is the usual starting point for vocal effects.").font(.subheadline).lineSpacing(4)
            HStack { Text("Vocal fader"); Spacer(); Text(String(format: "%.0f dB", fader)) }; Slider(value: $fader, in: -48...0, step: 1).accessibilityLabel("Vocal fader")
            HStack { Text("Send level"); Spacer(); Text(String(format: "%.0f dB", send)) }; Slider(value: $send, in: -60...0, step: 1).accessibilityLabel("Send level")
            Card(color: Palette.lime.opacity(0.5)) { VStack(alignment: .leading, spacing: 10) { Text("Make a throw").font(.headline); Text("Keep the delay on an FX channel at 100% wet. Draw a send-level rise on the word you want repeated, then return the send to silence. The delay already inside the effect can keep ringing. Muting the return would cut that tail.").font(.subheadline).lineSpacing(4) } }
            Text("Levels are relative gain offsets, not measured output loudness. −60 dB is very quiet; a DAW send’s −∞ position is fully off.").font(.caption).foregroundStyle(Palette.muted)
        }.padding(22) }.pageStyle().navigationTitle("Signal flow").navigationBarTitleDisplayMode(.inline)
    }
    private func block(_ title: String, detail: String, icon: String) -> some View { VStack(spacing: 8) { Image(systemName: icon).font(.title3); Text(title).font(.subheadline.bold()); Text(detail).font(.caption).foregroundStyle(Palette.muted).multilineTextAlignment(.center) }.padding(16).frame(maxWidth: .infinity).background(.white, in: RoundedRectangle(cornerRadius: 18)) }
}
