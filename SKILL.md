---
name: automated-website-wireframing
description: Interpret client briefs, generate baseline wireframes as HTML/CSS sketches (and optional Figma-ready JSON export), then iterate layouts from structured feedback loops.
---

# Automated Website Wireframing

Creates fast first-pass website wireframes from brief data.

## Workflow
1. Parse client brief (audience, sections, goals, CTA)
2. Build page structure and low-fidelity components
3. Export:
   - HTML wireframe sketch
   - optional figma-like JSON layout
4. Apply feedback updates and regenerate

## Quick Start

```bash
python3 skills/automated-website-wireframing/scripts/generate_wireframe.py \
  --brief skills/automated-website-wireframing/references/sample-brief.json \
  --outdir ./out
```

Iterate with feedback:

```bash
python3 skills/automated-website-wireframing/scripts/iterate_wireframe.py \
  --brief skills/automated-website-wireframing/references/sample-brief.json \
  --feedback skills/automated-website-wireframing/references/sample-feedback.json \
  --outdir ./out-iterated
```

## Safety
- Generates drafts only
- No external publishing or deployment actions
