# Bible Study Library — Project Status

**Last updated:** June 1, 2026  
**Session:** 4.0 — Proverbs 31 · The Tongue · Suffering & Sovereignty · Character of God

-----

## 🌐 Live URL

```
https://ptander01.github.io/Holy-Spirit-Bible-Study/
```

GitHub repo: `https://github.com/Ptander01/Holy-Spirit-Bible-Study`

-----

## Confirmed File Structure (on GitHub — source of truth)

```
Holy-Spirit-Bible-Study/              ← repo root = site root
├── index.html                        ✅ Updated Session 4.0 — 21+ studies, 2 new standalones live, Women's track complete
│
├── first-principles/
│   ├── seeking-god.html              ✅ Complete — heart selector, 6 word studies, guide mode
│   ├── word-of-god.html              ✅ Complete — Psalm 119 explorer, guide mode
│   ├── discipleship.html             ✅ Complete — guide mode
│   ├── sin.html                      ✅ Complete — 6-passage sin reference, 55 definition cards, guide mode
│   ├── repentance.html               ✅ Complete — guide mode
│   ├── the-cross.html                ✅ Complete — 6 resurrection evidence cards, medical account, guide mode
│   ├── light-and-darkness.html       ✅ Complete — guide mode
│   ├── the-church.html               ✅ Complete — guide mode
│   ├── jesus-is-lord.html            ✅ Complete — guide mode
│   └── counting-the-cost.html        ✅ Complete — guide mode
│
├── core-four/
│   ├── core-four-gospel.html         ✅ Pillar 01 — blue #5a8ab0
│   ├── core-four-discipleship.html   ✅ Pillar 02 — green #6aaa6a
│   ├── core-four-community.html      ✅ Pillar 03 — amber #c4944a
│   └── core-four-disciplemaking.html ✅ Pillar 04 — purple #9a6ab0
│
├── standalone/
│   ├── lust.html                     ✅ Men's study — shame cycle, 5 tools, accountability Qs
│   ├── fasting.html                  ✅ Spiritual disciplines — 4 tabs, Isaiah 58, practices guide
│   ├── prayer.html                   ✅ Session 3.0 — 6 tabs, ACTS, Psalms, Unanswered, Lord's Prayer
│   ├── suffering-and-sovereignty.html ✅ NEW Session 4.0 — 6 tabs, pastoral + Reformed, Long Seasons
│   └── character-of-god.html         ✅ NEW Session 4.0 — 6 tabs, Jesus tab, Attributes, Grace tension
│
├── stage-of-life/
│   ├── marriage.html                 ✅ 6 tabs — Foundation, Roles, By Decade (accordion), Hard Conversations
│   ├── discipline-and-formation.html ✅ 5 tabs — Eli Warning, Patria Potestas, James 3:5, tongue/verbal
│   └── discipling-your-children.html ✅ 5 tabs — Shema, Deut 6, heritage/stewardship, Judges 2:10
│
├── womens/
│   ├── women-anxiety-and-fear.html   ✅ 6 tabs — The Lies, Women of Scripture, Phil 4
│   ├── women-identity-and-worth.html ✅ 6 tabs — Roles vs Identity, Who You Are in Christ, Imago Dei
│   ├── women-comparison-and-contentment.html ✅ 6 tabs — Anatomy, Learning Contentment, Envy & Celebration
│   ├── women-womanhood-and-calling.html ✅ 6 tabs — Women of Scripture, Titus 2, Discernment Framework
│   ├── women-proverbs-31.html        ✅ NEW Session 4.0 — 6 tabs, Acrostic poem, Who She Is, Misuse tab
│   └── women-the-tongue.html         ✅ NEW Session 4.0 — 6 tabs, Gossip Anatomy, James 3, Proverbs
│
├── listen/
│   ├── the-cross-listen.html         ✅ Audio player — 6 sections
│   ├── sin-listen.html               ✅ Audio player — 5 sections
│   ├── lust-listen.html              ✅ Audio player — 6 sections
│   ├── core-four-gospel-listen.html  ✅ Audio player — 4 sections
│   └── discipleship-listen.html      ✅ Audio player — 6 sections
│
└── resource-series/
    ├── WordOfGod_SeriesGuide_1.html  ✅ Week 1 + Week 2 (Teaching) live — Weeks 3&4 pending
    ├── holy-spirit-study_32.html     ✅ Pre-system React app
    └── ephesians_study_phase1-2.html ✅ Pre-system interactive guide
```

