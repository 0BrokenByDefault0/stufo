import SwiftUI

struct Chapter: Codable, Identifiable {
    let id, title, subtitle, symbol: String
}
struct Lesson: Codable, Identifiable {
    let id, chapter, title, subtitle, level, visual: String
    let minutes: Int
    let concepts, steps: [String]
    let mistake, practice, success: String
    let tags, sources: [String]
    let question: String
    let options: [String]
    let answer: Int
    let explanation: String
    var searchText: String { ([title, subtitle, mistake, practice] + tags + concepts + steps).joined(separator: " ") }
}
struct Workflow: Codable, Identifiable {
    let id, title, subtitle, symbol, time: String
    let steps, lessonIDs: [String]
}
struct FAQ: Codable, Identifiable {
    let id, question, answer: String
    let tags, lessonIDs: [String]
}
struct Term: Codable, Identifiable {
    var id: String { term }
    let term, meaning, example: String
}
struct Source: Codable, Identifiable {
    let id, title, author, url, kind: String
}
struct Curriculum: Codable {
    let chapters: [Chapter]
    let lessons: [Lesson]
    let workflows: [Workflow]
    let faqs: [FAQ]
    let glossary: [Term]
    let sources: [Source]
}
struct JournalEntry: Codable, Identifiable {
    var id = UUID()
    var date = Date()
    var title: String
    var body: String
}
struct SavedState: Codable {
    var completed = Set<String>()
    var saved = Set<String>()
    var checks = Set<String>()
    var notes: [String: String] = [:]
    var quizPassed = Set<String>()
    var journal: [JournalEntry] = []
    var lastLesson: String?
}

@MainActor final class StudioStore: ObservableObject {
    @Published var state: SavedState { didSet { save() } }
    @Published var error: String?
    let content: Curriculum
    private let key = "stufo.progress.v1"
    init() {
        let defaults = UserDefaults.standard
        #if DEBUG
        if ProcessInfo.processInfo.arguments.contains("--uitest-reset") { defaults.removeObject(forKey: "stufo.progress.v1"); defaults.removeObject(forKey: "stufo.bpm") }
        #endif
        state = defaults.data(forKey: "stufo.progress.v1").flatMap { try? JSONDecoder().decode(SavedState.self, from: $0) } ?? SavedState()
        do {
            guard let url = Bundle.main.url(forResource: "curriculum", withExtension: "json") else { throw CocoaError(.fileNoSuchFile) }
            content = try JSONDecoder().decode(Curriculum.self, from: Data(contentsOf: url))
        } catch {
            content = Curriculum(chapters: [], lessons: [], workflows: [], faqs: [], glossary: [], sources: [])
            self.error = "The lesson library could not be loaded. Please reinstall Stufo; saved notes are kept on this device."
        }
    }
    func save() {
        do { UserDefaults.standard.set(try JSONEncoder().encode(state), forKey: key) }
        catch { self.error = "Your latest progress could not be saved. Please keep the app open and copy any important notes." }
    }
    func toggle(_ id: String, in keyPath: WritableKeyPath<SavedState, Set<String>>) {
        if state[keyPath: keyPath].contains(id) { state[keyPath: keyPath].remove(id) }
        else { state[keyPath: keyPath].insert(id) }
    }
    func lesson(_ id: String) -> Lesson? { content.lessons.first { $0.id == id } }
    var nextLesson: Lesson? { content.lessons.first { !state.completed.contains($0.id) } }
    var resumeLesson: Lesson? { state.lastLesson.flatMap(lesson) ?? nextLesson }
    func chapter(_ id: String) -> Chapter? { content.chapters.first { $0.id == id } }
    func score(_ query: String, title: String, body: String, tags: [String] = []) -> Double {
        let stop: Set<String> = ["a","an","the","i","my","me","is","it","to","and","or","of","in","on","for","do","does","how","can","why","what","with","get","make","you","this","that","are","am","studio","pro","one","please"]
        func tokens(_ text: String) -> [String] { text.lowercased().components(separatedBy: CharacterSet.alphanumerics.inverted).filter { !$0.isEmpty && !stop.contains($0) } }
        let original = Set(tokens(query))
        guard !original.isEmpty else { return 0 }
        let groups = [["latency","lag","late","delay","buffer"], ["muddy","mud","muffled","boxy"], ["vocal","vocals","voice","rap"], ["silent","silence","sound","hear","monitor"], ["clipping","clip","distorted","distortion","crackle"], ["reverb","space","wet"], ["export","bounce","render","mixdown"], ["comp","comping","takes","layers"], ["tuning","pitch","autotune","tune"], ["eq","equalizer","equalisation","equalization"], ["logic","migrate","migration","transfer"], ["automate","automation","envelope"], ["duck","ducking","sidechain"], ["gain","level","volume"], ["save","backup","missing"], ["plugin","plugins","plug"]]
        var expanded = original
        for group in groups where !original.isDisjoint(with: group) { expanded.formUnion(group) }
        let titleWords = Set(tokens(title)), tagWords = Set(tokens(tags.joined(separator: " "))), bodyWords = Set(tokens(body))
        let exact = Double(original.intersection(titleWords).count * 7 + original.intersection(tagWords).count * 5 + original.intersection(bodyWords).count)
        let related = expanded.subtracting(original)
        let synonym = Double(related.intersection(titleWords).count * 2 + related.intersection(tagWords).count)
        return exact + min(synonym, 6)
    }
    func search(_ query: String) -> [Lesson] {
        guard !query.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else { return content.lessons }
        return content.lessons.map { ($0, score(query, title: $0.title, body: $0.searchText, tags: $0.tags)) }.filter { $0.1 > 1 }.sorted { $0.1 > $1.1 }.map(\.0)
    }
    var exportText: String {
        var lines = ["STUFO — MY STUDIO NOTEBOOK", "\(state.completed.count) lessons practiced · \(state.quizPassed.count) knowledge checks passed", ""]
        for lesson in content.lessons {
            if let note = state.notes[lesson.id], !note.isEmpty { lines += [lesson.title, note, ""] }
        }
        for entry in state.journal { lines += [entry.title, entry.date.formatted(date: .abbreviated, time: .omitted), entry.body, ""] }
        return lines.joined(separator: "\n")
    }
}

