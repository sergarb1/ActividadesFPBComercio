# Color Palette & Brand Style

**This is the single source of truth for all colors and brand-specific styles.** To customize diagrams for your own brand, edit this file — everything else in the skill is universal.

---

## Estilo del proyecto (ActividadesFPBComercio)

- Marca del site: **azul `#2563eb` + teal `#0f766e`** (variante clara `#4ecdc4`).
- Tipografía de las fichas: **Excalifont** → `fontFamily: 5` (así quedan igual que las imágenes ya publicadas).
- `roughness: 1` (estilo dibujado a mano) para que encaje con las láminas de las fichas.

---

## Shape Colors (Semantic)

Colors encode meaning, not decoration. Each semantic purpose has a fill/stroke pair.

| Semantic Purpose | Fill | Stroke |
|------------------|------|--------|
| Primary/Neutral | `#dbeafe` | `#2563eb` |
| Secondary | `#ccfbf1` | `#0f766e` |
| Tertiary | `#e0f2fe` | `#0369a1` |
| Start/Trigger | `#fed7aa` | `#c2410c` |
| End/Success | `#a7f3d0` | `#047857` |
| Warning/Reset | `#fee2e2` | `#dc2626` |
| Decision | `#fef3c7` | `#b45309` |
| AI/LLM | `#ddd6fe` | `#6d28d9` |
| Inactive/Disabled | `#f1f5f9` | `#475569` (use dashed stroke) |
| Error | `#fecaca` | `#b91c1c` |

**Rule**: Always pair a darker stroke with a lighter fill for contrast.

---

## Text Colors (Hierarchy)

Use color on free-floating text to create visual hierarchy without containers.

| Level | Color | Use For |
|-------|-------|---------|
| Title | `#2563eb` | Section headings, major labels |
| Subtitle | `#0f766e` | Subheadings, secondary labels |
| Body/Detail | `#64748b` | Descriptions, annotations, metadata |
| On light fills | `#374151` | Text inside light-colored shapes |
| On dark fills | `#ffffff` | Text inside dark-colored shapes |

---

## Evidence Artifact Colors

Used for code snippets, data examples, and other concrete evidence inside technical diagrams.

| Artifact | Background | Text Color |
|----------|-----------|------------|
| Code snippet | `#1e293b` | Syntax-colored (language-appropriate) |
| JSON/data example | `#1e293b` | `#22c55e` (green) |

---

## Default Stroke & Line Colors

| Element | Color |
|---------|-------|
| Arrows | Use the stroke color of the source element's semantic purpose |
| Structural lines (dividers, trees, timelines) | Primary stroke (`#2563eb`) or Slate (`#64748b`) |
| Marker dots (fill + stroke) | Primary fill (`#2563eb`) |

---

## Background

| Property | Value |
|----------|-------|
| Canvas background | `#ffffff` |
