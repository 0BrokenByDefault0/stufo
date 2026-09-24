import SwiftUI

struct SessionsView: View {
    @EnvironmentObject private var store: StudioStore
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                Eyebrow(text: "From idea to finished record")
                Text("A little direction.\nA lot of progress.").font(.system(size: 35, weight: .bold, design: .rounded)).tracking(-1)
                Text("Practical checklists for the moment you’re in. Your place is saved automatically.").foregroundStyle(Palette.muted).font(.subheadline).lineSpacing(4)
                ForEach(store.content.workflows) { workflow in NavigationLink { WorkflowView(workflow: workflow) } label: { WorkflowRow(workflow: workflow) }.buttonStyle(.plain).accessibilityIdentifier("workflow-\(workflow.id)") }
            }.padding(22).padding(.bottom, 20)
        }.pageStyle().toolbar(.hidden, for: .navigationBar)
    }
}
struct WorkflowRow: View {
    @EnvironmentObject private var store: StudioStore
    let workflow: Workflow
    var count: Int { workflow.steps.indices.filter { store.state.checks.contains("\(workflow.id).\($0)") }.count }
    var body: some View {
        Card {
            HStack(alignment: .top, spacing: 16) {
                Image(systemName: workflow.symbol).font(.title2).frame(width: 44, height: 48).background(Palette.paper, in: RoundedRectangle(cornerRadius: 14))
                VStack(alignment: .leading, spacing: 8) {
                    Text(workflow.title).font(.headline).multilineTextAlignment(.leading)
                    Text(workflow.subtitle).font(.caption).foregroundStyle(Palette.muted).multilineTextAlignment(.leading)
                    HStack { Text(workflow.time); Spacer(); Text("\(count)/\(workflow.steps.count)") }.font(.caption.monospacedDigit()).foregroundStyle(Palette.muted)
                    ProgressView(value: Double(count), total: Double(workflow.steps.count)).tint(Palette.ink)
                }
            }
        }
    }
}
struct WorkflowView: View {
    @EnvironmentObject private var store: StudioStore
    let workflow: Workflow
    @State private var reset = false
    var count: Int { workflow.steps.indices.filter { store.state.checks.contains("\(workflow.id).\($0)") }.count }
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                Eyebrow(text: "Session guide · \(workflow.time)")
                Text(workflow.title).font(.system(.largeTitle, design: .rounded, weight: .bold)).tracking(-1)
                Text(workflow.subtitle).foregroundStyle(Palette.muted)
                HStack { ProgressView(value: Double(count), total: Double(workflow.steps.count)).tint(Palette.ink); Text("\(count) / \(workflow.steps.count)").font(.caption.monospacedDigit()) }
                ForEach(Array(workflow.steps.enumerated()), id: \.offset) { index, step in
                    let key = "\(workflow.id).\(index)"
                    Button { store.toggle(key, in: \.checks) } label: {
                        HStack(alignment: .top, spacing: 14) {
                            Image(systemName: store.state.checks.contains(key) ? "checkmark.circle.fill" : "circle").font(.title2)
                            VStack(alignment: .leading, spacing: 7) { Eyebrow(text: "Step \(index + 1)"); Text(step).font(.body).lineSpacing(4).multilineTextAlignment(.leading) }
                            Spacer(minLength: 0)
                        }.padding(20).background(store.state.checks.contains(key) ? Palette.lime.opacity(0.5) : .white, in: RoundedRectangle(cornerRadius: 20))
                    }.buttonStyle(.plain).accessibilityLabel("Step \(index + 1), \(store.state.checks.contains(key) ? "complete" : "incomplete"): \(step)").accessibilityIdentifier("workflowStep\(index)")
                }
                if count == workflow.steps.count { Card(color: Palette.lime) { Label("Session complete. Take a fresh listen.", systemImage: "checkmark.seal").font(.headline) } }
                SectionTitle(title: "Understand the why")
                ForEach(workflow.lessonIDs.compactMap(store.lesson)) { LessonRow(lesson: $0) }
                Button("Start this checklist again") { reset = true }.font(.subheadline).frame(maxWidth: .infinity).padding()
            }.padding(22).padding(.bottom, 20)
        }.pageStyle().navigationTitle("Session guide").navigationBarTitleDisplayMode(.inline)
            .confirmationDialog("Reset this checklist?", isPresented: $reset, titleVisibility: .visible) { Button("Reset checklist", role: .destructive) { for index in workflow.steps.indices { store.state.checks.remove("\(workflow.id).\(index)") } } }
    }
}

