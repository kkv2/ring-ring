# Design language

Everything here comes from the hero banner, [`docs/assets/hero-20-ink.svg`](../assets/hero-20-ink.svg)
— a prepaid telephone card in deep navy, printed in ivory, with brass punch marks. That card is the
whole identity. When a screen needs a decision this document does not cover, the question to ask is
*what would be printed on the card?*

Machine-readable values live in [`tokens.css`](./tokens.css). This file explains them.

> **Why write this down.** The palette and the dial mark were designed for the README banner, but the
> operator console will need the same ones. Recovering them from an SVG later means guessing which
> hex was deliberate and which was a one-off.

---

## Palette

Eleven values, all taken directly from the banner. There are no others.

### Surfaces

| Token | Hex | Role |
|---|---|---|
| `--mm-desk-100` | `#E4E2DA` | Page ground, light theme. The desk the card sits on. |
| `--mm-desk-200` | `#D6D4C9` | Hairlines and dividers on `desk-100`. |
| `--mm-navy-700` | `#2E5480` | Raised navy surface; the card gradient's light end. |
| `--mm-navy-900` | `#16304E` | Deep navy surface; the card gradient's dark end. |
| `--mm-navy-950` | `#0E2136` | Punched (used) marks. The deepest value in the system. |
| `--mm-navy-100` | `#C8D7E8` | Pale tint for secondary labels on navy. Used once, at 90%, for the card's top line. |

### Ink

| Token | Hex | Role | Contrast |
|---|---|---|---|
| `--mm-paper-100` | `#F3EFE6` | Type printed on navy. | 11.7:1 on `navy-900` |
| `--mm-slate-900` | `#1C2430` | Headings on `desk-100`. | 12.0:1 |
| `--mm-slate-600` | `#585F68` | Body text on `desk-100`. | 5.0:1 |
| `--mm-slate-400` | `#767D86` | Meta and labels on `desk-100`. | **3.2:1** |

`slate-400` reaches only 3.2:1 and does not meet 4.5:1. In the banner it only ever sets 12–13px uppercase mono at wide
tracking, which is the one place it is legible enough. Use it for the same thing or not at all —
never for body copy.

### Accent

| Token | Hex | Role |
|---|---|---|
| `--mm-brass-500` | `#D2A94E` | The single accent. |

**Brass is a dark-ground colour.** It reaches 6.1:1 on `navy-900` and only **1.7:1** on `desk-100`.
On light surfaces it may be used as a graphic fill — a rule, a mark, a punch, a chart series — but
never as text and never as the only signal carrying meaning. When a light surface needs an accent
*for type*, the accent is `navy-700` (6.0:1 on `desk-100`).

Spend boldness in one place. Brass is it; everything else in the system is navy, slate or paper.

### Status — proposed, not from the banner

The banner has no notion of a call in progress, so these are extensions. Change them freely; they
are chosen to sit at the same low saturation as the rest.

| Token | Hex | Meaning |
|---|---|---|
| `--mm-status-live` | `#3E7D6A` | Call connected |
| `--mm-status-ringing` | `#D2A94E` | Ringing — reuses brass |
| `--mm-status-ended` | `#767D86` | Ended normally |
| `--mm-status-dropped` | `#B4503C` | Dropped, failed, escalated |

All four land between 3.2:1 and 3.9:1 on `desk-100` — they are fills, dots and stripes, not text.
Always pair them with a written state.

Status colour is separate from the accent. A brass button and a ringing badge must not be the same
component wearing different paint.

---

## The dial mark

[`dial.svg`](./dial.svg) — a rotary dial reduced to a ring, a hub and ten holes. It appears embossed
into the card face at 20–26% opacity, and it is the closest thing the project has to a logo.

It is drawn from a single radius `R`, so it holds at any size:

| Element | Value |
|---|---|
| Outer ring | `r = R`, stroke `0.068R`, no fill |
| Hub | `r = 0.21R` |
| Holes | ten, `r = 0.145R`, centres at `0.68R` |
| Hole angles | `-108° + i × 30°`, `i = 0…9` |

