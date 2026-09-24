import SwiftUI

@main struct StufoApp: App {
    @StateObject private var store = StudioStore()
    var body: some Scene {
        WindowGroup {
            RootView().environmentObject(store).tint(Palette.ink).preferredColorScheme(.light)
                .alert("Stufo", isPresented: Binding(get: { store.error != nil }, set: { if !$0 { store.error = nil } })) { Button("OK") { store.error = nil } } message: { Text(store.error ?? "") }
        }
    }
}

struct RootView: View {
    @State private var tab = 0
    var body: some View {
        TabView(selection: $tab) {
            NavigationStack { TodayView() }.tabItem { Label("Today", systemImage: "sun.max") }.tag(0)
            NavigationStack { LearnView() }.tabItem { Label("Learn", systemImage: "books.vertical") }.tag(1)
            NavigationStack { SessionsView() }.tabItem { Label("Sessions", systemImage: "slider.horizontal.3") }.tag(2)
            NavigationStack { AssistantView() }.tabItem { Label("Ask", systemImage: "bubble.left.and.text.bubble.right") }.tag(3)
            NavigationStack { StudioView() }.tabItem { Label("Studio", systemImage: "waveform.path") }.tag(4)
        }.onAppear {
            if let flag = ProcessInfo.processInfo.arguments.firstIndex(of: "--tab"), ProcessInfo.processInfo.arguments.count > flag + 1 { tab = Int(ProcessInfo.processInfo.arguments[flag + 1]) ?? 0 }
        }
    }
}

struct TodayView: View {
    @EnvironmentObject private var store: StudioStore
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 28) {
                HStack {
                    HStack(spacing: 8) { Image(systemName: "waveform").font(.title2.weight(.bold)); Text("stufo").font(.system(size: 30, weight: .black, design: .rounded)).tracking(-1) }
                    Spacer()
                    Text("STUDIO\nCOMPANION").font(.system(.caption2, design: .monospaced, weight: .medium)).tracking(1.3).foregroundStyle(Palette.muted).multilineTextAlignment(.trailing)
                }
                VStack(alignment: .leading, spacing: 18) {
                    HStack { Eyebrow(text: "Less noise. More music."); Spacer(); Image(systemName: "sparkle") }
                    Text("Your next\nbreakthrough.").font(.system(size: 44, weight: .bold, design: .rounded)).tracking(-2).minimumScaleFactor(0.7).fixedSize(horizontal: false, vertical: true)
                    Text("Build your ears. Know your tools.\nFinish music that sounds like you.").font(.subheadline).foregroundStyle(Palette.muted).lineSpacing(4)
                    WaveArt().frame(height: 105).accessibilityHidden(true)
                    HStack(spacing: 0) {
                        metric("\(store.content.lessons.count)", "LESSONS")
                        Spacer()
                        metric("\(store.state.completed.count)", "PRACTICED")
                        Spacer()
                        metric("Offline", "ALWAYS READY")
                    }
                }.padding(24).background(Palette.lime, in: RoundedRectangle(cornerRadius: 30))
                if let lesson = store.resumeLesson {
                    VStack(alignment: .leading, spacing: 12) {
                        SectionTitle(title: store.state.lastLesson == nil ? "Start with the essentials" : "Pick up where you left off")
                        NavigationLink { LessonView(lesson: lesson) } label: {
                            HStack(spacing: 18) {
                                Image(systemName: store.chapter(lesson.chapter)?.symbol ?? "headphones").font(.title2).frame(width: 58, height: 66).background(Palette.chapter(lesson.chapter), in: RoundedRectangle(cornerRadius: 17))
                                VStack(alignment: .leading, spacing: 6) { Eyebrow(text: "\(lesson.level) · \(lesson.minutes) min"); Text(lesson.title).font(.headline).multilineTextAlignment(.leading) }
                                Spacer(minLength: 0); Image(systemName: "arrow.up.right")
                            }.padding(18).background(.white, in: RoundedRectangle(cornerRadius: 24))
                        }.buttonStyle(.plain).accessibilityIdentifier("continueLesson")
                    }
                }
                VStack(alignment: .leading, spacing: 12) {
                    SectionTitle(title: "What are we making?", caption: "A clear next step, right beside your DAW.")
                    ForEach(store.content.workflows.prefix(3)) { workflow in NavigationLink { WorkflowView(workflow: workflow) } label: { WorkflowRow(workflow: workflow) }.buttonStyle(.plain) }
                }
                Card(color: Palette.ink) {
                    VStack(alignment: .leading, spacing: 12) {
                        Label("THE STUDIO RULE", systemImage: "ear").font(.caption.bold()).tracking(1.5).foregroundStyle(Palette.lime)
                        Text("One move. One reason.\nThen listen again.").font(.system(.title2, design: .rounded, weight: .semibold)).foregroundStyle(.white)
                        Text("Use the lessons on your own song. The goal is a decision you can hear, not a preset you can memorize.").font(.subheadline).foregroundStyle(.white.opacity(0.7)).lineSpacing(3)
                    }
                }
            }.padding(22).padding(.bottom, 20)
        }.pageStyle().toolbar(.hidden, for: .navigationBar)
    }
    private func metric(_ value: String, _ label: String) -> some View {
        VStack(alignment: .leading, spacing: 5) { Text(value).font(.system(.title3, design: .rounded, weight: .bold)); Text(label).font(.system(size: 8, weight: .bold, design: .monospaced)).tracking(0.6) }
    }
}

