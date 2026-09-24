import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
chapters = [
('start','Find your footing','Know the room, the signal, and the tools before chasing a sound.','compass.drawing'),
('record','Capture the feeling','A confident performance and a clean recording beat a complicated chain.','mic'),
('edit','Build the best take','Comp, clean, and tune without polishing away the personality.','scissors'),
('mix','Make it translate','Balance, tone, and dynamics that serve the song on real speakers.','slider.horizontal.3'),
('space','Create depth & movement','Delays, reverb, automation, and the moments people remember.','water.waves'),
('create','Develop your language','Rhythm, harmony, arrangement, and a sound that belongs to you.','pianokeys'),
('finish','Finish with intention','Turn a working session into a record you can confidently share.','checkmark.seal'),
('advance','Work like an artist','Build judgment, speed, and repeatable habits through deliberate practice.','sparkles')]
lessons=[]
def L(id, chapter, title, subtitle, visual, concepts, steps, mistake, practice, success, tags, sources, question, options, answer, explanation, minutes=8):
    lessons.append(dict(id=id,chapter=chapter,title=title,subtitle=subtitle,visual=visual,level='Foundation' if chapter in ['start','record'] else 'Intermediate' if chapter in ['edit','mix','space'] else 'Developing craft',minutes=minutes,concepts=concepts.split('\n\n'),steps=steps.split('|'),mistake=mistake,practice=practice,success=success,tags=tags.split(','),sources=sources.split(','),question=question,options=options.split('|'),answer=answer,explanation=explanation))

L('orientation','start','Find your way around','Five places you will use in almost every session.','arrangement',
"Think in jobs. The Arrange view is where performances live in time. The Console is where their sound is balanced and processed. The Browser finds audio, instruments, and effects. The Inspector exposes details for the selected item. The transport controls playback and recording.\n\nA track is the timeline container; a channel is the audio path in the mixer. They often correspond, but buses, effects returns, and multi-output instruments make the relationship less simple. Studio One tutorials may call a working document a Song; current Studio Pro calls it a Session.",
'Create an empty Session and save it in its own folder with an unmistakable name.|Open the Console with its onscreen button. Select a track and locate its corresponding channel.|Open the Browser, Inspector, and editor one at a time. Notice what remains selected as you change views.|Locate play, stop, record, tempo, the metronome, and the loop range before adding effects.',
'Opening every panel at once makes the application feel harder than it is. Keep only the panel you need visible.',
'Import a short beat, create one empty vocal track, rename both, and practice switching between arrangement and mixer without losing your place.',
'You can point to the audio event, its track, its channel, and the Main output without guessing.','interface,navigation,beginner,console,browser,inspector,song,session','console,toolbox',
'Where do you usually balance channel levels and insert effects?','The Console|The file name field|The metronome',0,'The Console exposes the channel signal paths. The Arrange view answers where a performance happens.')

L('signal','start','Follow the signal','Stop guessing where the sound disappeared.','signal',
"Every sound takes a route. For a microphone, start with the physical mic and cable, continue through the interface preamp and converter, then the DAW input, track, channel, output, and headphones. A meter tells you whether signal has reached that point.\n\nMonitoring and recording are different jobs. You can hear an input without recording it, or record an input while listening through a different monitoring path. Keeping those ideas separate solves a surprising number of beginner problems.",
'With playback stopped, speak and look for input on the interface.|Select the matching mono hardware input on the vocal track. Arm it and look for a meter response.|Check that the channel reaches your Main output, which reaches the interface outputs you actually use.|If one meter moves and the next does not, inspect the connection between those two stages before changing anything else.',
'Adding gain at the end of a broken route cannot fix a muted, disconnected, or wrongly selected input.',
'Draw your route in a session note, then deliberately mute one stage. Diagnose it using the meters and restore it.',
'You can locate a silent stage without changing three unrelated settings.','sound,silent,monitor,routing,input,output,microphone','audio,console',
'An interface meter moves but the DAW input meter does not. What should you inspect first?','The reverb decay|The DAW input assignment|The export format',1,'The problem is likely between the interface and selected DAW input, not downstream processing.')

L('audio-setup','start','Set up your Apollo session','One device, one sample rate, one monitoring plan.','signal',
"Use the Apollo as your Studio Pro audio device when it is your recording and listening interface. Match the session’s sample rate to your workflow and keep it consistent. 48 kHz and 24-bit recording are a practical starting point, not an automatic sound-quality upgrade over a well-made 44.1 kHz recording.\n\nCreate a mono input for the one microphone socket you are using and a stereo output for your speakers or headphones. A stereo track does not make one microphone more spacious; it can simply create an empty or redundant side.",
'In the audio-device settings, select Apollo for your recording and playback path.|In the session audio I/O setup, map a mono input to the actual Apollo mic input and confirm the stereo Main output.|Create a mono audio track, choose that input, and name it Lead Dry.|Record ten seconds and play it back with input monitoring disabled so you hear the recorded file.',
'A correct device selection does not guarantee that a particular track has the correct input. Check both.',
'Make a tiny setup session containing a beat and a dry mic track. Reopen it and prove that playback and recording still work.',
'You can capture and replay a clean mono voice with the correct left/right playback.','apollo,setup,48khz,sample rate,mono,stereo,interface','audio,ua-inserts',
'For one ordinary vocal microphone, what track format is the sensible starting point?','Mono|Stereo because it sounds wider|Surround',0,'One microphone provides one signal. Width is a later production decision.')

L('latency','start','Understand the delay you feel','Buffer size is a tradeoff, not a quality knob.','levels',
"A computer processes audio in blocks. Smaller buffers generally shorten the wait but give the computer less time to finish its work. Larger buffers give it breathing room during mixing. The buffer does not change the resolution of a recorded waveform.\n\nThe time you feel also includes converters, driver buffering, and plug-in latency. At 48 kHz, 128 samples is about 2.67 milliseconds for one block; it is not the total round-trip latency. Look-ahead limiting, linear-phase processing, and some DSP routing can add much more.",
'Choose how you will monitor: Apollo Console or the DAW. Avoid listening to both copies.|For DAW monitoring, start around 64 or 128 samples, then raise the buffer if the session crackles.|During recording, remove unnecessary high-latency processing from the live path and mix output.|During mixing, try 256 or 512 samples, or more if needed. There is no prize for a small buffer when nobody is performing.',
'If a high-latency plug-in is the problem, reducing the buffer alone may barely change what you feel.',
'Speak a short phrase with DAW monitoring at two buffer sizes. Then compare Console monitoring. Note which route you are actually hearing.',
'You can choose a stable recording setup and explain why your mixing setup can be different.','latency,lag,buffer,late,delay,crackle,1024,64,128','ua-latency',
'Does a larger buffer automatically make the recorded audio lower quality?','Yes|No; it mainly changes processing timing and stability|Only with a mono track',1,'Buffer size affects responsiveness and workload, not recording bit depth.')

L('gain','start','Leave space for the performance','Healthy recording levels without chasing the red.','levels',
"Recording gain begins at the microphone preamp. A mix fader changes what you hear later; it does not rescue a converter that clipped before the signal reached your session. Set gain using the loudest part of the actual delivery.\n\nFor a starting point, let energetic vocal peaks fall somewhere around −12 to −6 dBFS and leave extra room for an unpredictable performance. These are working ranges, not laws. Clean signal and consistent distance matter more than hitting one number.",
'Have the beat playing at a comfortable headphone level and rehearse the loudest line.|Adjust the interface preamp while watching its input meter and the DAW input.|Record a short test; listen for grit, overloaded syllables, room noise, and excessive breaths.|If peaks are safe but the voice feels quiet in headphones, change the monitor mix rather than pushing the preamp toward clipping.',
'Normalizing a quiet file later raises noise along with the vocal. Recording too hot trades a small convenience for irreversible damage.',
'Record a quiet phrase and your loudest phrase without moving the preamp. Find one setting that captures both cleanly.',
'Your loudest delivery remains clean and the quieter material is usable without extreme gain increases.','gain,clipping,distortion,level,headroom,dbfs,preamp','audio',
'Your input clips before recording. Which control should you address first?','The interface preamp gain|The reverb send|The master export name',0,'The overload happens upstream. A downstream fader cannot unclip that recording.')

L('files','start','Save a session you can trust','Make tomorrow’s session open like today’s.','export',
"A session file is a set of decisions and references. It is not automatically a container for every audio file you used. A beat dragged from Downloads or an external drive can remain dependent on that location unless copied into the session’s media.\n\nUse a simple folder system: one song folder, clear versions, and a separate backup. A sync folder is useful but can faithfully sync a deletion too. Keep at least one additional version you can recover independently.",
'Name the session with the song title and save it before recording.|Use the session’s media-management options to bring external audio into the session folder; verify what the option says in your version.|Save a new version before major edits or printing processing.|After closing the DAW, make a backup copy. Reopen the working session and check for missing-media warnings.',
'Renaming or moving source audio in Finder can break references. Use the DAW’s media-management tools when reorganizing an active song.',
'Make a copy of a tiny practice session with its media and open the copy independently. Confirm that the beat and vocal both play.',
'You know where your session, media, exports, and recoverable backup live.','save,backup,missing,files,media,folder,archive','v-save',
'Why can a session file open with missing audio?','The session can reference audio stored elsewhere|The tempo was too slow|A mono mic requires stereo media',0,'The session’s references and the actual media are separate unless the files have been collected.')

L('apollo-monitor','record','Monitor once, record deliberately','Console, UAD MON, and the sound you actually keep.','signal',
"Apollo Console can let you hear yourself without waiting for a round trip through the DAW. If you also enable software input monitoring, you may hear a second delayed copy: hollow, phasey, doubled, or echoing. Choose a single monitoring route.\n\nFor ordinary Console insert slots, UAD MON lets you hear processing without committing those inserts to the DAW input; UAD REC prints them. Unison processing has its own behavior and is committed on the input path. Do not assume MON makes a Unison preamp fully reversible.",
'Choose Console monitoring and turn off the Studio Pro track’s software monitor button while recording into the correctly armed track.|Start with an intentionally dry, clean capture. Check the Console REC/MON state on the channel you use.|Keep a tasteful headphone effect if it helps performance, while confirming whether that effect is being recorded.|Record a test, then bypass playback effects and listen to the actual captured file.',
'UAD Spark/native plug-ins run on the computer; they are not automatically the same as the Apollo DSP versions available in Console.',
'Record one sentence with your intended Console setup, then inspect playback with no DAW inserts. Write down exactly what was printed.',
'You know which processing is permanent and hear only one live copy of your voice.','apollo,console,uad,monitor,double,echo,unison,dry,wet','ua-inserts',
'You hear a phasey duplicate of your live voice. What is a good first check?','Whether Console and DAW monitoring are both audible|Whether the song title is too long|Whether export is set to WAV',0,'Two monitoring paths can create a delayed duplicate of the same performance.')

L('mic-technique','record','Get closer to a better vocal','The room and performance are part of your sound.','signal',
"Before EQ, listen to what the microphone hears. A bare reflective room adds a short, hard echo that can be difficult to remove. A consistent distance, controlled headphone spill, and a pop filter can improve a recording more than another processor.\n\nStart about a handspan away and adjust to the microphone and delivery. Closer can add weight and intimacy; farther can capture more room. Aim slightly across the capsule if plosives are excessive, then listen for lost clarity. Move with intention, not randomly.",
'Choose the quietest practical part of the room. Place absorption where reflected sound is strongest; avoid assuming thin foam fixes bass.|Set a pop filter and mark a comfortable standing position.|Perform the loudest section at the distance you will actually use, then set gain.|Record two distances and compare at matched playback level in the beat.',
'A louder playback can make one position seem better. Match levels before judging the tone.',
'Record the same four bars close, medium, and slightly off-axis. Pick the version that needs the least correction.',
'Your consonants are clear, plosives are controlled, and the vocal does not change tone every time your head moves.','microphone,room,plosive,pop filter,acoustics,recording','toolbox',
'Which is a useful first response to repeated plosive blasts?','Try placement, distance, and a pop filter|Add 10 dB of treble|Normalize every syllable',0,'Preventing the burst at capture is usually cleaner than trying to repair it later.')

