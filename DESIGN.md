---
name: SpiritByte legal website
description: The Android app's Amber CRT identity adapted to readable Spanish legal documents.
colors:
  bg: "#0d0c0a"
  surface: "#1a1712"
  line: "#524226"
  text: "#f5d696"
  muted: "#b59a70"
  primary: "#ffb000"
  accent: "#ffd566"
typography:
  display:
    fontFamily: '"Geist Pixel", monospace'
    fontSize: "clamp(38px, 5vw, 68px)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  document-display:
    fontFamily: '"Geist Pixel", monospace'
    fontSize: "clamp(36px, 4.4vw, 60px)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  headline:
    fontFamily: '"Geist Pixel", monospace'
    fontSize: "28px"
    fontWeight: 400
    lineHeight: 1.2
  title:
    fontFamily: '"Geist Pixel", monospace'
    fontSize: "25px"
    fontWeight: 400
    lineHeight: 1.2
  body:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "17px"
    lineHeight: 1.75
  lead:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "19px"
    lineHeight: 1.7
rounded:
  code: "3px"
  control: "4px"
spacing:
  small: "12px"
  medium: "16px"
  mobile-gutter: "22px"
  control-gap: "24px"
  tablet-gutter: "28px"
  tablet-gap: "32px"
  desktop-gutter: "44px"
  desktop-gap: "64px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.bg}"
    rounded: "{rounded.control}"
    padding: "15px 22px"
  button-primary-hover:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.bg}"
  summary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    padding: "26px 28px"
  appearance-select:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    padding: "7px 28px 7px 10px"
  navigation:
    textColor: "{colors.muted}"
    padding: "10px 0"
---

# Design System: SpiritByte legal website

## Overview

**Creative North Star: "SpiritByte Amber CRT, adapted for reading"**

This site inherits the existing Android identity because the owner requested the same theme. The app's Amber CRT palette, actual fox logo and Geist Pixel Square headings remain the visual authority. This document records the implementation; it does not establish a replacement identity.

Long Spanish legal text uses system sans-serif, generous leading and a restrained document layout. Pixel type supplies recognition at headings and branding. Decorative CRT scanlines stay inside the fox panel, leaving the reading surface clear.

**Key Characteristics:**

- Inherited Amber CRT branding with four optional app-derived reading palettes.
- Flat, warm dark surfaces and thin separators.
- Pixel headings paired with readable system body text.
- Desktop contents beside the document; mobile contents within its flow.
- Local licensed assets and semantic static HTML.

Evidence: `styles.css` supplies the normative web tokens above. `site.js` defines optional palette selection and printing. Identity was compared with `D:/SpiritByte-Android/app/src/main/java/com/spiritbyte/android/SpiritTheme.kt` and the viewed `D:/SpiritByte-Android/docs/screenshots/apariencia.png`, which shows Amber CRT and Geist Pixel Square selected. `ASSETS.md` records the fox source, font source and licenses. This comparison makes no Google Play approval or publication claim.

## Colors

Amber CRT combines an almost-black warm background, brown panel edges and amber emphasis. Frontmatter records actual default CSS values.

### Primary

- **Amber phosphor** (`primary`): page headings, brand, main reading action and active navigation.

### Secondary

- **Soft amber** (`accent`): links, keyboard focus, main action hover and text actions.

### Neutral

- **Warm near-black** (`bg`): page background and main action text.
- **Brown-black panel** (`surface`): summary, inline code, selector and fox panel.
- **Dark amber border** (`line`): document rows, table cells, page divisions and controls.
- **Pale amber text** (`text`): body text and subordinate headings.
- **Muted amber text** (`muted`): supporting copy, metadata and inactive navigation.

The optional Green Phosphor, Synthwave 84, IBM Noir and Commodore 64 palettes swap these same seven roles without changing layout or typography. Their exact values remain in the `html[data-theme]` declarations in `styles.css`. Amber is the static default; JavaScript adds the selector and attempts to remember the preference locally.