struct WaveArt: View {
    var body: some View {
        Canvas { context, size in
            for row in 0..<14 {
                var path = Path()
                for i in 0...180 {
                    let x = Double(i) / 180 * size.width
                    let phase = Double(i) / 180
                    let envelope = pow(sin(phase * .pi), 2)
                    let y = size.height / 2 + sin(phase * .pi * 5 + Double(row) * 0.22) * envelope * (20 + Double(row) * 2.4)
                    if i == 0 { path.move(to: CGPoint(x: x, y: y)) } else { path.addLine(to: CGPoint(x: x, y: y)) }
                }
                context.stroke(path, with: .color(Palette.ink.opacity(0.25 + Double(row) * 0.045)), lineWidth: 1)
            }
        }
    }
}

struct LearnView: View {
    @EnvironmentObject private var store: StudioStore
    @State private var query = ""
    @State private var mode = "Path"
    @State private var onlySaved = false
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                Eyebrow(text: "Your artist development")
                Text("Learn the craft.").font(.system(size: 36, weight: .bold, design: .rounded)).tracking(-1)
                SearchField(text: $query)
                Picker("Library view", selection: $mode) { Text("Path").tag("Path"); Text("Library").tag("Library"); Text("Watch").tag("Watch") }.pickerStyle(.segmented)
                if mode == "Watch" {
                    Text("Selected from Studio Pro Toolbox. Videos play online with their original creators; older Studio One screens may differ from Studio Pro 8.").font(.subheadline).foregroundStyle(Palette.muted)
                    ForEach(store.content.sources.filter { $0.kind == "video" && (query.isEmpty || ($0.title + $0.author).localizedCaseInsensitiveContains(query)) }) { source in SourceRow(source: source) }
                    if let source = store.content.sources.first(where: { $0.id == "toolbox" }) { SourceRow(source: source) }
                } else if mode == "Library" || !query.isEmpty {
                    Toggle("Saved lessons only", isOn: $onlySaved).font(.subheadline).tint(Palette.ink)
                    let lessons = store.search(query).filter { !onlySaved || store.state.saved.contains($0.id) }
                    Text("\(lessons.count) lessons").font(.caption).foregroundStyle(Palette.muted)
                    if lessons.isEmpty { ContentUnavailableView("No lessons found", systemImage: "magnifyingglass", description: Text("Try “delay”, “recording”, “EQ”, or clear the saved filter.")) }
                    ForEach(lessons) { lesson in LessonRow(lesson: lesson) }
                } else {
                    Card {
                        VStack(alignment: .leading, spacing: 10) {
                            HStack { Text("Practice, then progress").font(.headline); Spacer(); Text("\(store.state.completed.count)/\(store.content.lessons.count)").font(.caption.monospacedDigit()) }
                            ProgressView(value: Double(store.state.completed.count), total: Double(max(1, store.content.lessons.count))).tint(Palette.ink)
                            Text("Move at your pace. Every stage is unlocked.").font(.caption).foregroundStyle(Palette.muted)
                        }
                    }
                    ForEach(Array(store.content.chapters.enumerated()), id: \.element.id) { index, chapter in
                        NavigationLink { ChapterView(chapter: chapter, index: index) } label: {
                            Card(color: Palette.chapter(chapter.id).opacity(0.5)) {
                                VStack(alignment: .leading, spacing: 16) {
                                    HStack { Eyebrow(text: "Stage \(String(format: "%02d", index + 1))"); Spacer(); Image(systemName: chapter.symbol).font(.title2) }
                                    Text(chapter.title).font(.system(.title2, design: .rounded, weight: .bold))
                                    Text(chapter.subtitle).font(.subheadline).foregroundStyle(Palette.muted).multilineTextAlignment(.leading)
                                    HStack {
                                        let lessons = store.content.lessons.filter { $0.chapter == chapter.id }
                                        Text("\(lessons.filter { store.state.completed.contains($0.id) }.count) / \(lessons.count) practiced").font(.caption)
                                        Spacer(); Image(systemName: "arrow.right")
                                    }
                                }
                            }
                        }.buttonStyle(.plain)
                    }
                }
            }.padding(22).padding(.bottom, 20)
        }.pageStyle().toolbar(.hidden, for: .navigationBar)
    }
}