L('first-recording','record','Record your first usable vocal','A ten-minute route from silence to a take.','arrangement',
"A good first recording session has a narrow goal: a beat plays, a mic records, and you can hear the result. Leave the elaborate vocal chain for later. Setup friction steals attention from delivery.\n\nUse a lead track for the main performance and separate tracks for doubles and ad-libs. Naming the role now makes later routing much easier. A dry lead is a flexible source for every later decision.",
'Import the beat and set the tempo intentionally. If the beat already plays at the right speed, do not accidentally stretch it.|Create a mono lead track with the correct input. Choose one monitor path and test the recording level.|Give yourself a count-in or a few bars of lead-in. Record a short complete section rather than restarting after every small mistake.|Stop, disarm if needed, and play back. Save before adding another layer.',
'Hearing the live input is not proof that audio was recorded. Confirm that a waveform exists and the recorded file plays.',
'Capture eight bars in three complete passes. Keep going through a small mistake so you learn which errors matter musically.',
'Three takes are safely captured and you can identify the strongest overall performance.','record,first,vocal,rap,arm,count in,beat','audio,v-record',
'What proves that a take was captured?','Hearing your live mic alone|Playing back the recorded event|Seeing a plug-in window',1,'Playback of the recorded event verifies the actual captured material.')

L('takes','record','Record takes to layers','Keep alternatives without making a mess.','comping',
"Layers let alternate performances share a track’s processing and routing. They are especially useful when you want several attempts at the same phrase but only one lead vocal at a time. A separate track is better when you want performances to sound together.\n\nIn the Record panel, Record Takes to Layers places successive takes into layers. The latest take becomes the active track material. Later you can build a comp from the best phrases while retaining the alternatives.",
'Define a short recording range that includes a natural lead-in and the phrase ending.|Enable Record Takes to Layers in the Record panel; check recording behavior with a small test.|Record three complete passes, changing only one intention per pass: calm, urgent, or conversational.|Expand the layers and label memorable takes before listening again.',
'Comping every syllable immediately can hide the fact that one full take has better momentum. Start with a performance, then repair it.',
'Record one hook three ways and select the strongest full take before making any edits.',
'You can switch alternatives without losing takes or accidentally stacking all of them.','takes,layers,loop,record,alternates,comping','layers,v-layers',
'When do separate tracks make more sense than alternate layers?','When two vocals should play together|When you want only one alternate performance|When you want fewer files at any cost',0,'Separate tracks give simultaneous parts independent mix control.')

L('doubles','record','Build doubles that feel intentional','Width starts with another performance.','stereo',
"A double is a new performance of the same part. Tiny differences in pitch, timing, and tone can add size. Copying a file makes an identical signal; panning two identical copies does not create the same natural width.\n\nUse doubles where the arrangement needs support: a hook, an emphasized phrase, or a response. Constant stacking can make the lead less personal. Keep the strongest storytelling voice as the anchor.",
'Record the lead first and decide which words deserve reinforcement.|Perform a new left and right double, matching important consonants and phrase endings.|Lower both doubles until you mainly notice their absence when muted.|Check mono and reduce width tricks if the vocal becomes thin or unstable.',
'Perfectly aligning every detail can remove useful human variation. Fix distracting flams; preserve the feeling.',
'Compare an eight-bar hook with doubles throughout against doubles on only its last two lines.',
'The added voices make the section lift while the lyric stays easy to understand.','double,doubles,stack,width,stereo,hook','v-align',
'Why is a new double different from a copied lead file?','It contains a distinct performance|It is automatically louder|It needs no editing',0,'Performance differences create a texture that identical copies do not.')

L('performance','record','Direct your own performance','Record an intention, not just the right words.','arrangement',
"Technical confidence gives you room to perform. Decide who the line is addressed to and what changes emotionally across the verse. An understated delivery can feel intense when its timing and consonants are committed.\n\nA useful take note describes a result: clearer ending, less rushed, stronger first word. A vague instruction like better gives you nothing to try. Capture contrasts and choose in context, not from memory.",
'Mark breaths, key words, and the emotional turn in the lyric.|Record one controlled pass, one more animated pass, and one quieter intimate pass.|Listen with the beat and compare the meaning, not just precision.|Keep the take that serves the song; use another only where it fixes a clear weakness.',
'Recording endless exhausted takes can make the performance smaller. Step away when you stop hearing meaningful differences.',
'Choose four bars and change only emphasis on each pass. Note which version makes the lyric easiest to believe.',
'You can name the intention of the take you chose.','performance,rap,delivery,flow,breath,takes','toolbox',
'Which take direction is most actionable?','Make it better|Leave more space before the last word|Sound expensive',1,'A specific performance change can be attempted and evaluated.')

L('logic-migration','record','Bring a Logic song with you','Move the music while preserving your options.','export',
"A DAW project is not a universal format. Plug-in states, take folders, routing, and automation do not all translate by moving the project file. Aligned audio is the most reliable bridge. Export a reference mix too so you can compare the result.\n\nChoose a common start and end for every file, including silence before late entries. Keep the original Logic project. Print creative sounds you need to preserve and export dry alternatives for decisions you want to remake.",
'Save a duplicate Logic project. Write down sample rate, tempo, time signature, and any tempo changes.|Export tracks as audio files with consistent ranges, 24-bit WAV, and normalization off. Decide explicitly whether processing and automation are included.|Print instruments or special bus effects you rely on, and retain dry vocal files and a stereo reference. Do not assume aux returns are included in a track export.|Create a Studio Pro session at the same sample rate, import the aligned files to the same start, and compare against the reference before editing.',
'Files that start at each region’s own first sound will not line up when all are dropped at bar one. Verify alignment at both the start and end.',
'Migrate a one-minute excerpt before moving an entire song. Confirm a late ad-lib and the final downbeat land correctly.',
'The destination plays in time and you know which sounds are printed versus editable.','logic,migrate,migration,transfer,stems,import,export','logic-export',
'What most reliably preserves alignment during an audio migration?','Export every track from a common start|Trim all starting silence independently|Normalize every track',0,'A shared origin preserves the timing relationship even for late entries.')

L('comping','edit','Comp for a believable performance','The best take still needs to sound like one take.','comping',
"Comping assembles chosen parts of different takes into one performance. Start with a strong main take and replace only what improves the song. Timing, breath, tone, and emotional continuity matter as much as pitch.\n\nIn Studio Pro, expand the layers and select useful ranges to promote into the active performance. Work in phrases first. A perfect word from a dramatically different mic distance may be worse than a slightly imperfect word that belongs.",
'Listen through without editing and mark only clear problems.|Expand the take layers and audition alternate phrases for those moments.|Build the comp using natural word or breath boundaries. Check transitions in context.|Keep the source layers and save a version before consolidating or printing the comp.',
'A cut in the middle of a vowel often changes tone or pitch abruptly. Move the seam to a quieter boundary when possible.',
'Build one eight-bar comp using no more than five replacements. Listen without looking at the screen.',
'You hear one convincing delivery and cannot easily identify the edit points.','comping,comp,takes,layers,edit,vocal','comping,v-comp',
'What is usually the best first comping strategy?','Replace every syllable|Start with a strong full take and repair specific weaknesses|Always choose the loudest words',1,'A strong base performance preserves continuity and reduces unnecessary editing.')

L('fades','edit','Make clean edits and fades','Remove the click, keep the breath.','edit',
"A hard edit can cut a waveform at a discontinuity and create a click. Short fades soften the entry and exit; a crossfade blends overlapping pieces. The right length depends on the material. A fade that fixes a click can also erase a consonant if it is too long.\n\nBreaths are part of phrasing. You do not need to delete every breath or fill every pause with digital silence. Turn distracting breaths down and preserve the ones that make the performance feel human.",
'Zoom in far enough to place an edit accurately, then make a cut at a natural boundary.|Use event fade handles for a short fade-in or fade-out; start with a few milliseconds and listen.|Where pieces overlap, use a crossfade and adjust its length until no click or doubled syllable remains.|Zoom back out and check the whole phrase with the beat.',
'Solo listening can tempt you to make an unnaturally silent vocal. Judge most cleanup in the actual arrangement.',
'Create one intentionally bad seam in a practice copy, repair it with fades, and compare before and after.',
'The edit is quiet without dulling the beginning of the word.','fade,fades,click,scissors,edit,crossfade,breath','v-fades,comping',
'What should you check after extending a fade-in?','Whether it softened the first consonant too much|Whether the file name changed|Whether the tempo doubled',0,'A fade affects performance details, not just clicks.')

L('clip-gain','edit','Even the vocal before compression','A little preparation makes a better chain.','levels',
"One shouted word can drive a compressor much harder than the rest of a line. Clip or event gain lets you reduce that outlier before it reaches the processor. This is different from riding the channel fader after processing.\n\nUse gain editing for large inconsistencies and fader automation for the final musical relationship with the beat. You are preparing an expressive performance, not making every waveform the same height.",
'Listen for words that jump out or vanish before adding a heavy compressor.|Adjust event gain or a clip-gain curve for the specific phrase or syllable.|Replay through the compressor and notice whether its reduction is now more consistent.|Keep meaningful loud/soft contrasts and avoid raising background noise between words.',
'Waveform size is a clue, not a loudness verdict. Different vowels can look different while sounding balanced.',
'Prepare four uneven lines with gain moves, then use less compression than before. Compare articulation and energy.',
'The compressor reacts more evenly and the performance still breathes.','clip gain,event gain,volume,uneven,syllable,compression','clip-gain',
'Why use clip gain before a compressor?','To shape what reaches its detector|To add reverb tails|To change the sample rate',0,'Upstream gain changes how strongly the compressor reacts.')

L('timing','edit','Tighten the pocket','Fix distractions without snapping the life away.','arrangement',
"Rhythmic feel lives around the grid as well as on it. A vocal can lean behind the beat and still feel locked. Judge where a phrase lands against the snare, kick, and bass instead of assuming every syllable should touch a line.\n\nFor doubles, distracting consonant flams often matter more than tiny vowel differences. Move phrases first and use stretching sparingly. Repeatedly stretching a whole vocal to fix one word can damage unrelated material.",
'Choose one rhythmic reference in the beat and listen to the vocal against it.|Identify a phrase that sounds late or early, not merely one that looks off-grid.|Move or locally edit the smallest useful region. Preserve breaths and neighboring transitions.|Compare the original at the same level and check the doubles for flams.',
'A visually neat waveform arrangement can still sound stiff. Close your eyes for the final decision.',
'Make a tight version and a relaxed version of four bars. Choose the one that makes the groove feel better.',
'The phrase lands intentionally and still sounds like you.','timing,grid,quantize,pocket,align,double,stretch','v-align',
'What should guide a vocal timing edit?','Its relationship to the groove|The prettiest waveform spacing|A rule that every word must start on a beat',0,'Timing choices are musical. The grid is a reference, not a performance.')