-----

## Session 4.0 — What Was Built

### New Files (4 total + updated index)

|File                                          |Tabs|Accent              |Notes                                                                         |
|----------------------------------------------|----|--------------------|--------------------------------------------- --------------------------------|
|`womens/women-proverbs-31.html`               |6   |`#a07080` rose-mauve|Acrostic display, Verse 30 as key, misuse tab, *eshet chayil* word study      |
|`womens/women-the-tongue.html`                |6   |`#a07080` rose-mauve|6-stage gossip anatomy, James 3 verse-by-verse, Proverbs organized by theme   |
|`standalone/suffering-and-sovereignty.html`   |6   |`#7a8aaa` slate-blue|Pastoral + Reformed, Long Seasons tab (illness/depression/disability), Witnesses|
|`standalone/character-of-god.html`            |6   |`#c4944a` amber-gold|8 Jesus scenes, 8 attribute cards, grace/consequence tension table            |

### Women's Track — Now Complete (6 studies)

1. Anxiety & Fear
2. Identity & Worth
3. Comparison & Contentment
4. Womanhood & Calling
5. **Proverbs 31** ← NEW
6. **The Tongue & Gossip** ← NEW

### Index Updates

- Resource Studies stat: 17+ → 21+
- Suffering & Sovereignty: moved from Planned → live standalone
- Character of God: moved from Planned → live standalone
- Proverbs 31 and The Tongue added to Women's Studies section
- Planned Studies now shows: Identity in Christ, Spiritual Warfare

-----

## Design System

### Tokens (defined inline in every file — core.css exists but not yet linked)

```css
--bg:           #0c0f18
--surface:      #13182a
--surface-2:    #1a2035
--accent:       per-study (see table below)
--cream:        #ede8dc
--cream-dim:    #a09a8e
--muted:        #5c6078
--border:       #232a42
--border-lt:    #2e3858
--font-display: 'Cinzel'
--font-serif:   'Cormorant Garamond'
--font-body:    'Lora'
```

### Per-Study Accent Colors (complete)

|Study                                   |Color                  |
|----------------------------------------|-----------------------|
|Seeking God (FP)                        |`#a89880` warm sand    |
|Word of God (FP)                        |`#c9a84c` gold         |
|Discipleship (FP)                       |`#4a8a8a` teal         |
|Sin (FP)                                |`#7a7a8a` slate        |
|Repentance (FP)                         |`#c47a30` amber        |
|The Cross (FP)                          |`#9a3a3a` crimson      |
|Light & Darkness (FP)                   |`#4a6a9a` cobalt       |
|The Church (FP)                         |`#5a8a5a` sage         |
|Jesus Is Lord (FP)                      |`#7a5a9a` violet       |
|Counting the Cost (FP)                  |`#b89a50` warm gold    |
|Gospel (Core Four)                      |`#5a8ab0` blue         |
|Discipleship (C4)                       |`#6aaa6a` green        |
|Community (Core Four)                   |`#c4944a` amber        |
|Disciplemaking (C4)                     |`#9a6ab0` purple       |
|Lust (standalone)                       |`#6b7a9a` slate        |
|Fasting (standalone)                    |`#6b8a5a` olive        |
|Prayer (standalone)                     |`#7a6aaa` indigo       |
|Suffering & Sovereignty (standalone)    |`#7a8aaa` slate-blue   |
|Character of God (standalone)           |`#c4944a` amber-gold   |
|Marriage (stage-of-life)                |`#9a7a5a` bronze       |
|Discipline & Formation (stage-of-life)  |`#b87355` terracotta   |
|Discipling Your Children (stage-of-life)|`#b87355` terracotta   |
|All Women's Studies                     |`#a07080` rose-mauve   |