The file uses `currentColor` for both fill and stroke, so it recolours from CSS `color`. Do not add a
finger stop, do not add numbers, do not rotate it.

**Embossed, not stamped.** On the card it is the same colour as the surrounding ink at low opacity —
it reads as a pressed impression, not a printed logo. Keep that treatment when it appears large.
At small sizes (a favicon, an avatar, a nav mark) it may be solid.

---

## The telecard

The object itself, should a screen want to render one — an empty-state, a call summary, a share card.

| Property | Value |
|---|---|
| Aspect ratio | `1.585` (85.6 × 54 mm) |
| Corner radius | `16px` at 560px wide; scale with the card |
| Face | `linear-gradient(135deg, navy-700, navy-900)` |
| Shine | `linear-gradient(135deg, rgb(255 255 255 / .22), transparent 55%)` over the face |
| Shadow | offset `+4, +6`, `rgb(0 0 0 / .09)`, no blur |
| Tilt | `-2.2°` when the card is an object in a scene; `0°` when it is a UI element |

**Punch row.** Ten marks, `12 × 19`, `2px` radius, `27px` pitch, along the top left of the face. Used
units are `navy-950` at 90% opacity; remaining units are `brass-500` at 80%. This is the one detail
that makes the object read as a *phone* card rather than a credit card — if a card appears without
it, the reference is lost.

---

## Type

The banner uses the macOS system faces. No webfont has been chosen yet; when one is, it replaces the
first entry in each stack and nothing else changes.

| Role | Stack |
|---|---|
| Sans | `"Helvetica Neue", Helvetica, "Hiragino Sans", system-ui, sans-serif` |
| Mono | `Menlo, ui-monospace, "SF Mono", monospace` |

Tracking carries as much of the identity as the faces do:

- **Wordmark** — `-0.035em`, weight 700, always lowercase, always hyphenated: `moshi-moshi`.
  Never capitalised, never spaced out, never set in mono.
- **Uppercase mono labels** — `0.20em`. This is the card's voice: `AI VOICE FRONT DESK`,
  `105 UNITS`, `MOSHI MOSHI TELEPHONE CARD`.
- **Small mono meta rows** — `0.10em`.

Mono is for labels, identifiers, timers, phone numbers and units — anything that is data. Sans is for
anything that is language.

---

## Japanese

The chosen banner has none, deliberately. 「もしもし」 was carrying the reference by itself in earlier
drafts; with it gone, the card object does that work and the README's opening paragraph explains the
name in words.

In the product this reverses: **the service speaks Japanese only** (see the README's out-of-scope
note), so the console will be Japanese-first. When Japanese appears, set it in `Hiragino Sans`; the
banner set 「もしもし」 at `600` weight with `6–10px` letter-spacing, which is a good starting point
for headings.

---

## The banner

[`docs/assets/hero-20-ink.svg`](../assets/hero-20-ink.svg) — `1280 × 480`, rendered to PNG at 2×
(`2560 × 960`) for the README. The SVG is the source; regenerate the PNG from it rather than
editing the raster.

The composition, should it ever need rebuilding or resizing:

| | |
|---|---|
| Ground | `desk-100`, with `desk-200` hairlines every `8px` at 50% opacity |
| Card | `560 × 352` at `x 96, y 90`, tilted `-2.2°` about `380, 268` |
| Punch row | ten marks at `x 132, y 124`; three used |
| Rule | `y 176`, `brass-500` at 45%, from `x 132` to `x 620` |
| Dial | `r 74` centred `556, 352`, `brass-500` at 24%, placed clear of the wordmark |
| Wordmark | `56px`, weight 700, `-0.035em`, `paper-100`, baseline `y 300` |
| Card labels | `11px` `navy-100` at the top, `12.5px` `brass-500` under the wordmark — both mono, wide tracked |
| Right column | from `x 740` — tagline `38px` `slate-900`, description `18px` `slate-600`, rule, then a `12.5px` mono stack row in `slate-400` |

Three things carry the identity and must survive any redraw: **the punch row** (without it the
object is a credit card), **the embossed dial**, and **the wordmark in lowercase at tight
tracking**. Everything else is arrangement.

The banner contains no Japanese — see the section above.