L('tuning','edit','Tune with an intention','Natural control or an audible effect — choose deliberately.','eq',
"Pitch correction needs a sensible target. A wrong key or scale can pull intentional notes to the wrong place. Spoken or heavily percussive rap may not benefit from the same settings as a sung hook. Start by identifying the melody and listening against the harmonic backing.\n\nFaster correction can create a stylized, stepped sound; slower correction tends to preserve more transition and drift. Formant controls change vocal character separately from the basic musical pitch. Neither should be adjusted just because the control exists.",
'Comp the performance first, keeping a dry original.|Identify the key from the actual music; verify the proposed notes against the beat rather than trusting one automatic guess.|Use the pitch tool you own, choose the appropriate input range, and compare a subtle setting with an intentional effect.|Listen to held notes and slides. Back off when the correction fights the phrase instead of helping it.',
'Using the same correction speed on every note can make a nuanced delivery unstable or robotic in the wrong places.',
'Create natural and obviously tuned versions of the same hook. Level-match and write what each version communicates.',
'The tuning supports the melody and character without pulling notes to unintended targets.','tuning,pitch,autotune,antares,melodyne,formant,scale,key','v-tune',
'What should you verify before increasing correction strength?','The musical key and intended notes|The export file extension|The reverb color',0,'Strong correction toward the wrong notes makes the musical error more obvious.')

L('cleanup','edit','Know what repair can and cannot do','Remove distractions without sanding off the voice.','edit',
"Noise reduction, de-clicking, and de-essing solve different problems. A steady fan is not the same as a mouth click, a plosive, or a bright consonant. Name the problem before picking the processor.\n\nTools such as iZotope RX can help rescue a take, but strong repair can leave watery, chirping, or dull artifacts. Sometimes moving a mic or recording a line again is faster and more convincing. Keep the original and compare in context.",
'Listen to a pause and a loud phrase. Describe the unwanted sound in plain language.|Try an edit or small gain change before processing the entire file.|If using repair, target the narrowest useful region and start gently.|Level-match the result and listen for damage to consonants, room decay, and sustained vowels.',
'An impressively silent gap does not prove that the words still sound good. Evaluate the voice while it is present.',
'Repair one mouth click and one noisy pause. Compare the full phrase with the untouched original.',
'The distraction is lower without making the vocal sound processed.','noise,repair,rx,izotope,click,denoise,plosive','toolbox',
'What is the best first step in choosing a repair tool?','Identify the type of problem|Apply the strongest denoiser preset|Remove every breath',0,'Specific problems call for specific tools and often smaller edits.')

L('balance','mix','Build a mix with the faders','The most powerful move is often the simplest.','levels',
"Balance is the relationship between parts. If the lyric is buried, first decide whether the vocal is too quiet or the beat is too dominant. An EQ curve is not a substitute for choosing which element leads the song.\n\nMake an initial balance at a comfortable, fairly quiet playback level. Loud monitoring can make almost anything feel exciting. Return to a consistent volume so you can compare decisions fairly.",
'Begin with the lead vocal and the beat, with unnecessary processing bypassed.|Bring up the lead until every important lyric reads. Then adjust the beat around it.|Add doubles, ad-libs, and effects one role at a time, keeping the lead as your anchor.|Listen at a quieter level, then briefly on another playback device. Fix balance before adding polish.',
'If every element is made louder to compete, the mix eventually just overloads. Lower competing parts when appropriate.',
'Make a 60-second balance using only faders and pan. Export it as a baseline for later comparisons.',
'The song communicates before any elaborate processing is added.','balance,volume,fader,buried,beat,vocal,mix','console',
'Before boosting vocal treble to fix a buried lyric, what should you assess?','The vocal-to-beat balance|The app theme|The bit depth of your notes',0,'A level relationship can be the real issue; tonal processing may be unnecessary.')

L('eq','mix','Hear what an EQ move is doing','Frequency, gain, and width have different jobs.','eq',
"Frequency chooses where a move is centered, gain chooses how much boost or cut, and Q controls how concentrated a bell is. A broad small move can reshape tone; a narrow move can address a clearly heard resonance.\n\nListen in the beat. A vocal that sounds huge alone can crowd the bass and keys; a soloed vocal that seems slightly lean can sit beautifully in the record. The aim is useful separation, not a perfect-looking curve.",
'Name a problem: rumble, too much low-mid weight, a harsh vowel, or insufficient clarity.|In Pro EQ or Pro-Q, use a small move with an appropriate shape and listen in context.|Bypass at similar loudness so a louder processed version does not win automatically.|Keep the band only if you can describe the audible improvement.',
'Sweeping an extreme boost makes almost every frequency sound offensive. Use that technique cautiously, then judge a modest cut in context.',
'Make no more than three EQ moves on a vocal. Write one reason for each; remove any you cannot justify.',
'You can predict which part of the voice a band changes before turning it on.','eq,equalizer,frequency,q,bell,muddy,harsh,tone','proq-bands',
'Which control mainly changes the width of a bell band?','Q|Pan|Sample rate',0,'Q determines how narrow or broad the bell is around its center.')

L('low-cut','mix','Low cut means high pass','Find the right shape in Pro-Q without guessing.','eq',
"A high-pass filter lets higher frequencies pass while reducing lower ones. FabFilter calls this shape Low Cut. A low shelf is different: it lowers or raises a broad low range without necessarily removing everything below the corner.\n\nStart low and move the cutoff upward while the beat plays. Listen for reduced rumble, then for the point where the voice loses weight. Back off from that point. There is no universal vocal cutoff; the source and arrangement decide.",
'Create or select a band in Pro-Q and set its shape to Low Cut.|Begin around the lowest unwanted rumble, using a moderate slope such as 12 dB/oct as an experiment.|Raise the cutoff gradually while listening to the lower body of the voice.|Compare bypassed and active, then try a gentler setting if the voice has become thin.',
'A steep filter can alter the transient and phase response. Steeper is not automatically cleaner or more professional.',
'Compare Low Cut with a low-shelf reduction on the same vocal. Notice when one solves the problem with less loss of body.',
'You can choose the shape by its function rather than its icon.','high pass,highpass,low cut,pro q,fabfilter,filter,rumble','proq-bands,proq-mode',
'In Pro-Q, which shape performs a high-pass function?','Low Cut|Low Shelf|High Cut',0,'Low Cut removes low-frequency content and passes the higher range.')

L('compression','mix','Compress for consistency','Threshold starts the action; timing shapes the feeling.','dynamics',
"A compressor turns down signal according to a detector and settings. Threshold sets where gain reduction begins; ratio sets how strongly level above that region is controlled. Attack and release shape the response over time. Makeup gain brings the result back up afterward.\n\nFor a vocal experiment, try a moderate ratio around 3:1, an attack in the tens of milliseconds, and a release that recovers naturally between phrases. These are starting points. Watch reduction and listen; the displayed numbers are not a recipe for every voice.",
'Even large level outliers with clip gain first.|Lower the compressor threshold until louder words are controlled without flattening every syllable.|Compare faster and slower attack while listening to consonant impact; adjust release to avoid distracting pumping.|Match output loudness to bypass and decide whether the voice is easier to follow.',
'If the processed version is simply louder, you have not proved that compression improved it.',
'Use the compression lab, then compare two real vocal settings: one clearly overdone and one restrained. Identify the audible difference.',
'The vocal stays present and expressive, with no unexplained pumping or crushed diction.','compression,compressor,threshold,ratio,attack,release,pro c','toolbox',
'At an ideal 4:1 ratio, 8 dB above the threshold becomes how much above it?','2 dB|8 dB|32 dB',0,'Eight divided by four is two. Timing and knee can change real-time behavior.')

L('deess','mix','Control sharp consonants','Treat the “S” without losing the whole voice.','eq',
"Sibilance is the sharp energy in sounds such as S, SH, and sometimes T. Its frequency varies with the singer and microphone. A de-esser reacts to that energy; it should not darken every vowel just because the vocal is bright.\n\nStart with careful recording and reasonable EQ. Boosting air heavily and then aggressively de-essing can create a cycle of undoing your own decisions. If one isolated consonant is the problem, a gain edit can be cleaner.",
'Find a phrase containing both bright consonants and sustained vowels.|Use a de-esser such as Pro-DS or your available equivalent; listen to its detection or audition function if provided.|Adjust sensitivity so reduction mainly follows the troublesome consonants.|Compare full phrases with the beat and listen for a lisp, dullness, or disappearing endings.',
'A de-esser that sounds smooth on one aggressive word can be too strong for the rest of the performance.',
'Fix one harsh S with gain editing and another with de-essing. Compare which intervention is least noticeable.',
'The consonants remain intelligible without jumping painfully out of the mix.','deess,de esser,sibilance,sss,sharp,harsh,pro ds','toolbox',
'What is a sign of excessive de-essing?','A lisp or lost consonants|A clearer song title|More accurate tempo',0,'Over-reduction can erase the very sounds that make speech intelligible.')

L('vocal-chain','mix','Give every plug-in a job','Use the tools you own without using all of them.','signal',
"A useful chain is an ordered set of decisions. A practical starting sequence might be corrective EQ, compression, de-essing where needed, and optional color. Reverb and delay often live on separate sends. Change the order when the sound gives you a reason.\n\nYour stock tools can handle the fundamentals. Pro-Q can shape tone, your compressor can control dynamics, and saturation can add texture. Soothe can reduce moving resonances when used carefully. iZotope, UAD, Antares, and LANDR are choices, not mandatory stages.",
'Write a one-sentence job for each insert before loading it.|Build one processor at a time and compare at similar loudness.|If compression brings sharp consonants forward, revisit de-essing placement or intensity.|Save a useful chain as a starting point, then retune it for every recording.',
'Stacking processors that solve the same problem can quietly remove clarity and expression. Remove any stage you cannot hear helping.',
'Take an existing vocal chain and bypass one plug-in at a time. Keep only the ones with a clear audible purpose.',
'You can explain the chain in plain language and it still sounds good with fewer distractions.','chain,plugins,soothe,izotope,uad,landr,fabfilter,antares,stock','routing,v-stock',
'When should you add another processor?','When it solves an identified audible problem or creative goal|Because an influencer uses ten|Whenever an insert slot is empty',0,'A processor earns its place by improving this recording, not by being available.')

L('stereo-mono','mix','Make width survive mono','A wide mix still needs a strong center.','stereo',
"Panning places different signals across the stereo field. Time and phase differences can create width too, but some widening techniques cancel when left and right are combined. A mix that disappears in mono is not simply more spacious.\n\nKeep the lead and important low-end relationships stable. Use the sides for supporting performances and ambience when it helps the arrangement. Test the whole mix, because a beautiful soloed stereo effect may fight the vocal once everything returns.",
'Build a useful balance with the main vocal anchored near the center.|Pan true doubles and supporting parts to make room rather than widening everything.|Switch the monitoring output to mono and compare at a reasonable matched level.|If a part collapses, reduce stereo timing tricks, check polarity relationships, or choose a different texture.',
'A duplicated track with a tiny delay can sound wide and still create comb filtering. Treat it as an effect with a tradeoff.',
'Listen to a hook in stereo, mono, and through one small speaker. Note what changes in lyric intelligibility.',
'The hook keeps its meaning and essential energy on narrow playback.','stereo,mono,width,phase,pan,correlation,cancel','toolbox',
'Why check mono?','To reveal cancellation and judge the core balance|To make every mix permanently mono|To increase sample rate',0,'Mono is a practical translation check, especially after widening effects.')