enum Palette {
    static let paper = Color(red: 0.965, green: 0.961, blue: 0.941)
    static let ink = Color(red: 0.12, green: 0.15, blue: 0.14)
    static let muted = Color(red: 0.37, green: 0.40, blue: 0.37)
    static let lime = Color(red: 0.79, green: 0.93, blue: 0.36)
    static let line = Color(red: 0.85, green: 0.87, blue: 0.82)
    static let purple = Color(red: 0.77, green: 0.72, blue: 0.94)
    static let clay = Color(red: 0.96, green: 0.72, blue: 0.57)
    static let teal = Color(red: 0.64, green: 0.82, blue: 0.77)
    static func chapter(_ id: String) -> Color {
        switch id { case "start", "finish": return lime; case "record", "create": return clay; case "edit", "advance": return purple; default: return teal }
    }
}

struct Eyebrow: View {
    let text: String
    var body: some View { Text(text.uppercased()).font(.system(.caption2, design: .monospaced, weight: .bold)).tracking(2).foregroundStyle(Palette.muted) }
}
struct Card<Content: View>: View {
    var color: Color = .white
    @ViewBuilder let content: Content
    var body: some View { content.padding(20).frame(maxWidth: .infinity, alignment: .leading).background(color, in: RoundedRectangle(cornerRadius: 24)).overlay(RoundedRectangle(cornerRadius: 24).stroke(Palette.ink.opacity(0.06))) }
}
struct PrimaryButton: ButtonStyle {
    var body: some View { EmptyView() }
    func makeBody(configuration: Configuration) -> some View {
        configuration.label.font(.system(.subheadline, weight: .semibold)).frame(maxWidth: .infinity).padding(.vertical, 16).background(Palette.ink, in: Capsule()).foregroundStyle(.white).opacity(configuration.isPressed ? 0.8 : 1)
    }
}
struct SearchField: View {
    @Binding var text: String
    var prompt = "Search lessons, skills, questions…"
    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: "magnifyingglass").foregroundStyle(Palette.muted)
            TextField(prompt, text: $text).font(.subheadline).autocorrectionDisabled().accessibilityIdentifier("librarySearch")
            if !text.isEmpty { Button { text = "" } label: { Image(systemName: "xmark.circle.fill") }.accessibilityLabel("Clear search") }
        }.padding(16).background(.white, in: RoundedRectangle(cornerRadius: 18)).overlay(RoundedRectangle(cornerRadius: 18).stroke(Palette.line))
    }
}
struct SectionTitle: View {
    let title: String
    var caption: String? = nil
    var body: some View {
        VStack(alignment: .leading, spacing: 5) {
            Text(title).font(.system(.title2, design: .rounded, weight: .bold))
            if let caption { Text(caption).font(.subheadline).foregroundStyle(Palette.muted) }
        }
    }
}
extension View {
    func pageStyle() -> some View { self.background(Palette.paper).foregroundStyle(Palette.ink) }
}
