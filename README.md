# Holy Spirit — Interactive Bible Study

A self-contained interactive reference app covering the Holy Spirit across the entire biblical canon. Built for a Friday morning Bible study group in Clemson, SC after 18 months of weekly study.

**Open `holy-spirit-study.html` in any browser. No server, no install, no login required.**

---

## What It Is

83 Spirit observations drawn from Genesis to Revelation, each tagged with ten theological characteristics and organized across five interactive tabs. Every passage card and scripture reference opens a deep dive modal with the ESV text, study commentary, theological reflection, and navigable cross-references.

The content comes from 18 months of real group study — teaching notes, leadership discussions, personal journals, and serious engagement with the biblical text. The tool exists to serve that content.

---

## The Five Tabs

### 1 — Characteristic Matrix
The complete reference table. Every observation laid out canonically with all ten characteristics mapped simultaneously as columns — Creator, Empowers, Guides, Reveals, Indwells, Convicts, Transforms, Unifies, Intercedes, Sovereign. Filter by testament, characteristic, or keyword. Toggle the Observations or Matrix columns independently to focus your reading.

### 2 — Chronological Timeline
Eight literary genres (Torah, History, Wisdom, Prophets, Gospels, Acts, Epistles, Apocalyptic) rendered side by side across the canon's arc. Each passage is a hoverable node with colored dots marking active characteristics. A frequency bar chart below shows OT vs NT distribution with a count/percentage toggle.

### 3 — By Lens
Four interpretive frames for the same 83 observations:
- **OT vs NT** — the theological shift from *ruach* to *pneuma*, with an eight-dimension contrast table
- **By Genre** — passages and dominant characteristics for each literary genre
- **By Characteristic** — one thread pulled through the full canon at a time, split by testament
- **Canon Map** — a density heatmap of all 66 books; click any book to expand its passages

### 4 — Practical Application
Nine questions the group returned to repeatedly, sequenced from the most foundational (*do I believe I am indwelt?*) to the most urgent (*what is at stake if the Spirit is absent?*). Each grounded in the passages studied, with clickable scripture references.

### 5 — Study Notes
Nine synthesized sections drawn from teaching notes, leadership discussions, and personal journals. The theological framework behind the data — what the Spirit is, why the distinctions matter, and how 18 months of study changed the way we read Scripture.

---

## Architecture

**Single file delivery** — the entire app ships as one `.html` file. React 18 is loaded via CDN; everything else is self-contained. Open by double-clicking. Works offline once loaded.

**Pre-compiled React** — JSX source is compiled with Babel CLI targeting Safari 12+ and injected into the HTML at build time. No Babel standalone runtime is used (it causes blank pages in Safari on large files).

**Design system** — dark parchment aesthetic built on two typefaces (Cormorant Garamond for body, DM Mono for metadata and labels), a restrained token set, and characteristic colors as the primary visual encoding throughout. Sphere animations on matrix rows are triggered by `IntersectionObserver` as they enter the viewport.

**Built with** — React 18, Babel CLI, vanilla CSS-in-JS, Python rebuild script, and iterative sessions with [Claude AI](https://claude.ai).

---

## Development

The JSX source lives separately from the compiled HTML. To make changes:

```
1. Edit    app.jsx                          ← source of truth
2. Compile ./node_modules/.bin/babel app.jsx -o app.compiled.js
3. Rebuild python3 rebuild.py              ← injects compiled JS into HTML
4. Output  holy-spirit-study.html
```

**Babel config** (`babel.config.json`):
```json
{
  "presets": [
    ["@babel/preset-env", { "targets": "Safari >= 12", "modules": false, "loose": true }],
    ["@babel/preset-react", { "runtime": "classic" }]
  ]
}
```

> **Note:** Do not use `type="text/babel"` in the HTML. Babel standalone cannot transpile files this large in Safari and will render a blank page.

---

## Content

The ten Spirit characteristics tracked across every passage:

| Characteristic | Description |
|---|---|
| Creator | Spirit as agent of creation and life |
| Empowers | Spirit enabling action, courage, skill |
| Guides | Spirit directing movement and decision |
| Reveals | Spirit disclosing truth and knowledge |
| Indwells | Spirit dwelling within a person |
| Convicts | Spirit bringing awareness of sin |
| Transforms | Spirit changing character from within |
| Unifies | Spirit binding community together |
| Intercedes | Spirit praying on behalf of believers |
| Sovereign | Spirit acting beyond human agency |

---

## Theological Frameworks Preserved

- *"The transformative is always miraculous, but the miraculous is not always transformative"*
- Christopher Wright's two extremes: God in a box ←→ sensational / emotional / unrestrained
- The freight engine / needle metaphor for Spirit through history
- *"OT writers often attributed the unexplainable to the sovereignty of God"*
- Realistic expectations: these are cumulative highlights across all of human history

---

## Status

Active development. Ongoing additions include:
- Additional verse deep dives
- Remaining ROWS gaps (Gal 4:6, Rom 5:5, 2 Cor 1:21-22, Acts 16:6-7)
- Global search across all tabs
- Previous / next navigation within the deep dive modal

---

*Friday Morning Bible Study · Clemson, SC · Holy Spirit series · 18 months*