L('sends','space','Inserts, buses, and sends','Three routing ideas that unlock the mixer.','signal',
"An insert processes a channel in sequence. A send creates an additional route to another channel. A bus combines sources so you can treat them as a group. These are signal-flow jobs, not competing names for the same thing.\n\nFor shared ambience, keep the dry vocal on its normal path and send some of it to an FX channel. Set the reverb or delay there fully wet so the original dry sound is not unintentionally duplicated. The send controls the feed; the return fader controls the processed output.",
'Locate the lead channel’s Inserts and Sends areas in the Console.|Create an FX channel containing a delay, then add a send from the lead to that FX channel.|Set the effect’s mix to 100% wet and bring up the send gently.|Mute the send and then the return separately. Listen to which action stops new input and which cuts the effect output.',
'A partly dry effect on a parallel return can change the original level and obscure what the send is doing.',
'Create one shared reverb for lead and doubles with different send amounts. Keep the return at a stable level.',
'You can follow both the direct sound and the effect path without guessing.','send,sends,bus,insert,fx,wet,dry,routing','routing',
'For a conventional parallel reverb return, where should the reverb mix begin?','100% wet|100% dry|Always 50/50',0,'The source channel already carries the dry sound; the return supplies the effect.')

L('delay-throw','space','Throw the last word into space','Automate the send. Let the tail finish.','automation',
"A throw highlights a chosen word or phrase with an echo. The dry lead stays stable while only that moment feeds the delay. It is a rhythmic response to the lyric, not a wash over the entire verse.\n\nStart with a tempo-synced quarter or eighth note, modest feedback, and a return that does not compete with the next line. Darkening or thinning the repeat can separate it from the main voice. There is no correct wet level until you hear it in the song.",
'Create a delay FX return at 100% wet and a send from the lead.|Expose that send’s level as an automation parameter. Draw points at silence before the target word, up through the word, and back down afterward.|Set the automation to Read and play from before the phrase so the initial state is established.|Adjust the rise timing, send amount, and feedback until the response finishes musically. Leave the return active so the existing tail can decay.',
'Automating the return mute or delay bypass can cut off the tail. Automating an insert’s dry/wet mix can also change the lead itself.',
'Create three different throws across a verse: one short, one syncopated, and one final long answer. Keep the rest comparatively dry.',
'Only the intended word repeats, and the next lyric remains clear.','throw,delay,throws,echo,last word,automate,send','automation,editing-automation,v-throw',
'Which parameter is a useful first choice for a clean vocal delay throw?','The send level feeding the delay|The dry vocal pan for the whole song|The return mute throughout the tail',0,'Controlling the feed selects the word while allowing the delay already inside the effect to decay.')

L('reverb','space','Choose depth, not fog','Size, decay, and pre-delay tell different stories.','space',
"Reverb suggests a space around the sound. Decay describes how long it lingers; pre-delay creates a gap before the reverberant response; tone shapes how bright or dark that space feels. A short room and a long plate can communicate very different distances.\n\nStart with the vocal’s role. An intimate lead often needs less obvious ambience than a distant ad-lib. Pre-delay can preserve the initial articulation, but too much can sound like a separate echo. Judge against the rhythm.",
'Create a fully wet reverb return and feed it quietly from the lead.|Choose a short, restrained space first and raise it until you hear what it adds.|Adjust decay and pre-delay while checking consonants and the gaps between lines.|Filter the return if its low end muddies the beat or its brightness exaggerates S sounds.',
'A soloed lush reverb can swallow the song. Set the amount with the full arrangement playing.',
'Compare a close verse and a deeper hook using the same dry vocal. Change the ambience, not the lead’s fundamental balance.',
'The voice sits in a space without losing the words.','reverb,predelay,decay,plate,room,wet,fog','v-reverb',
'What does pre-delay mainly change?','The gap before the reverberant response|The singer’s pitch|The recording bit depth',0,'That gap can help separate the direct articulation from the surrounding space.')

L('automation','space','Make automation predictable','Draw a move, read it back, keep control.','automation',
"Automation stores a parameter’s value over time. Read plays back the curve. Touch writes while you manipulate the control and then returns toward existing automation. Latch continues writing the last value after release until playback stops. Write can overwrite throughout playback.\n\nFor your first moves, draw a simple curve and use Read. Add points before and after the change so it returns to a known baseline. The parameter you choose determines what changes: channel volume, send level, or a plug-in’s mix are different operations.",
'Choose one parameter and reveal its automation lane.|Place a baseline point before the section, points defining the move, and a return point afterward.|Use Read and replay from earlier in the song to hear the full behavior.|If recording live moves with Touch or Latch, return to Read afterward and inspect the curve.',
'Leaving Write or Latch active can replace a carefully drawn section on the next pass.',
'Draw a 1–2 dB lift into a hook, then a separate delay-send throw. Explain which signal each curve controls.',
'The move happens in the same place on repeated playback and returns to the intended value.','automation,read,touch,latch,write,curve,envelope,mix','automation-modes,editing-automation',
'Which mode is the safest default for replaying existing automation without writing new moves?','Read|Write|Latch',0,'Read follows the stored values rather than recording control changes.')

L('ducking','space','Let effects move around the vocal','Space can bloom when the lyric pauses.','dynamics',
"Ducking lowers one sound while another is present. For a vocal reverb or delay, put compression on the effect return and let the dry voice drive the detector through a sidechain. The effect gets quieter during the line and returns in the gaps.\n\nThe sidechain is a control signal. It need not become audible in the return itself. Release timing determines whether the effect comes back naturally or swells in a distracting way.",
'Begin with an existing wet effect return that sounds good on its own.|Insert a sidechain-capable compressor after the effect and enable its external detector input.|Route a controlled feed from the dry vocal to that sidechain, keeping the normal vocal and FX paths intact.|Adjust threshold and release until the words read clearly and the ambience returns smoothly between them.',
'Over-ducking can create an obvious sucking sensation. Use the smallest reduction that solves the masking.',
'Compare a static return against a gently ducked one at similar average loudness. Listen especially to the space after the last word.',
'The effect supports the vocal and emerges naturally in its gaps.','duck,ducking,sidechain,reverb,delay,masking','routing,v-duck',
'What does the external sidechain primarily supply to the compressor?','A signal that controls its gain reduction|A new song tempo|A mandatory audible harmony',0,'The detector listens to the sidechain to decide how the return should be controlled.')

L('creative-fx','space','Design a signature vocal moment','One memorable contrast can carry a section.','stereo',
"A signature effect works because of where it appears and what surrounds it. A filtered whisper, distorted reply, pitched double, or abrupt dry moment can feel more original than a large permanent chain. Contrast creates impact.\n\nUse references to describe a quality: intimate, grainy, unstable, spacious, clipped, or playful. Then translate that quality into a controllable experiment on your own performance. You are building a vocabulary, not copying someone’s entire identity.",
'Pick one phrase that deserves a change and duplicate it to a clearly labeled effects track.|Try one main transformation: filtering, saturation, pitch/formant change, or rhythmic repeats.|Blend it with the lead and automate when it enters and leaves.|Print an alternate version once it works, preserving the dry source and an editable copy.',
'An effect that is exciting for four seconds can become tiring for an entire verse. Use the arrangement as a control.',
'Make three one-line responses: intimate and dry, grainy and narrow, then airy and distant. Choose the one that adds meaning.',
'The effect makes the phrase more memorable without obscuring the lyric or swallowing the next section.','creative,texture,saturation,formant,signature,adlib,osquinn,isaiah,idk','v-creative',
'Why can a brief effect feel stronger than the same effect running constantly?','Contrast gives it a clear role|It uses a higher sample rate|Short effects always need more gain',0,'The surrounding untreated sound helps the change register as an event.')

L('rhythm','create','Build a pocket before a pattern','Timing and empty space are musical material.','arrangement',
"A drum pattern is a set of relationships: what repeats, what surprises, and what leaves room for the voice. Begin with an anchor, such as the snare, then decide how the kick and hats support the phrasing. Faster subdivisions do not automatically create more energy.\n\nVelocity, note placement, and sound choice interact. A hat pattern can feel mechanical when every hit has the same emphasis. Small intentional variations are useful; randomizing everything can destroy the groove.",
'Start a short loop with a clear backbeat and a simple kick pattern.|Add hats that imply movement without filling every available subdivision.|Change the strength of selected hits and compare straight timing with a little swing.|Rap or hum over the loop. Remove hits that constantly interrupt your phrase endings.',
'A busy soloed beat can leave no space for the record’s main performance. Compose with the vocal role in mind.',
'Make two versions of an eight-bar groove: one with fewer notes, one with more. Record a rough vocal over both before choosing.',
'The groove supports a convincing performance rather than competing with it.','rhythm,drum,beat,pattern,swing,velocity,groove','v-patterns',
'What is a useful test for a drum pattern intended for a rap song?','Perform over it|Count plug-ins on the drum bus|Make every hat equally loud',0,'The pattern needs to work with the performance it is supporting.')

L('midi','create','Understand MIDI and instruments','A note instruction is not a recording of sound.','arrangement',
"MIDI describes musical events such as note, timing, velocity, and controller movement. A virtual instrument turns those instructions into audio. An audio recording stores the resulting waveform. This is why changing an instrument can transform a MIDI part without rerecording the notes.\n\nVelocity often changes both loudness and timbre, depending on the instrument. A note’s visible length and the sound’s release are different things: a short note can still ring after its note-off.",
'Create an instrument track and load a simple sound from the Browser.|Play or draw a short phrase, then vary one note’s velocity.|Open the note editor and change pitch, timing, and length separately so you hear their distinct effects.|Save the editable part and render an audio version only when you need portability or reduced processing load.',
'Exporting MIDI alone does not preserve a special synthesizer sound. Keep a rendered audio reference when that sound matters.',
'Use the same four notes with a piano-like sound, a soft pad, and a short pluck. Notice which note lengths need to change.',
'You can distinguish the performance data from the sound generator and the rendered audio.','midi,instrument,notes,keyboard,velocity,render','v-instruments',
'What does a MIDI file usually preserve?','Note and performance instructions|Every plug-in’s exact audio output|The microphone’s room reflections',0,'The instrument that interprets those instructions determines the resulting sound.')

L('harmony','create','Find a small harmonic world','You can write a song before learning every chord.','arrangement',
"A key gives a piece a tonal center, but songs can borrow notes and chords outside a simple scale. Begin by hearing where the music feels settled. A chord is a collection of pitches; an inversion changes which chord tone sits lowest without changing the basic note set.\n\nUse a small palette and explore rhythm, register, and voice leading. Moving one inner note can be more expressive than adding several new chords. Theory is a language for noticing relationships, not permission to make music.",
'Choose a simple instrument and find a tonal center by ear against the beat.|Build a short progression with two to four chords and listen for tension and return.|Move the same chords into different registers or inversions to reduce awkward leaps.|Sing a simple melody before adding extra layers, then verify that it fits the intended harmony.',
'An automatic key label is a suggestion to verify. A loop may be ambiguous, borrowed, or tuned away from standard pitch.',
'Write three melodies over the same progression using only a few notes. Change rhythm and contour more than complexity.',
'You can hear the home note and explain why a phrase feels resolved or unfinished.','harmony,key,chord,scale,inversion,melody,theory','toolbox',
'What changes when you invert a basic chord?','The ordering of its chord tones|Its sample rate|Every note automatically moves to a new key',0,'Inversions change voicing and bass position while preserving the basic chord-tone set.')

L('arrangement','create','Make the hook feel earned','Energy is more than loudness.','arrangement',
"Arrangement is the order and interaction of musical ideas. A hook can feel bigger because the verse withheld something: a double, a bass layer, a higher register, a wider texture, or a rhythmic accent. Turning up the master is rarely the most interesting contrast.\n\nThink in sections with clear jobs. The intro invites, the verse develops, the hook states, and a bridge or break changes perspective. Those are possibilities rather than a mandatory formula.",
'Mark the sections of your song and write each section’s role.|Identify the strongest hook feature and remove competing versions of it from earlier sections.|Create a transition with a small omission, fill, breath, or effect tail.|Listen from the end of the verse through the hook without stopping or soloing.',
'A hook that only works when auditioned by itself may not have enough contrast with the section before it.',
'Make a hook lift by changing only three arrangement elements while keeping the master fader fixed.',
'You feel a section change before looking at a marker or noticing a volume jump.','arrangement,hook,verse,bridge,transition,energy,section','toolbox',
'Which can make a hook feel larger without increasing the master level?','Adding a contrast that the verse intentionally withheld|Renaming the master channel|Duplicating the exact full mix',0,'The relationship between sections creates the lift.')

