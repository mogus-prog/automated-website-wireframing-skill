#!/usr/bin/env python3
import argparse, json, os, copy
from generate_wireframe import html_from_brief, figma_like_json


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def apply_feedback(brief, fb):
    b = copy.deepcopy(brief)
    add = fb.get('add_sections', [])
    remove = set(fb.get('remove_sections', []))
    sections = [s for s in b.get('sections', []) if s not in remove]
    sections.extend([s for s in add if s not in sections])
    b['sections'] = sections
    if fb.get('primary_cta'):
        b['primary_cta'] = fb['primary_cta']
    return b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--brief', required=True)
    ap.add_argument('--feedback', required=True)
    ap.add_argument('--outdir', required=True)
    args = ap.parse_args()

    brief = load(args.brief)
    fb = load(args.feedback)
    b2 = apply_feedback(brief, fb)

    os.makedirs(args.outdir, exist_ok=True)
    with open(os.path.join(args.outdir, 'wireframe.html'), 'w', encoding='utf-8') as f:
        f.write(html_from_brief(b2))
    with open(os.path.join(args.outdir, 'wireframe.figma.json'), 'w', encoding='utf-8') as f:
        json.dump(figma_like_json(b2), f, indent=2)
    with open(os.path.join(args.outdir, 'applied-feedback.json'), 'w', encoding='utf-8') as f:
        json.dump(fb, f, indent=2)

    print('Generated iterated wireframe outputs')


if __name__ == '__main__':
    main()
