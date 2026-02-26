#!/usr/bin/env python3
import argparse, json, os


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def html_from_brief(b):
    title = b.get('project_name', 'Website Wireframe')
    sections = b.get('sections', ['Hero', 'Features', 'CTA'])
    cta = b.get('primary_cta', 'Get Started')
    blocks = []
    for s in sections:
        sid = s.lower().replace(' ', '-')
        blocks.append(f"<section id='{sid}' class='wf-section'><h2>{s}</h2><div class='wf-box'>Content block</div></section>")
    return f"""<!doctype html>
<html><head><meta charset='utf-8'><title>{title}</title>
<style>
body{{font-family:Arial,sans-serif;background:#f7f7f7;margin:0;padding:20px}}
.wf-wrap{{max-width:1100px;margin:0 auto}}
.wf-section{{background:#fff;border:1px solid #ddd;padding:20px;margin:14px 0}}
.wf-box{{height:90px;border:2px dashed #bbb;background:#fafafa;display:flex;align-items:center;justify-content:center;color:#666}}
button{{padding:10px 16px;border:1px solid #333;background:#fff;cursor:pointer}}
</style></head>
<body><div class='wf-wrap'><h1>{title}</h1>{''.join(blocks)}<section class='wf-section'><button>{cta}</button></section></div></body></html>"""


def figma_like_json(b):
    y = 0
    frames = []
    for s in b.get('sections', []):
        frames.append({'name': s, 'x': 0, 'y': y, 'width': 1200, 'height': 220, 'type': 'FRAME'})
        y += 240
    return {'document': {'name': b.get('project_name', 'Wireframe'), 'children': frames}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--brief', required=True)
    ap.add_argument('--outdir', required=True)
    args = ap.parse_args()

    b = load(args.brief)
    os.makedirs(args.outdir, exist_ok=True)

    html = html_from_brief(b)
    with open(os.path.join(args.outdir, 'wireframe.html'), 'w', encoding='utf-8') as f:
        f.write(html)

    with open(os.path.join(args.outdir, 'wireframe.figma.json'), 'w', encoding='utf-8') as f:
        json.dump(figma_like_json(b), f, indent=2)

    with open(os.path.join(args.outdir, 'summary.md'), 'w', encoding='utf-8') as f:
        f.write(f"# Wireframe Summary\n\nProject: {b.get('project_name')}\nSections: {', '.join(b.get('sections', []))}\n")

    print('Generated wireframe outputs')


if __name__ == '__main__':
    main()