L('sampling','create','Turn a sound into an idea','Choose, trim, transform, and make room.','edit',
"A sample becomes useful through context. A small fragment can supply a rhythm, a texture, or a melodic seed. Trimming its start changes feel; envelope and filtering change its role; repitching changes both character and sometimes duration, depending on the playback mode.\n\nPractice with your own recordings or material you have permission to use. Keep a note of where each source came from so a promising sketch does not become confusing when it is time to release.",
'Record a short original sound: a spoken syllable, a tap, or a room texture.|Trim to the useful section and apply fades so playback is clean.|Load it into a sampler or arrange the audio directly, then make a simple rhythmic idea.|Change only one parameter at a time and save the version that inspires a performance.',
'Transformation alone does not establish permission to release someone else’s recording. Keep source provenance alongside the session.',
'Make a four-bar texture from your own voice without using the original words as a recognizable lead.',
'The sound has a specific role and its source is documented.','sample,sampling,chop,sampler,sampleone,texture','v-sample',
'What is a useful habit when collecting samples?','Keep a source and permission note|Assume a short clip has no owner|Discard the original source immediately',0,'Good provenance makes later decisions and collaboration much easier.')

L('references','create','Study a reference without chasing it','Translate admiration into decisions.','stereo',
"A useful reference answers a specific question. Is the lead close or distant? Are doubles audible or only felt? How much silence surrounds the drums? What changes when the hook arrives? These observations are more actionable than make it sound like this artist.\n\nMatch playback loudness before comparing. A mastered reference can easily seem better just because it is louder. Listen to one feature at a time and adapt the principle to your voice and arrangement.",
'Choose two references that share one quality you want, rather than one supposedly perfect target.|Lower the references to a comparable perceived loudness.|Write observations about vocal placement, low end, space, and section changes.|Try one related decision in your own song, then judge whether it serves your performance.',
'Exact settings from someone else’s session do not recreate their voice, room, recording, or arrangement.',
'Make a reference note with three observations and three original experiments for your own song.',
'You can describe a desired sonic quality without relying on an artist’s name.','reference,isaiah rashad,osquinn,idk,inspiration,style,unique','toolbox',
'Why level-match a reference before comparison?','Louder playback can bias the judgment|It changes the song’s key|It removes all mastering',0,'Comparable loudness makes tonal and arrangement differences easier to judge fairly.')

L('mix-review','finish','Review a mix without chasing your tail','Separate observations from fixes.','stereo',
"A useful review is a fresh listen with a short list. Write what you hear before touching controls. Group notes by priority: performance, arrangement, balance, tone, space, then polish. Solving a higher-level issue can eliminate several smaller ones.\n\nUse a consistent reference volume and more than one realistic playback context. A small speaker helps reveal midrange balance; headphones reveal detail; mono can expose cancellation. No single device is the final judge.",
'Export a rough mix and step away from the session.|Listen through once without stopping. Mark timestamps and plain-language problems.|Choose the three changes with the largest musical benefit and make only those.|Export a new version and compare against the old one at similar loudness.',
'Changing ten things at once makes it hard to know which move helped. Keep a previous version and a reason for each revision.',
'Run a three-note review on one song. Fix the notes, then stop and compare before creating more work.',
'Each revision has an audible purpose and the song becomes clearer rather than merely different.','review,revision,translation,reference,car test,headphones','toolbox',
'What is a useful review note?','At 0:42 the last word is buried under the snare|Needs more professional|Use more plug-ins',0,'A specific observation leads to a testable change.')

L('premaster','finish','Prepare a clean premaster','Give the next stage room to work.','export',
"A premaster is a finished mix prepared for mastering. Its job is to preserve your musical decisions while avoiding accidental overload or unnecessary delivery processing. There is no magic peak target that substitutes for a good mix.\n\nIf a limiter is only making a preview loud, export a version without that loudness stage. If bus processing is integral to the sound, keep it and communicate what it does. Preserve both an approved reference and the clean working export when useful.",
'Check the full arrangement, fades, and effect tails before export.|Inspect the Main path for clipping, accidental solo states, and preview-only processing.|Export a high-quality PCM file at the session sample rate, commonly 24-bit WAV, with no unrequested normalization.|Listen to the exported file from beginning to end and note its version and processing state.',
'Turning down the final fader does not undo distortion already created earlier in the signal chain.',
'Export a clean premaster and a louder reference from the same mix. Label both clearly so they cannot be confused.',
'The delivered file is complete, clean, and accurately labeled.','premaster,headroom,master,limiter,clean,wav','mixdown',
'What is more useful than chasing one exact premaster peak number?','A clean mix with intentional processing and clear delivery settings|Clipping every bus then lowering Main|Normalizing every stem separately',0,'A mastering workflow needs an intact mix and known processing, not an arbitrary meter ritual.')

L('loudness','finish','Understand loudness without worshiping a number','LUFS, peaks, and the feel of the record.','levels',
"Peak level describes the largest momentary excursions; loudness measurements describe aspects of perceived level over time. Integrated LUFS summarizes an entire program, while short-term measurements help you compare sections. True-peak estimation considers peaks that can occur between samples during reconstruction.\n\nStreaming normalization is playback behavior, not one universal mastering target. A dense mix and a sparse mix can share an integrated reading and still feel different. Preserve transients and emotional contrast instead of crushing the record to satisfy a screenshot.",
'Compare your mix and reference at similar perceived loudness.|Add final limiting gently if needed and listen to kick impact, bass sustain, consonants, and distortion.|Measure the complete exported file, not only the loudest loop.|Check the destination’s current delivery guidance when releasing; keep a high-quality master and a documented version.',
'An impressive loudness number can hide a smaller, flatter-sounding record. Turn the loud version down and compare again.',
'Create two limiting intensities and match their playback level. Choose by impact and clarity rather than which is loudest.',
'You can distinguish loudness from quality and identify when limiting costs too much.','lufs,loudness,true peak,mastering,limiter,normalization','v-master',
'If one master is louder, what should you do before deciding it sounds better?','Match perceived playback level|Increase its limiter again|Ignore the quiet version',0,'Level matching helps expose the musical tradeoff rather than rewarding simple gain.')

L('export','finish','Export the file you intended','Range, format, tails, and the final listen.','export',
"Export is part of production. The wrong range can cut off an intro or tail; a muted group can remove a part; a forgotten solo can turn a full mix into a stem. Name the intended deliverable before opening the dialog.\n\nIn Studio Pro, use Session > Export Mixdown for a finished mix. Choose the correct output and a range that includes the actual ending. Keep a lossless version for further work; make compressed copies when they suit the sharing destination.",
'Clear unintended solo and mute states and verify the Main output.|Set start and end deliberately, leaving time for reverb and delay to finish.|Choose stereo WAV and suitable resolution for your workflow, then give the file a versioned name.|Open the rendered file outside the DAW and check the first second, the loudest section, and the full ending.',
'A session that plays correctly does not prove the export settings are correct. Listen to the file you will actually use.',
'Export a 30-second excerpt with a long delay ending. Verify that the tail is intact and no extra silent minute follows it.',
'The delivered file begins, ends, and sounds exactly as intended.','export,bounce,mixdown,wav,mp3,tail,render','mixdown',
'What should you verify after rendering?','The actual exported file|Only the session screenshot|Only the filename extension',0,'The export is the deliverable, so it needs its own listening check.')

L('stems','finish','Make stems someone can actually use','Alignment and intent matter more than the ZIP name.','export',
"A multitrack export usually contains individual tracks; stems are often grouped elements such as drums, music, lead vocals, and backing vocals. People use the words differently, so label the contents clearly. Effects returns and shared bus processing can complicate reconstruction.\n\nExport every part over a common range. Note whether files are dry, processed, or include effects. If several files each include a shared reverb or nonlinear master processor, summing them may not reproduce the original mix exactly.",
'Choose the intended groups or individual tracks and use Studio Pro’s Export Stems dialog.|Inspect the Tracks and Channels choices and decide which outputs match the deliverable.|Use a shared start and ending range, with clear names and a reference mix.|Import the exported files into a fresh session at unity gain and check timing, missing parts, and effect balance.',
'A collection of independently normalized stems can destroy the original balance. Avoid normalization unless it is explicitly wanted.',
'Export lead, backing vocals, music, and effects from a small session, then rebuild a reference mix from those files.',
'The files line up automatically and their processing state is unambiguous.','stems,multitrack,collaborate,deliver,export,alignment','stems',
'Why include a stereo reference with stems?','It communicates the intended overall result|It replaces all source tracks|It guarantees every plug-in transfers',0,'The reference gives the recipient a concrete target for balance and intent.')

L('templates','advance','Build a template that saves attention','Keep useful defaults, not a museum of plug-ins.','signal',
"A good template removes repetitive setup while leaving the music open. For vocal work, that might mean a beat track, lead and double tracks, a vocal group, two effects returns, and clear colors. It should not start with a master chain that changes every decision before you understand it.\n\nTrack presets can carry repeatable setup; a full session template can preserve routing and structure. Treat saved settings as starting points. Input devices and available plug-ins can change between computers or sessions.",
'Build a small clean session with your usual roles and routing.|Keep recording paths simple and check that no high-latency mastering effects are active.|Save the template or track presets with descriptive names.|Open a new session from it and verify inputs, outputs, monitoring, and blank recording space.',
'A template can preserve a mistake as efficiently as a good decision. Test the version you actually save.',
'Time how long it takes to become ready to record before and after the template. Remove anything that does not save attention.',
'You can begin a clean recording quickly without hunting through unused tracks.','template,preset,workflow,setup,track preset','v-template,v-presets',
'What is a useful template goal?','Reduce repetitive setup while keeping decisions flexible|Load every owned plug-in|Force the same tone on every song',0,'The template should save attention, not make unearned creative decisions.')

L('shortcuts','advance','Get fast at the moves you repeat','Five remembered commands beat fifty forgotten ones.','edit',
"Speed comes from repetition on real work. Choose the actions that interrupt your flow most often: split, zoom, show the Console, show automation, and find a command. Learn those first rather than memorizing a huge cheat sheet.\n\nKey maps differ, and Mac function keys may require the Fn modifier depending on system settings. Studio Pro’s command search and keyboard-shortcut settings are useful when a tutorial’s shortcut does not match your setup.",
'Write down the five actions you use most often during one session.|Look up their commands in your installed key map and verify each on a disposable example.|Practice without the mouse where it actually saves time.|Consider a macro only after the exact sequence is already reliable and repetitive.',
'A macro that combines destructive actions too early can make an error faster. Keep a recoverable version and understand the commands inside it.',
'Edit eight bars using three chosen shortcuts. Repeat tomorrow until the actions feel automatic.',
'You stay focused on the performance because common navigation is no longer a search task.','shortcuts,macros,keyboard,find command,speed,zoom','v-find,v-macros,v-zoom',
'When is a macro most useful?','After a repeated command sequence is understood and reliable|Before you know what its steps do|Only when it has at least ten actions',0,'Automation is most useful when the underlying workflow is already sound.')