struct AssistantView: View {
    @EnvironmentObject private var store: StudioStore
    @State private var query = ""
    @State private var submitted = ""
    @State private var expandedFAQ: String?
    @FocusState private var focused: Bool
    var matches: [(FAQ, Double)] { store.content.faqs.map { ($0, store.score(submitted, title: $0.question, body: $0.answer, tags: $0.tags)) }.filter { $0.1 >= 6 }.sorted { $0.1 > $1.1 } }
    var lessons: [Lesson] { Array(store.search(submitted).prefix(4)) }
    let suggestions = ["I can’t hear my microphone", "How do I throw a delay?", "My vocal sounds muddy", "Move my song from Logic", "Which Pro-Q filter is high pass?"]
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                Eyebrow(text: "Your offline studio assistant")
                Text("What’s in\nyour way?").font(.system(size: 40, weight: .bold, design: .rounded)).tracking(-1.5)
                Text("Find clear answers in your lesson library. Ask about recording, mixing, your tools, or the next step.").font(.subheadline).foregroundStyle(Palette.muted).lineSpacing(4)
                VStack(spacing: 14) {
                    TextField("Ask a studio question…", text: $query, axis: .vertical).lineLimit(2...5).focused($focused).submitLabel(.search).onSubmit(ask).accessibilityIdentifier("assistantQuestion")
                    Button(action: ask) { HStack { Text("Find my next step"); Spacer(); Image(systemName: "arrow.up.right") } }.buttonStyle(PrimaryButton()).disabled(query.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty).accessibilityIdentifier("askButton")
                }.padding(18).background(.white, in: RoundedRectangle(cornerRadius: 22))
                if submitted.isEmpty {
                    VStack(alignment: .leading, spacing: 10) {
                        Eyebrow(text: "Start here")
                        ForEach(suggestions, id: \.self) { suggestion in Button { query = suggestion; ask() } label: { HStack { Text(suggestion).multilineTextAlignment(.leading); Spacer(); Image(systemName: "arrow.up.left") }.font(.subheadline).padding(15).background(Palette.lime.opacity(0.4), in: RoundedRectangle(cornerRadius: 16)) }.buttonStyle(.plain).accessibilityIdentifier("suggestion-\(suggestion)") }
                    }
                } else {
                    VStack(alignment: .leading, spacing: 15) {
                        Eyebrow(text: "From your library")
                        if let best = matches.first {
                            Card(color: Palette.lime.opacity(0.5)) {
                                VStack(alignment: .leading, spacing: 13) { Text(best.0.question).font(.title3.bold()); Text(best.0.answer).lineSpacing(5).textSelection(.enabled).accessibilityIdentifier("assistantAnswer"); Text("Matched reference answer · not generated AI").font(.caption).foregroundStyle(Palette.muted) }
                            }
                            ForEach(best.0.lessonIDs.compactMap(store.lesson)) { LessonRow(lesson: $0) }
                        } else {
                            Card { Text("I don’t have a verified direct answer to that question yet. \(lessons.isEmpty ? "Try a specific symptom or topic, such as latency, comping, or sends." : "These lessons may help you narrow it down.")").lineSpacing(4).accessibilityIdentifier("assistantAnswer") }
                        }
                        if !lessons.isEmpty {
                            SectionTitle(title: "Explore the topic")
                            ForEach(lessons.filter { !(matches.first?.0.lessonIDs.contains($0.id) ?? false) }) { LessonRow(lesson: $0) }
                        }
                    }
                }
                SectionTitle(title: "The frequently asked things")
                ForEach(store.content.faqs) { faq in
                    DisclosureGroup(isExpanded: Binding(get: { expandedFAQ == faq.id }, set: { expandedFAQ = $0 ? faq.id : nil })) {
                        VStack(alignment: .leading, spacing: 12) { Text(faq.answer).font(.subheadline).lineSpacing(4).padding(.top, 10); ForEach(faq.lessonIDs.compactMap(store.lesson)) { LessonRow(lesson: $0) } }
                    } label: { Text(faq.question).font(.subheadline.weight(.semibold)).multilineTextAlignment(.leading) }.padding(18).background(.white, in: RoundedRectangle(cornerRadius: 18))
                }
            }.padding(22).padding(.bottom, 20)
        }.pageStyle().toolbar(.hidden, for: .navigationBar).scrollDismissesKeyboard(.interactively)
    }
    private func ask() { let trimmed = query.trimmingCharacters(in: .whitespacesAndNewlines); guard !trimmed.isEmpty else { return }; submitted = trimmed; focused = false }
}

