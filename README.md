# Stufo

A native iPhone study companion for Fender Studio Pro / Studio One: original lessons, visual explanations, guided workflows, and practical help for recording and producing music.

## Included

- 48 lessons across eight stages, with exercises, knowledge checks, notes, and completion tracking.
- 11 persistent session checklists, including Apollo vocal recording, delay throws, Logic migration, and mix delivery.
- 30 curated FAQ answers with an offline question matcher and relevant lesson links.
- 62 plain-English glossary entries.
- 21 curated video links from Studio Pro Toolbox and 17 reference/library links.
- Interactive delay/tap-tempo calculator, EQ map, compression curve, and signal-flow lab.
- Bookmarks, personal lesson notes, a session journal, and notebook export through the system share sheet.

## Build and install

Open `Stufo.xcodeproj` in Xcode 16 or later. The app targets iOS 17+ and uses SwiftUI with no third-party runtime dependencies. Choose your signing team for a normal device installation.

Pushing to `main` runs **Build unsigned IPA**. Its first job compiles an arm64 device app and uploads `Stufo-unsigned-IPA`. The IPA is deliberately unsigned and requires signing with the user's chosen signing/sideloading workflow before installation. The subsequent, bounded simulator job checks the core journey and captures native screenshots; it does not delay artifact upload. Each job is capped at ten minutes.

```sh
python3 scripts/content.py
xcodebuild -project Stufo.xcodeproj -scheme Stufo -configuration Release \
  -sdk iphoneos -destination 'generic/platform=iOS' \
  CODE_SIGNING_ALLOWED=NO CODE_SIGNING_REQUIRED=NO build
```

The checked-in project is reproducible with `python3 scripts/project.py`; ordinary builds do not require regeneration.

## Content and privacy

The written curriculum and diagrams are original educational material. Source references and credited video links are bundled in the app. Studio Pro Toolbox is Lukas Ruschitzka's independent tutorial index; linked videos remain with their original creators. No tutorials or videos are mirrored. Older videos may use Studio One terminology; written guidance is oriented toward Studio Pro 8.x. Manual/reference links were checked during creation on September 24, 2026.

Core features work offline. The assistant retrieves curated answers and lessons; it is not a cloud LLM, cannot inspect a DAW session, and does not analyze recordings. It acknowledges when no direct answer is available. Illustrative labs do not process audio. Learning progress indicates completed practice, not certified mastery.

Personal progress, bookmarks, notes, and checklists use app-local preferences. There are no accounts, API keys, analytics SDKs, or automatic uploads. External reference links open only when selected. Deleting the app removes local data; use notebook export to preserve writing.

## Small, intentional implementation

Four Swift source files, one bundled JSON curriculum, native navigation, system sharing, and direct local persistence. The content generator contains a single integrity check for IDs, references, and quiz answers. One UI smoke test checks loading, a bookmark across relaunch, search, a checklist, an assistant answer, and the tempo tool.

Future extensions should respond to actual use: deeper chapter packs, imported audio examples, or an optional model-backed assistant can be added independently. Keep the default experience fast and offline.