L('cpu','advance','Keep the session responsive','Spend processing where you can hear the benefit.','levels',
"CPU load depends on the whole signal path, not only the number of tracks. One expensive instrument or oversampled processor can be a bottleneck. During recording, responsiveness matters; during mixing, you can trade a larger buffer for stability.\n\nRendering or transforming a committed instrument can free resources, but preserve an editable version if you may change notes or sound design. Bypass and deactivate are not always equivalent in how much processing they release.",
'Open the performance view and identify the actual heavy instruments or effects.|Temporarily reduce unnecessary oversampling and other costly quality modes while tracking.|Raise the buffer during mixing or render a stable part after saving an editable version.|Before final export, restore any intentional quality settings and listen for differences.',
'Randomly disabling everything can change the sound without revealing the cause of the dropout. Isolate the load systematically.',
'Find the single biggest processing cost in a practice session and reduce it while preserving the audible result.',
'The session plays reliably and every printed part has a recoverable source.','cpu,dropout,crackle,freeze,render,buffer,performance','ua-latency,routing',
'What is a sensible first move when a session crackles under load?','Identify the actual bottleneck and review buffer/latency choices|Delete all source audio|Assume the interface is broken',0,'A focused diagnosis preserves the session and addresses the real cost.')

L('ear-practice','advance','Train the ears behind the tools','Build recognition through controlled comparisons.','eq',
"Critical listening improves when you change one thing and know what changed. First exaggerate a move enough to recognize its character; then reduce it to a useful amount. Return to the full mix before keeping it.\n\nFrequency recognition, compression timing, and spatial judgment are separate skills. Work on one for a few minutes at a time. Short fresh listening often teaches more than hours of fatigued tweaking.",
'Pick a familiar eight-bar passage and a single concept to study.|Create a clear contrast, such as a broad low-mid cut versus bypass, with matched playback level.|Describe the difference without using better or worse: thinner, softer front edge, farther away, more nasal.|Reduce the effect and try to identify it again before checking the control.',
'Loud, narrow frequency sweeps can be unpleasant and distort your judgment. Keep volume comfortable and use brief comparisons.',
'Spend ten minutes on one EQ region, then write a sentence predicting what that region will do on tomorrow’s session.',
'You can describe a change before seeing which setting is active.','ears,ear training,listening,practice,frequency,compression','toolbox',
'What makes a listening exercise easier to learn from?','Changing one variable at a time|Changing all plug-ins at once|Always choosing the louder version',0,'A controlled comparison connects the audible result to a specific cause.')

L('finish-habit','advance','Build the habit of finishing','Expertise is a trail of decisions you can explain.','export',
"Progress is not just watching more tutorials. It is applying a principle, hearing the result, and carrying the lesson into the next record. A small finished song gives you feedback across the entire process; an endlessly polished loop leaves many skills untouched.\n\nUse a repeatable cycle: make, review, identify one weakness, practice it, finish again. Keep your standards specific and your experiments limited enough that you can complete them.",
'Set one musical goal and one technical goal for the next session.|Choose the shortest workflow that gets you to a listenable export.|Keep a decision note describing the biggest improvement and the biggest remaining issue.|Schedule the next practice around that issue, using the relevant lesson instead of browsing aimlessly.',
'A progress counter records practice, not expertise. The real evidence is what you can hear and reliably do in a new song.',
'Finish a 60–90 second song study this week: recorded lead, deliberate arrangement, a clear mix, and an export you have checked.',
'You can finish another small record with fewer unexplained choices and more control over the result.','finish,practice,expert,habit,learning,artist,progress','toolbox',
'What best demonstrates learning?','Applying the idea successfully in a new session|Only collecting bookmarks|Watching at double speed without trying it',0,'Transfer to your own work is stronger evidence than passive completion.')

workflows=[]
def W(id,title,subtitle,symbol,time,steps,ids): workflows.append(dict(id=id,title=title,subtitle=subtitle,symbol=symbol,time=time,steps=steps.split('|'),lessonIDs=ids.split(',')))
W('record-session','Record a clean vocal','A calm setup for a take worth keeping.','mic','15–25 min',
'Save a new session in its own song folder. Name the beat and lead tracks.|Confirm Apollo is the audio device and the vocal track uses the correct mono input.|Choose one monitor path. If listening through Console, disable DAW input monitoring to avoid a duplicate.|Check what Console processing will print. Test the actual recorded file with playback inserts bypassed.|Rehearse your loudest line and set preamp gain with comfortable headroom.|Balance headphones so you can hear yourself without shouting against the beat.|Record a short test, then play it back to verify sound and timing.|Capture three purposeful takes, keep the alternatives, and save before editing.','audio-setup,apollo-monitor,gain,first-recording,takes')
W('throw-session','Make a vocal delay throw','Give one word a beautiful afterlife.','repeat','10–15 min',
'Choose a phrase ending with space before the next line.|Set a delay FX return fully wet and feed it from a vocal send.|Match the delay to the session tempo. Start with a quarter note and modest feedback.|Show the send-level automation and establish an off baseline before the phrase.|Raise the send only across the chosen word, then lower it again. Keep the return active for the tail.|Set automation to Read and replay from before the move.|Adjust the feed level, repeat tone, and feedback until the next lyric stays clear.|Save a version and compare with the dry phrase at the same lead level.','sends,delay-throw,automation,reverb')
W('mix-session','Mix a rap vocal','Clarity, intimacy, and space with a reason.','slider.horizontal.3','30–60 min',
'Choose the best performance and repair distracting edits.|Use event or clip gain to tame large outliers before compression.|Build a clear lead-to-beat balance with the faders.|Use corrective EQ only for problems you can describe. Keep vocal body intact.|Compress enough to control inconsistent peaks, then match bypass loudness.|De-ess only where sharp consonants need it. Check for a lisp.|Add a little color only if the vocal needs it; compare without it.|Blend a shared ambience and one or two deliberate throws.|Ride phrases against the beat and check the hook in mono.|Export a reference, take a break, and make a short review list.','comping,clip-gain,balance,eq,compression,deess,vocal-chain,delay-throw')
W('logic-session','Move a song from Logic','Keep timing and the sounds you care about.','arrow.left.arrow.right','20–40 min',
'Save an untouched copy of the original Logic project.|Write down sample rate, tempo, time signature, and any changes over time.|Choose a common start and end for all exports, including leading silence.|Export aligned WAVs and explicitly decide whether processing and automation are included.|Keep dry vocal alternatives and print important instruments or creative bus effects.|Export a stereo reference and label all files clearly.|Import the aligned files into a matching Studio Pro session at the same origin.|Compare the opening, a late entry, and the ending with the reference before making new edits.','logic-migration,stems,files')
W('comp-session','Build a convincing vocal comp','A strong performance with invisible repairs.','scissors','20–30 min',
'Listen to each full take and choose a strong emotional foundation.|Mark the few phrases that clearly need improvement.|Expand the layers and audition alternatives at those phrases.|Choose replacements with compatible tone, breath, and intention.|Check seams and add short fades or crossfades as needed.|Replay the whole section with the beat, without watching the edits.|Save a comp version while retaining the original layers.','takes,comping,fades,timing')
W('no-sound-session','Find the missing sound','Trace the route before touching random settings.','speaker.slash','5–10 min',
'Check the physical connection and whether the interface input meter moves.|Check the selected DAW audio device and session I/O mapping.|Confirm the track input matches the actual mic socket and that recording is armed when needed.|Confirm your chosen monitor route is audible; avoid enabling two routes as a fix.|Look for muted channels, unexpected solos, and a wrong output destination.|Check the Main meter, interface output, headphones, and their volume.|Record a short file and play it back to distinguish monitoring trouble from recording trouble.','signal,audio-setup,apollo-monitor')
W('hook-session','Make the hook lift','Create impact with arrangement and contrast.','sparkles','20–40 min',
'Define the hook’s emotional job in one sentence.|Choose a lead performance that communicates it clearly.|Record real doubles on the lines that need extra size.|Tighten distracting consonants without removing all variation.|Make room before the hook by withholding one texture or rhythmic element.|Add a supporting effect or wider background while keeping the lead centered.|Listen from the verse through the hook at a fixed master level.|Check mono and keep only the changes that strengthen the song.','doubles,performance,arrangement,stereo-mono,creative-fx')
W('premaster-session','Prepare a clean premaster','A complete, clearly labeled mix for the next stage.','waveform','15–25 min',
'Listen through the full mix and finish the arrangement, edits, and balances.|Check buses and Main for overloads or unintended solo/mute states.|Decide which bus processing is musical and which is preview loudness only.|Save a clean version while keeping the approved loud reference if useful.|Set the export range to include the intro and complete effect tail.|Export a lossless file at the session sample rate with intentional bit depth and no unrequested normalization.|Play the rendered file outside the DAW and label the version and processing state.','mix-review,premaster,loudness,export')
W('stems-session','Export usable stems','A package that opens in time and makes sense.','square.stack.3d.up','15–30 min',
'Decide whether you are exporting individual tracks or grouped stems.|Name each output by role and identify dry, processed, and effects-only files.|Select sources deliberately in Export Stems, including needed returns.|Use a common start and end for every file. Avoid independent normalization.|Include a stereo reference and notes about tempo, sample rate, and printed processing.|Import the results into a fresh session and verify timing and completeness.|Keep the original editable project and a separate backup of the delivery.','stems,export,files')
W('review-session','A focused mix review','Three useful changes, then a fresh listen.','ear','15–20 min',
'Export the current mix and take a short break.|Listen from beginning to end without adjusting controls.|Write timestamps and plain-language observations, not proposed plug-ins.|Compare a reference at similar playback loudness.|Choose only the three most important changes.|Make those changes, export a new version, and compare with the previous one.|Document the improvement and the next unanswered question in your notebook.','mix-review,references,ear-practice')
W('practice-session','Your 20-minute practice','A small experiment that becomes a real skill.','timer','20 min',
'Pick one problem in your own song and open the matching lesson.|Spend a few minutes understanding the principle and signal path.|Try one controlled change on a short passage.|Level-match before and after. Describe the result in concrete words.|Repeat at a smaller, musically useful amount.|Write what worked and mark the lesson practiced only after applying it.|Export the result or save a recoverable version, then stop.','ear-practice,finish-habit')