-----

## Listen Mode

Built with a shared Python template generator (`/tmp/build_listen.py`).
Player features: voice selector (prefers Enhanced Siri), speed 0.8×–1.8×, section nav, ±15s, waveform, progress bar.

**Best experience:** Safari on iPhone with Enhanced Siri voice downloaded.

**Known limitation:** iOS won't play with screen locked — screen must stay on.

**Listen files built:** The Cross, Sin, Lust, Core Four Gospel, FP Discipleship  
**Still needed:** All remaining FP studies (7) + Core Four pillars (3) + Fasting + Prayer

-----

## Roadmap

### 🔴 Infrastructure (high priority)

1. **Link core.css** — replace inline `:root` blocks with `<link>`. One afternoon, massive long-term payoff.
1. **Print stylesheet** — `@media print` optimized for #24 lb textured cardstock.

### 🟡 Features

1. **Library search page** — `search.html` indexing passages, topics, word studies. Static, no server.
1. **localStorage note persistence** — reflection textareas save per-study per-device. ~10 lines JS per file.
1. **Listen mode — remaining studies** — Python generator ready; content work only.
1. **PWA** — `manifest.json` + `service-worker.js`. Installable from Safari, works offline.

### 🟢 Content Builds — Next Session Priority

1. **Word of God Weeks 3 & 4** — awaiting pastor's teaching notes
2. **Identity in Christ** — still in Planned Studies; natural next standalone
3. **Spiritual Warfare** — still in Planned Studies; men's track companion
4. **Sermon companion template** — reusable format for any series
5. **Listen mode** — Suffering, Character of God, Prayer are high-value candidates

### 🔵 Deployment

1. **Wix integration** — link from church website nav to GitHub Pages URL
1. **PWA** — after manifest + service worker, promote "Add to Home Screen"

### ⚪ Future / Migration

1. Holy Spirit study → current design system (5,176 lines React — significant lift)
1. Ephesians study → current design system (3,600 lines)
1. Spiritual Warfare standalone (men's track)

-----

## GitHub Upload Instructions — Session 4.0

Upload these files to GitHub:

```
index.html                                      ← REPLACE existing
standalone/suffering-and-sovereignty.html       ← NEW FILE
standalone/character-of-god.html                ← NEW FILE
womens/women-proverbs-31.html                   ← NEW FILE
womens/women-the-tongue.html                    ← NEW FILE
```

**How to upload:**

1. Go to repo → Add file → Upload files
2. Drag files into the upload area (GitHub preserves folder structure)
3. Commit with message: "Session 4.0 — Women's track complete + Suffering + Character of God"

-----

## How to Start Next Session

Paste this into a new chat:

> "Bible Study Library 5.0 — continuing development. Read the PROJECT_STATUS.md and ARCHITECTURE.md from the project files, then let's pick up the build queue."

The AI will read both docs and have full context in under 2 minutes.

-----

## Deployment Reference

**GitHub Pages:**  
Repo: `https://github.com/Ptander01/Holy-Spirit-Bible-Study`  
Live: `https://ptander01.github.io/Holy-Spirit-Bible-Study/`  
Deploy: push to `main` branch → auto-deploys in ~60 seconds

**core.css linking (when ready):**

```html
<!-- In first-principles/ files: -->
<link rel="stylesheet" href="../core.css">

<!-- In standalone/, stage-of-life/, womens/ files: -->
<link rel="stylesheet" href="../core.css">

<!-- In root-level files: -->
<link rel="stylesheet" href="core.css">
```