struct StudioView: View {
    @EnvironmentObject private var store: StudioStore
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                Eyebrow(text: "A workbench for your ears")
                Text("Your studio,\nwithin reach.").font(.system(size: 38, weight: .bold, design: .rounded)).tracking(-1)
                SectionTitle(title: "Play with the idea", caption: "Move a control. See what changes.")
                NavigationLink { DelayLab() } label: { toolRow("Delay & tempo", subtitle: "Tap the beat. Find the space between words.", icon: "metronome", color: Palette.lime) }.buttonStyle(.plain).accessibilityIdentifier("delayLab")
                NavigationLink { EQLab() } label: { toolRow("The frequency map", subtitle: "Low cut, bell, and shelf — made visible.", icon: "waveform.path", color: Palette.teal) }.buttonStyle(.plain)
                NavigationLink { CompressionLab() } label: { toolRow("Compression, explained", subtitle: "Threshold and ratio without the guesswork.", icon: "slider.vertical.3", color: Palette.purple) }.buttonStyle(.plain)
                NavigationLink { SignalLab() } label: { toolRow("Follow the signal", subtitle: "Inserts, sends, and a real delay throw.", icon: "point.3.connected.trianglepath.dotted", color: Palette.clay) }.buttonStyle(.plain)
                SectionTitle(title: "Your practice")
                NavigationLink { NotebookView() } label: { toolRow("Studio notebook", subtitle: "Your discoveries, session notes, and saved lessons.", icon: "square.and.pencil", color: .white) }.buttonStyle(.plain)
                NavigationLink { GlossaryView() } label: { toolRow("Plain-English glossary", subtitle: "\(store.content.glossary.count) concepts, with real examples.", icon: "text.book.closed", color: .white) }.buttonStyle(.plain)
                NavigationLink { SourcesView() } label: { toolRow("Sources & your setup", subtitle: "Original creators, manuals, and tool choices.", icon: "books.vertical", color: .white) }.buttonStyle(.plain)
                Text("STUFO 1.0  /  MADE FOR THE PRACTICE").font(.system(.caption2, design: .monospaced)).tracking(1).foregroundStyle(Palette.muted).padding(.top, 12)
            }.padding(22).padding(.bottom, 20)
        }.pageStyle().toolbar(.hidden, for: .navigationBar)
    }
    private func toolRow(_ title: String, subtitle: String, icon: String, color: Color) -> some View {
        Card(color: color) { HStack(spacing: 16) { Image(systemName: icon).font(.title2).frame(width: 36); VStack(alignment: .leading, spacing: 6) { Text(title).font(.headline); Text(subtitle).font(.caption).foregroundStyle(Palette.muted).multilineTextAlignment(.leading) }; Spacer(minLength: 0); Image(systemName: "arrow.up.right").font(.caption) } }
    }
}