faqs=[]
def F(id,q,a,tags,ids): faqs.append(dict(id=id,question=q,answer=a,tags=tags.split(','),lessonIDs=ids.split(',')))
F('mic-silent','Why can’t I hear my microphone?','Follow the signal in order: physical mic and interface meter, selected DAW input, chosen monitor path, channel output, Main output, and headphones. If the interface meter moves but the DAW input does not, inspect device and input mapping. If the recording plays back but the live mic is silent, focus on monitoring. Open the no-sound session checklist for a guided pass.','silent,silence,sound,hear,microphone,mic,monitor,input','signal,audio-setup,apollo-monitor')
F('double-monitor','Why does my live voice sound doubled or phasey?','Check whether Apollo Console and the DAW’s input monitor are both audible. The slightly delayed copies can interfere. Choose one live monitor route, then record and replay a short test. A doubled sound only on playback may instead come from duplicate tracks, a stereo effect, or an edit.','double,doubled,phasey,echo,monitor,console','apollo-monitor,stereo-mono')
F('buffer','What buffer should I use for recording?','For DAW monitoring, try 64 or 128 samples and raise it if the session becomes unstable. Console monitoring reduces dependence on that round trip. During mixing, a larger buffer is usually fine. Plug-in latency also matters: a low buffer cannot undo a high-latency processor elsewhere in the live path.','buffer,latency,lag,late,1024,128,64,recording','latency,apollo-monitor,cpu')
F('crackle','Why does my audio crackle or drop out?','Separate overload distortion from processing dropouts. Check input and bus meters first. If the issue follows CPU load, try a larger buffer and identify the costly instrument or effect. If it exists in a clean captured file even at safe levels, inspect the source, cables, interface setup, and clock/sample-rate configuration.','crackle,dropout,click,pop,cpu,buffer','cpu,gain,latency')
F('clipping','Can lowering the vocal fader fix a clipped recording?','It lowers playback volume but cannot undo distortion already captured at the input. Reduce preamp gain and rerecord when possible. A restoration tool may help a salvage situation, but it cannot promise the original waveform. If clipping happens only later in a plug-in or bus, fix that stage instead.','clipping,clipped,distortion,red,preamp,gain','gain,cleanup')
F('dry-console','Does UAD MON mean my recording is completely dry?','For ordinary Console insert slots, MON monitors processing without printing those inserts to the DAW input. Unison processing is a separate upstream case and is committed. Record a short test and listen with DAW effects bypassed so you know what your exact routing is capturing.','uad,mon,rec,unison,console,dry,print','apollo-monitor')
F('spark-console','Can I put UAD Spark plug-ins in Apollo Console?','Native UADx/Spark plug-ins run in the DAW on the computer. Apollo Console uses compatible UAD-2 DSP versions. Owning one format does not mean every plug-in is available in the other. Choose the monitoring route first, then use the format that actually supports it.','spark,uadx,console,plugin,dsp,native','apollo-monitor,vocal-chain')
F('throw','How do I put a delay on just one word?','Use a delay on a fully wet FX return and automate the lead’s send level. Raise the feed over the target word and return it to off afterward. Keep the return active so the tail can finish. Match the note division to the groove and reduce feedback if repeats collide with the next line.','delay,throw,throws,word,last,echo,send','delay-throw,sends,automation')
F('dry-wet','What does automating dry/wet actually change?','It changes the blend inside that particular effect. On a vocal insert, that can replace some direct vocal with processed sound. A send-level move instead changes what feeds a separate return while the source stays on its normal path. Know which control your automation lane is attached to.','dry,wet,mix,automating,automation,blend','sends,automation,delay-throw')
F('tail-cut','Why does my delay tail cut off?','If you mute the return or bypass the delay, you can cut the sound already ringing inside it. For a throw, stop new input with the send and leave the return audible. Also check the export end range, gates, and whether another automation lane changes the return volume.','tail,cut,cutoff,delay,return,mute,export','delay-throw,export')
F('automation-read','Why does my fader snap back or ignore a manual change?','A Read automation curve can restore the stored value during playback. Inspect the parameter’s automation lane and edit the curve if the move should persist. If controls unexpectedly overwrite a curve, check for Touch, Latch, or Write and return to Read when the recording pass is finished.','fader,snap,back,automation,read,latch,write','automation')
F('highpass','Which Pro-Q shape is the high-pass filter?','Choose Low Cut. It reduces low frequencies while allowing higher ones through. Low Shelf is a different shape. Start with a low cutoff and a moderate slope, move upward slowly with the beat playing, and back off before the voice becomes thin.','pro,q,proq,high,pass,highpass,low,cut,filter,fabfilter','low-cut,eq')
F('mud','Why does my vocal sound muddy or boxy?','First check recording distance, room sound, and the vocal-to-beat balance. Listen for excessive low-mid buildup rather than cutting a fixed frequency by habit. A modest broad reduction may help; heavy low cutting can remove body while leaving boxiness. Compare in the full mix at matched loudness.','mud,muddy,boxy,muffled,lowmid,vocal','mic-technique,balance,eq,low-cut')
F('harsh','Why is my vocal harsh even after de-essing?','Identify whether the problem is sharp consonants, an aggressive vowel, distortion, or too much brightness across the whole voice. A de-esser mainly targets sibilance. Revisit the recording, EQ boosts, compression, and saturation. Treat the specific region or phrase instead of darkening every word.','harsh,sharp,piercing,sibilance,sss,deess','deess,eq,vocal-chain')
F('thin','Why did my vocal become thin after EQ?','You may have cut useful body with a high cutoff, broad low-mid removal, or several overlapping corrections. Bypass the chain in stages and compare at the same level. Restore weight until the vocal fits the beat, then keep only the cuts that solve an audible problem.','thin,body,eq,low,cut,weak','low-cut,eq,vocal-chain')
F('compressor','What compressor settings should I use on my vocal?','Choose settings by the result. Start with a moderate ratio and a threshold that controls louder words, then compare attack for consonant impact and release for natural recovery. Match output loudness to bypass. If one word drives extreme reduction, fix that outlier with clip gain first.','compressor,compression,settings,ratio,attack,release,threshold','compression,clip-gain')
F('chain','What order should my vocal plug-ins go in?','Start with a reason for each stage. Corrective EQ, compression, and de-essing where needed is a useful baseline; optional color comes only if it helps. Reverb and delay can use sends. Change order when the interaction gives you a clear reason, and avoid loading every bundle you own.','chain,order,plugins,fabfilter,izotope,soothe,landr,uad','vocal-chain')
F('tune-wrong','Why does Auto-Tune pull my voice to the wrong notes?','Verify the actual key, scale, input range, and intended melody. The beat’s label or automatic detection may be wrong or incomplete. Test a held note against the music. Faster correction makes a wrong target more obvious; it does not fix the target.','autotune,auto,tune,tuning,pitch,key,wrong,notes','tuning,harmony')
F('takes-layers','How do I keep several vocal takes without losing them?','Use Record Takes to Layers and test the behavior on a short range. Keep a strong full performance as your base, then comp only where another take improves it. Use separate tracks when the performances should sound together as doubles or ad-libs.','takes,layers,comp,comping,record,alternate','takes,comping,doubles')
F('logic-transfer','How do I bring my Logic session into Studio Pro?','Use aligned audio exports from a common start, plus a stereo reference. Match sample rate and document tempo. Print essential instrument sounds and creative processing while retaining dry options and the original Logic project. Plug-in states and routing are not guaranteed to transfer with a project file.','logic,migrate,migration,transfer,import,stems','logic-migration,stems')
F('no-edit','Why won’t my editing tool do what I expect?','Check what is selected, whether a layer or event is active, whether the track or event is locked, and which tool or modifier is currently assigned. Zoom in and try a simple edit on a duplicate. If following a Logic tutorial, do not assume its take-folder gestures map directly to Studio Pro layers.','edit,editing,scissors,fade,tool,locked,click','orientation,comping,fades,shortcuts')
F('copy-double','Can I duplicate my lead to make it wide?','Identical copies are not the same as independent doubles. Panning identical audio left and right can remain effectively centered; adding delay may create width with phase tradeoffs. Record new supporting performances when you want natural double texture, then check the mix in mono.','duplicate,copy,double,width,wide,stereo','doubles,stereo-mono')
F('reverb-mess','How do I stop reverb from swallowing the words?','Lower the send, shorten the decay, and adjust pre-delay while the full mix plays. Filter the return if it adds low-mid mud or sharpness. If you want a bigger tail in the gaps, try gentle sidechain ducking on the return. Keep the direct lead clear first.','reverb,mess,swallow,words,fog,wet,space','reverb,ducking,sends')
F('lufs-target','Do I have to master everything to −14 LUFS?','No single integrated loudness number is a universal artistic mastering target. Streaming normalization and delivery requirements differ. Match your reference’s playback level, then judge impact, clarity, distortion, and dynamics. Check the destination’s current requirements when you release.','lufs,14,loudness,master,mastering,target,streaming','loudness,premaster')
F('premaster-level','Does a premaster have to peak at exactly −6 dB?','No. A clean, unclipped mix with appropriate headroom and clear delivery instructions matters more than one exact peak. Preserve intentional musical bus processing and distinguish a preview loudness limiter from the mix’s sound. Do not create headroom by lowering only the final fader after upstream clipping.','premaster,6,db,headroom,peak,level','premaster,gain')
F('export-tail','Why is the ending missing from my export?','Check the export range and any tail option, then allow enough time after the last event for the actual effects to finish. Inspect unintended mute, solo, or automation states. Play the rendered file outside the DAW; the timeline alone does not prove the export is complete.','export,ending,missing,tail,bounce,cut,range','export,delay-throw')
F('missing-files','Why are my audio files missing when I reopen?','The session may reference media outside its folder. Locate the originals and relink them, then use the DAW’s media-management options to collect what the session needs. Keep a separate backup. Avoid reorganizing active source files in Finder without checking the session references.','missing,files,media,save,backup,reopen','files')
F('next-step','What should I learn next as a beginner?','Start with signal flow, audio setup, recording levels, and a clean first take. Then learn comping and editing, a fader balance, basic EQ and compression, and sends. Finish a short song study before adding complex processing. The Path view keeps this sequence organized while leaving every lesson available.','beginner,next,learn,start,learning,first,expert','orientation,first-recording,finish-habit')
F('beat-import','Why does my imported beat play at the wrong speed?','Check the file’s original tempo, the session tempo, and any automatic stretching or tempo-follow setting applied to the audio event. Compare against the original file outside the DAW. If it should stay at its existing speed, remove unintended time stretching before recording vocals over it.','beat,import,speed,slow,fast,tempo,stretch','first-recording,timing')
F('stock-plugins','Do I need more plug-ins to make a professional song?','Your existing tools are already more than enough for the core jobs. Recording, performance, arrangement, balance, and listening decisions usually provide the larger gains. Add a tool only when you can name a specific limitation and hear why the replacement helps.','stock,plugins,buy,professional,tools,landr,soothe','vocal-chain,balance,finish-habit')