struct ChapterView: View {
    @EnvironmentObject private var store: StudioStore
    let chapter: Chapter
    let index: Int
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                Eyebrow(text: "Stage \(index + 1)")
                Text(chapter.title).font(.system(.largeTitle, design: .rounded, weight: .bold))
                Text(chapter.subtitle).foregroundStyle(Palette.muted)
                ForEach(store.content.lessons.filter { $0.chapter == chapter.id }) { LessonRow(lesson: $0) }
            }.padding(22)
        }.pageStyle().navigationTitle("Learning path").navigationBarTitleDisplayMode(.inline)
    }
}

struct LessonRow: View {
    @EnvironmentObject private var store: StudioStore
    let lesson: Lesson
    var body: some View {
        NavigationLink { LessonView(lesson: lesson) } label: {
            HStack(spacing: 14) {
                Image(systemName: store.state.completed.contains(lesson.id) ? "checkmark" : (store.chapter(lesson.chapter)?.symbol ?? "book")).font(.headline).frame(width: 45, height: 50).background(Palette.chapter(lesson.chapter), in: RoundedRectangle(cornerRadius: 14))
                VStack(alignment: .leading, spacing: 6) {
                    Text(lesson.title).font(.subheadline.weight(.semibold)).multilineTextAlignment(.leading)
                    Text("\(lesson.minutes) min · \(lesson.level)").font(.caption).foregroundStyle(Palette.muted)
                }
                Spacer(minLength: 0)
                Image(systemName: store.state.saved.contains(lesson.id) ? "bookmark.fill" : "chevron.right").font(.caption).foregroundStyle(Palette.muted)
            }.padding(16).background(.white, in: RoundedRectangle(cornerRadius: 20))
        }.buttonStyle(.plain)
    }
}