struct NotebookView: View {
    @EnvironmentObject private var store: StudioStore
    @State private var title = ""
    @State private var note = ""
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                SectionTitle(title: "Leave a trail.", caption: "What did you hear? What will you try next?")
                Card {
                    VStack(spacing: 14) {
                        TextField("Session name", text: $title).font(.headline)
                        TextField("What worked, what didn’t, your next move…", text: $note, axis: .vertical).lineLimit(4...12)
                        Button("Save session note") {
                            store.state.journal.insert(JournalEntry(title: title.isEmpty ? "Studio session" : title, body: note), at: 0); title = ""; note = ""
                        }.buttonStyle(PrimaryButton()).disabled(note.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
                    }
                }
                ShareLink(item: store.exportText) { Label("Export my notebook", systemImage: "square.and.arrow.up").font(.subheadline) }
                ForEach(store.state.journal) { entry in
                    Card { VStack(alignment: .leading, spacing: 10) { Eyebrow(text: entry.date.formatted(date: .abbreviated, time: .omitted)); Text(entry.title).font(.headline); Text(entry.body).lineSpacing(4).textSelection(.enabled) } }
                }
                SectionTitle(title: "Saved lessons")
                let saved = store.content.lessons.filter { store.state.saved.contains($0.id) }
                if saved.isEmpty { Text("Tap the bookmark in any lesson to keep it here.").font(.subheadline).foregroundStyle(Palette.muted) }
                ForEach(saved) { LessonRow(lesson: $0) }
                SectionTitle(title: "Notes from your lessons")
                ForEach(store.content.lessons.filter { !(store.state.notes[$0.id] ?? "").isEmpty }) { lesson in
                    VStack(alignment: .leading, spacing: 8) { LessonRow(lesson: lesson); Text(store.state.notes[lesson.id] ?? "").font(.subheadline).lineSpacing(4).padding(.horizontal, 8).textSelection(.enabled) }
                }
            }.padding(22)
        }.pageStyle().navigationTitle("Studio notebook").navigationBarTitleDisplayMode(.inline)
    }
}
struct GlossaryView: View {
    @EnvironmentObject private var store: StudioStore
    @State private var query = ""
    var body: some View {
        ScrollView { VStack(alignment: .leading, spacing: 16) {
            SearchField(text: $query, prompt: "Find a word…")
            let terms = store.content.glossary.filter { query.isEmpty || ($0.term + $0.meaning + $0.example).localizedCaseInsensitiveContains(query) }
            if terms.isEmpty { ContentUnavailableView.search(text: query) }
            ForEach(terms) { term in Card { VStack(alignment: .leading, spacing: 10) { Text(term.term).font(.title3.bold()); Text(term.meaning).lineSpacing(3); Text(term.example).font(.subheadline).foregroundStyle(Palette.muted).lineSpacing(3) } } }
        }.padding(22) }.pageStyle().navigationTitle("The glossary").navigationBarTitleDisplayMode(.inline)
    }
}
struct SourcesView: View {
    @EnvironmentObject private var store: StudioStore
    var body: some View {
        ScrollView { VStack(alignment: .leading, spacing: 22) {
            SectionTitle(title: "Built around your music")
            Card(color: Palette.lime.opacity(0.5)) { Text("Mac + Studio Pro · Apollo Twin X + Console · FabFilter · Antares · iZotope · UAD Spark · Soothe · LANDR\n\nStock tools come first in the lessons. Your other plug-ins are alternatives when their purpose fits the sound.").font(.subheadline).lineSpacing(5) }
            Text("Stufo is an independent personal study companion. Original lessons, diagrams, and exercises are paired with source references. Studio Pro Toolbox is curated by Lukas Ruschitzka; video rights remain with the creators. Stufo is not affiliated with Fender, PreSonus, or those creators.").font(.subheadline).foregroundStyle(Palette.muted).lineSpacing(4)
            Text("Written for Fender Studio Pro 8.x, with Studio One terminology explained where useful. Manuals checked September 24, 2026. Features, names, and shortcuts can differ by version and key map. Use Find Command or the linked manual if a menu has moved.").font(.subheadline).lineSpacing(4)
            Text("Lessons, notes, progress, checklists, and the reference assistant work offline. Links open online. The assistant matches your question to curated reference answers; it does not listen to your song or generate AI advice. Personal notes stay on this device unless you export them. Deleting the app removes local data.").font(.subheadline).foregroundStyle(Palette.muted).lineSpacing(4)
            SectionTitle(title: "Manuals & further learning")
            ForEach(store.content.sources.filter { $0.kind != "video" }) { SourceRow(source: $0) }
        }.padding(22) }.pageStyle().navigationTitle("Sources & setup").navigationBarTitleDisplayMode(.inline)
    }
}