glossary=[]
def G(term,meaning,example): glossary.append(dict(term=term,meaning=meaning,example=example))
G('Attack','How quickly a dynamics processor responds after the conditions for reduction are met.','A slower compressor attack may let more of a consonant’s front edge through.')
G('Automation','Stored changes to a parameter over the session timeline.','Raise a delay send over one word and lower it afterward.')
G('Aux / FX return','A channel carrying the processed output of a parallel effect path.','A fully wet reverb returns to the mix on its own channel.')
G('Bit depth','The precision used to represent sample amplitudes in a digital format.','24-bit recording offers useful working dynamic range; gain staging still matters.')
G('Bounce / render','Create an audio file from a live arrangement or processing path.','Print a synth part so another DAW can play the exact sound.')
G('Buffer','A block of audio processed by the computer at a time.','A smaller buffer can improve live responsiveness but increase processing pressure.')
G('Bus','A channel that combines and processes signals routed to it.','Send all backing vocals to a group bus for one overall level adjustment.')
G('Channel','An audio signal path in the mixer.','A virtual instrument can produce several channels from one track.')
G('Clip / event gain','Level adjustment associated with audio material before later channel processing.','Turn down one shouted word before it drives the compressor too hard.')
G('Clipping','An overload where a signal exceeds what a stage can represent or handle cleanly.','A red input meter can warn that you are recording a distorted peak.')
G('Comp','A performance assembled from selected parts of alternate takes.','Use take two for the first line and take three for the ending.')
G('Compressor','A processor that reduces dynamic level according to its detector and settings.','Control peaks so the lyric stays present without constant fader moves.')
G('Crossfade','An overlap where one piece fades out while the other fades in.','Hide a seam between two chosen vocal takes.')
G('dB','A logarithmic way to express a ratio, such as a change in level.','A fader move of −3 dB is a relative reduction, not a complete loudness description.')
G('dBFS','Digital level relative to full scale.','0 dBFS is the sample ceiling of a fixed-point file, not a recording target.')
G('Decay','How long a sound or reverberant response takes to die away.','A long reverb decay can fill the gap after a final lyric.')
G('De-esser','A processor that reduces excessive sibilant energy.','Control sharp S sounds while preserving the body of vowels.')
G('Dither','A small noise signal used when reducing quantization precision.','Apply it deliberately at a final bit-depth reduction, rather than repeatedly throughout a chain.')
G('Double','A separately performed supporting version of a part.','Record two new hook takes for natural left/right width.')
G('Dry / wet','Direct sound versus sound processed by an effect.','A parallel delay return is usually wet while the vocal channel carries the dry voice.')
G('Ducking','Reducing one signal in response to another.','Lower reverb while the singer speaks, then let it return in the gap.')
G('EQ','Equalization: altering the balance of frequency regions.','Reduce a low-mid buildup while keeping enough weight in the voice.')
G('Event','A piece of audio or musical material placed on the timeline.','Trim the end of a vocal event without deleting the entire track.')
G('Feedback','The amount of a delay’s output fed back into its input.','More feedback usually creates more repeats and can build into runaway sound at extreme settings.')
G('Formant','A resonance pattern that contributes to perceived vocal character.','A formant shift can make a voice seem smaller or larger without a corresponding melody change.')
G('Gain staging','Managing signal levels through each part of a chain.','Keep the preamp, plug-in inputs, buses, and output from accidental overload.')
G('Headroom','The available margin before a signal overloads a stage.','Leave space for a louder-than-rehearsed word during recording.')
G('High pass / low cut','A filter that reduces lower frequencies and passes higher ones.','In Pro-Q, use Low Cut to reduce unwanted rumble.')
G('Insert','An effect placed directly in a channel’s signal path.','A compressor insert changes the vocal before it reaches downstream stages.')
G('Latency','The time between an input event and the resulting output.','A performer can feel delayed headphones even when the recorded timing is otherwise handled correctly.')
G('Layer','An alternate set of material associated with a track.','Keep several lead takes on layers before comping.')
G('Limiter','A dynamics processor used to constrain output peaks strongly.','Catch final peaks carefully without flattening the kick or consonants.')
G('LUFS','A family of loudness measurements designed around perceived program level.','Integrated LUFS summarizes a whole track; it is not a score for musical quality.')
G('Masking','When one sound makes another harder to hear.','Keys in the vocal’s important midrange can obscure words even when both tracks are loud.')
G('MIDI','Musical event instructions rather than a recorded waveform.','A note message can trigger a piano or synth depending on the loaded instrument.')
G('Mono','A single audio channel or a combined single-channel presentation.','One ordinary microphone is normally recorded to a mono track.')
G('Normalization','An automatic level adjustment to a chosen measurement target.','Independently peak-normalizing every stem can change their intended balance.')
G('Oversampling','Processing internally at a higher rate to reduce certain digital artifacts.','Some saturation modes sound cleaner with oversampling but cost more CPU.')
G('Pan','Placement or balance across the stereo field.','Keep the lead centered and place supporting doubles toward the sides.')
G('Parallel processing','Blending a processed path with an additional signal path.','Mix a compressed duplicate underneath the main vocal for extra density.')
G('Phase','The position of a repeating waveform cycle relative to another or to time.','Combining delayed versions of the same sound can reinforce some frequencies and cancel others.')
G('Polarity','The positive/negative orientation of a signal.','Flipping polarity multiplies the waveform by −1; it does not fix every timing-related phase issue.')
G('Pre-delay','A gap before the reverberant response begins.','A short gap can keep the lead’s articulation distinct from its ambience.')
G('Pre-fader / post-fader','Whether a branch takes signal before or after the channel fader.','A post-fader effects send follows vocal level changes; a pre-fader send can remain independent.')
G('Premaster','A completed mix prepared for a later mastering stage.','Deliver a clean WAV and identify any intentional bus processing.')
G('Q','A measure related to the width or resonance of an EQ filter.','A higher-Q bell is narrower than a lower-Q bell in the same EQ.')
G('Quantize','Move musical events toward a timing grid according to chosen rules.','Use partial strength if full snapping makes the groove stiff.')
G('Ratio','How strongly a compressor controls level above its threshold region.','In an ideal 4:1 case, 4 dB above threshold becomes 1 dB above it.')
G('Release','How a dynamics processor recovers from gain reduction.','Too-fast recovery can sound jumpy; too-slow recovery may hold down the next phrase.')
G('Sample rate','The number of digital samples representing one second of audio.','48 kHz means 48,000 samples per second, not 48,000 notes.')
G('Saturation','A nonlinear change that can add harmonics and alter peaks.','A little can add density; too much can make a bright vocal brittle.')
G('Send','An additional feed from a channel to another destination.','Feed a little lead vocal into a shared delay return.')
G('Sidechain','A signal used to control or influence a processor’s behavior.','Use the dry voice as the compressor detector signal on a reverb return.')
G('Sibilance','Strong high-frequency consonant energy in speech or singing.','An S can feel too sharp even when the vowel before it sounds balanced.')
G('Stem','Usually a grouped audio export, though people also use the word for individual tracks.','Label a file Lead Vocals Wet so its role and processing are clear.')
G('Threshold','The level region at which a dynamics process starts acting.','Lowering it usually causes more of a vocal to trigger compression.')
G('Throw','An effect accent applied to a specific word or musical moment.','Let the final word echo while the rest of the verse stays comparatively dry.')
G('Track','A timeline container for a performance or other session data.','An instrument track holds notes that produce audio through an instrument channel.')
G('Transient','A brief front edge or sudden energy change in a sound.','The initial hit of a snare or the attack of a consonant.')
G('True peak','An estimate of peaks that may occur between stored samples after reconstruction.','A true-peak meter can reveal a risk that a sample-peak meter misses.')
G('Unison','Apollo’s integrated preamp and compatible plug-in technology.','A Unison insert is on the recording input path; MON is not a universal undo switch for it.')
G('Velocity','A MIDI performance value often mapped to intensity or tone.','A harder piano note may trigger a brighter sample, not just a louder one.')

sources=[]
def S(id,title,author,url,kind='manual'): sources.append(dict(id=id,title=title,author=author,url=url,kind=kind))
base='https://fenderstudiopromanual.fender.com/en/Content/'
S('toolbox','Studio Pro Toolbox tutorial library','Lukas Ruschitzka','https://s1toolbox.com/tutorials','library')
S('console','The Console','Fender Studio Pro manual',base+'Mixing_Topics/The_Console.htm')
S('audio','Audio tracks and recording inputs','Fender Studio Pro manual',base+'Recording_Topics/Audio_Tracks.htm')
S('routing','Effects signal routing','Fender Studio Pro manual',base+'Mixing_Topics/Effects_Signal_Routing.htm')
S('layers','Track layers','Fender Studio Pro manual',base+'Recording_Topics/Track_Layers.htm')
S('comping','Comping','Fender Studio Pro manual',base+'Editing_Topics/Comping.htm')
S('automation','Automation types','Fender Studio Pro manual',base+'Automation_Topics/Automation_Types.htm')
S('editing-automation','Editing automation curves','Fender Studio Pro manual',base+'Automation_Topics/Editing_Automation_Envelopes.htm')
S('automation-modes','Automation modes and controller behavior','Fender Studio Pro manual',base+'Control_Link_Topics/Automation_with_Hardware.htm')
S('clip-gain','Clips and clip-gain curves','Fender Studio Pro manual',base+'Editing_Topics/Clips_and_Clip_Gain_Curves.htm')
S('mixdown','Exporting a mixdown','Fender Studio Pro manual',base+'Mixing_Topics/Mixing_Down.htm')
S('stems','Export stems from your session','Fender Studio Pro manual',base+'Saving%2C%20Import%20and%20Export/Export_Stems_from_your_Session.htm')
S('proq-bands','Pro-Q band controls: Low Cut, Bell, and Shelf','FabFilter','https://www.fabfilter.com/help/pro-q/using/bandcontrols')
S('proq-mode','Pro-Q processing modes','FabFilter','https://www.fabfilter.com/help/pro-q/using/processingmode')
S('ua-inserts','Console inserts, UAD REC/MON, and Unison','Universal Audio','https://help.uaudio.com/hc/en-us/articles/25350369296660-UAD-Plug-In-Inserts')
S('ua-latency','Latency in DAW sessions','Universal Audio','https://help.uaudio.com/hc/en-us/articles/360050596812-Why-am-I-Getting-Latency-in-my-DAW-Sessions')
S('logic-export','Export tracks as audio files in Logic Pro','Apple','https://support.apple.com/en-ca/guide/logicpro/lgcpb27f70f9/10.7/mac/11.6.1')
for id,title,author,video in [
('v-find','Find Command: faster navigation','Lukas Ruschitzka','d8qSJolQ7hk'),
('v-macros','Working with the Macro Toolbar','Lukas Ruschitzka','IUPDvVelaHY'),
('v-fades','A workflow for fast fades','Marcus Huyskens','WW2SpZrPOxw'),
('v-presets','Create your own track presets','Lukas Ruschitzka','BNvHPBU4Kp4'),
('v-save','Save files and future-proof a session','Andrew Barr','k2bKlUdnXCc'),
('v-template','Using a session as a template','Lukas Ruschitzka','R8mJgjbTqqM'),
('v-zoom','Useful zoom shortcuts','Gregor Beyerle','QvnWPN91MbE'),
('v-instruments','Instrument tracks explained','Lukas Ruschitzka','w4IarxKp9lQ'),
('v-master','Master and release music in Studio Pro','Joe Gilder','njCaNxj2L9M'),
('v-patterns','Remix audio loops in Pattern mode','Gregor Beyerle','wHRbJyezTAg'),
('v-record','Record and comp vocals in Studio Pro','Joe Gilder','vNDe9dZ5FWQ'),
('v-layers','The Takes to Layers workflow','Joe Gilder','6eAYE9CosBE'),
('v-comp','A practical guide to audio comping','Joe Gilder','MdMRuxyqnEU'),
('v-align','Align vocals with the DAW’s own tools','Joe Gilder','WOKpOjATVqM'),
('v-tune','Vocal Tune in Studio Pro 8.1','Gregor Beyerle','K2xYpIfrbac'),
('v-throw','Add delay to one part of a vocal','Joe Gilder','ZSbv8rqXOmg'),
('v-reverb','Five reverb principles','Joe Gilder','VnCpRTsg_G8'),
('v-stock','Better vocals with stock effects','Joe Gilder','P4B8UjRwCNA'),
('v-creative','Explore creative vocal effects','Joe Gilder','Mhq-4fhIXyA'),
('v-sample','Turn your voice into a playable instrument','Joe Gilder','XM1f6GShds4'),
('v-duck','Ducking reverb and delay effects','Gregor Beyerle','o2mJNccbB98')]:
    S(id,title,author,'https://youtu.be/'+video,'video')

content=dict(chapters=[dict(zip(['id','title','subtitle','symbol'], c)) for c in chapters],lessons=lessons,workflows=workflows,faqs=faqs,glossary=sorted(glossary,key=lambda x:x['term'].lower()),sources=sources)
# One integrity check: broken IDs would silently remove navigation destinations.
for collection in ['chapters','lessons','workflows','faqs','sources']:
    ids=[x['id'] for x in content[collection]]
    assert len(ids)==len(set(ids)), f'duplicate {collection} ID'
lesson_ids={x['id'] for x in lessons}; source_ids={x['id'] for x in sources}; chapter_ids={x[0] for x in chapters}
for lesson in lessons:
    assert lesson['chapter'] in chapter_ids
    assert set(lesson['sources']) <= source_ids, lesson['id']
    assert 0 <= lesson['answer'] < len(lesson['options'])
    assert len(lesson['steps']) >= 4
for item in workflows+faqs: assert set(item['lessonIDs']) <= lesson_ids, item['id']
(root/'Stufo/curriculum.json').write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n')
print(f"Generated {len(lessons)} lessons, {len(workflows)} workflows, {len(faqs)} answers, {len(glossary)} glossary entries, {len(sources)} sources")