struct LessonView: View {
    @EnvironmentObject private var store: StudioStore
    let lesson: Lesson
    @State private var choice: Int?
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 26) {
                VStack(alignment: .leading, spacing: 12) {
                    Eyebrow(text: "\(lesson.level) · \(lesson.minutes) min read + practice")
                    Text(lesson.title).font(.system(.largeTitle, design: .rounded, weight: .bold)).tracking(-1).accessibilityIdentifier("lessonTitle")
                    Text(lesson.subtitle).font(.title3).foregroundStyle(Palette.muted)
                }
                ConceptVisual(kind: lesson.visual).frame(minHeight: 180).padding(18).background(Palette.chapter(lesson.chapter).opacity(0.4), in: RoundedRectangle(cornerRadius: 24))
                VStack(alignment: .leading, spacing: 15) {
                    Eyebrow(text: "Understand it")
                    ForEach(lesson.concepts, id: \.self) { Text($0).font(.body).lineSpacing(5).textSelection(.enabled) }
                }
                VStack(alignment: .leading, spacing: 18) {
                    SectionTitle(title: "Do it in your session")
                    ForEach(Array(lesson.steps.enumerated()), id: \.offset) { index, step in
                        HStack(alignment: .top, spacing: 14) {
                            Text(String(format: "%02d", index + 1)).font(.system(.caption, design: .monospaced, weight: .bold)).padding(10).background(.white, in: Circle())
                            Text(step).lineSpacing(4).frame(maxWidth: .infinity, alignment: .leading).textSelection(.enabled)
                        }
                    }
                }
                Card(color: Palette.clay.opacity(0.35)) { VStack(alignment: .leading, spacing: 9) { Label("Watch for this", systemImage: "eye").font(.headline); Text(lesson.mistake).font(.subheadline).lineSpacing(4) } }
                Card(color: Palette.ink) {
                    VStack(alignment: .leading, spacing: 12) {
                        Text("YOUR NEXT 10 MINUTES").font(.caption.bold()).tracking(1).foregroundStyle(Palette.lime)
                        Text(lesson.practice).foregroundStyle(.white).lineSpacing(4)
                        Divider().overlay(.white.opacity(0.2))
                        Text("You’ve got it when…").font(.caption.bold()).foregroundStyle(Palette.lime)
                        Text(lesson.success).font(.subheadline).foregroundStyle(.white.opacity(0.8)).lineSpacing(3)
                    }
                }
                quiz
                VStack(alignment: .leading, spacing: 10) {
                    SectionTitle(title: "Make it yours", caption: "What changed in your song? Notes save as you type.")
                    TextField("A setting, a discovery, a question…", text: Binding(get: { store.state.notes[lesson.id] ?? "" }, set: { store.state.notes[lesson.id] = $0 }), axis: .vertical).lineLimit(4...10).padding(18).background(.white, in: RoundedRectangle(cornerRadius: 18)).accessibilityIdentifier("lessonNotes")
                }
                VStack(alignment: .leading, spacing: 12) {
                    Eyebrow(text: "Go deeper · original sources")
                    ForEach(store.content.sources.filter { lesson.sources.contains($0.id) }) { SourceRow(source: $0) }
                }
                Button { store.toggle(lesson.id, in: \.completed) } label: { Label(store.state.completed.contains(lesson.id) ? "Practiced — tap to undo" : "I practiced this", systemImage: store.state.completed.contains(lesson.id) ? "checkmark.circle.fill" : "checkmark.circle") }.buttonStyle(PrimaryButton()).accessibilityIdentifier("completeLesson")
                if let index = store.content.lessons.firstIndex(where: { $0.id == lesson.id }), index + 1 < store.content.lessons.count {
                    VStack(alignment: .leading, spacing: 10) { Eyebrow(text: "Up next"); LessonRow(lesson: store.content.lessons[index + 1]) }
                }
            }.padding(22).padding(.bottom, 25)
        }.pageStyle().navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) { Button { store.toggle(lesson.id, in: \.saved) } label: { Image(systemName: store.state.saved.contains(lesson.id) ? "bookmark.fill" : "bookmark") }.accessibilityLabel(store.state.saved.contains(lesson.id) ? "Unsave lesson" : "Save lesson").accessibilityIdentifier("saveLesson") }
            }.onAppear { store.state.lastLesson = lesson.id }
    }
    private var quiz: some View {
        Card {
            VStack(alignment: .leading, spacing: 14) {
                Label("Check your understanding", systemImage: "brain.head.profile").font(.headline)
                Text(lesson.question).font(.subheadline)
                ForEach(Array(lesson.options.enumerated()), id: \.offset) { index, option in
                    Button {
                        choice = index
                        if index == lesson.answer { store.state.quizPassed.insert(lesson.id) }
                    } label: {
                        HStack(alignment: .top) {
                            Image(systemName: choice == index ? (index == lesson.answer ? "checkmark.circle.fill" : "xmark.circle.fill") : "circle")
                            Text(option).multilineTextAlignment(.leading); Spacer(minLength: 0)
                        }.font(.subheadline).padding(13).frame(maxWidth: .infinity).background(choice == index ? (index == lesson.answer ? Palette.lime : Palette.clay) : Palette.paper, in: RoundedRectangle(cornerRadius: 12))
                    }.buttonStyle(.plain)
                }
                if let choice { Text((choice == lesson.answer ? "Exactly. " : "Try again. ") + lesson.explanation).font(.subheadline).foregroundStyle(Palette.muted).accessibilityIdentifier("quizFeedback") }
            }
        }
    }
}

struct SourceRow: View {
    let source: Source
    var body: some View {
        if let url = URL(string: source.url), url.scheme == "https" {
            Link(destination: url) {
                HStack(spacing: 13) {
                    Image(systemName: source.kind == "video" ? "play.rectangle" : "book.closed").font(.title3).frame(width: 32)
                    VStack(alignment: .leading, spacing: 4) { Text(source.title).font(.subheadline.weight(.medium)).multilineTextAlignment(.leading); Text(source.author + (source.kind == "video" ? " · Online video" : " · Reference")).font(.caption).foregroundStyle(Palette.muted) }
                    Spacer(minLength: 0); Image(systemName: "arrow.up.right").font(.caption)
                }.padding(16).background(.white, in: RoundedRectangle(cornerRadius: 18))
            }.buttonStyle(.plain)
        }
    }
}