The web muted role is lighter than Android's `dim` role in all five palettes: Amber (#b59a70 vs #a88c5c), Green (#8bc494 vs #68a874), Synthwave (#bba0dc vs #a882d2), Noir (#a0aebe vs #8290a0), Commodore (#aba7eb vs #8682d2). Synthwave's web primary (#ff69b4 vs #ff40a0) and Commodore's web body text (#d1ceff vs #bcb8ff) are also lighter. These are observed web reading adaptations, not exact token parity. The default Amber background, surface, border, body text, primary and accent match Android source.

**The Inheritance Rule.** Preserve the app's identifiable palette roles and assets; document reading adaptations explicitly instead of presenting them as Android values.

## Typography

**Display Font:** locally hosted Geist Pixel Square, exposed in CSS as `Geist Pixel`, with monospace fallback.

**Body Font:** system UI sans-serif with Apple, BlinkMacSystemFont and Segoe UI fallbacks.

Pixel headings preserve the app's terminal character. System body type handles long paragraphs, tables, metadata and navigation without carrying pixel texture through every line.

- **Display:** home heading at the frontmatter scale, with a pale-text second line. Tablet fixes the size to (50px), mobile to (48px).
- **Document display:** frontmatter scale with a maximum measure of (20ch); mobile (39px).
- **Headline:** general section heading; legal headings (26px), mobile (25px); summary headings (21px); contents headings (18px).
- **Title:** document row heading, mobile (24px).
- **Body:** frontmatter body scale, mobile (16px); legal body maximum (74ch).
- **Lead:** frontmatter lead scale, mobile (17px); general maximum (55ch), home maximum (43ch).
- **Labels:** metadata and selector (12px); main navigation (14px); footer supporting copy (13px).
- **Brand:** pixel wordmark (27px/1.15); supporting label (11px) with tracking (.04em); footer wordmark (20px).

**The Reading Rule.** Keep long legal prose in the observed system sans-serif stack; use Geist Pixel for identity and headings.

## Layout

The centered shell has a maximum width of (1240px), including desktop horizontal padding from the frontmatter. At (900px) and below, gutters and gaps tighten. At (640px) and below, it becomes a single-column reading flow with mobile gutters.

Home has a two-column hero (1.25fr / 1fr), followed by document rows, local-storage context, contact and footer. Mobile stacks the hero; its fox panel places a (110px) fox beside the short identity label. Document rows stack their action under the title and description.

Legal documents use a (240px) contents column and flexible reading column, separated by the desktop gap. Tablet contents use (190px) with the tablet gap. Contents remain sticky at (28px) from the viewport top until mobile, where they become static and their links use two columns. Legal body width is at most (74ch); sections have a (46px) top interval, reduced to (38px) on mobile. Anchors reserve (30px) scroll margin.

Desktop header minimum height is (116px); mobile branding and navigation stack. The three-column footer also stacks on mobile. Print styles provide white paper, dark ink, body text (11pt), document heading (28pt) and single-column legal content; interactive navigation and controls are hidden.

## Elevation & Depth

There are no box shadows. Depth comes from tonal panel contrast, thin borders and spacing. The fox panel alone adds stationary scanlines with a faint black stripe every (4px) and fine amber corner brackets. Text surfaces remain unobscured.

The fox enters once over (650ms) using `cubic-bezier(.16,1,.3,1)`, from (8px) below and opacity (.5). This only applies when reduced motion is not requested. Other interactions have immediate color and underline changes without transitions.

## Shapes

The form language is mostly rectangular with thin (1px) lines. Controls and summary use `rounded.control`; inline code uses `rounded.code`. The status indicator is a circular (6px) dot. Arrow icons use a single (1.5px) stroke at (22px). The actual fox image remains unaltered.

## Components

### Reading action

The filled amber link has a primary border, dark text, arrow and (24px) internal gap. Hover changes fill and border to accent. Mobile reduces padding to (14px 16px), text to (14px) and gap to (15px).

### Document rows

Full-width separated rows have pixel titles, muted descriptions and amber actions. Vertical padding is (28px), with thin top dividers; the last row also has a bottom divider. Hover underlines the title. Mobile stacks content and action with an (18px) gap and (26px) vertical padding.

### Summary and legal tables

The summary is a bordered surface panel with amber pixel heading and body text (16px). Mobile padding is (22px). Tables have collapsed thin borders, primary header text, surface header cells and system body type. Cell padding is (16px), reducing to (11px 10px) on mobile.

### Navigation and contents

Header navigation is muted at rest, amber and underlined on hover or current page. Contents links are muted (13px/1.5), becoming amber and underlined on hover; mobile size is (12px). Links, buttons and selects show an accent keyboard-focus outline (2px), offset (6px). The skip link appears on focus.

### Reading preference and print action

The native select has a surface fill and thin border, labeled `Paleta de lectura`. JavaScript adds it; it aligns right on desktop and left on mobile. The optional print button is a small underlined text action. Legal HTML and anchors remain usable without either enhancement.

### Fox panel

The decorative panel reuses the actual fox, muted pixel identity line, corner brackets and stationary scanlines. It is not behind legal text. The header uses the fox at (46px), with empty alternative text because the adjacent brand names the destination.

## Do's and Don'ts

### Do:

- **Do** preserve the app's fox, local Geist Pixel asset and default Amber CRT identity.
- **Do** retain system sans-serif body text, generous leading and established reading measure.
- **Do** keep legal content and anchors present in static HTML.
- **Do** preserve visible focus, reduced-motion behavior and print styles.
- **Do** record web palette adaptations when comparing with Android.

### Don't:

- **Don't** replace the inherited visual world during documentation or routine page additions.
- **Don't** place CRT scanlines over legal text.
- **Don't** describe adapted web tokens as exact Android matches.
- **Don't** require palette-selection JavaScript to access legal documents.
