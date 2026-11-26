#!/usr/bin/env python3
"""List and selectively clone catalog sources. Does not install or execute them."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent

def main():
    data = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['sectors', 'list', 'fetch'])
    parser.add_argument('--category', action='append', choices=list(data['sectors']))
    parser.add_argument('--repo', action='append', help='owner/repository; repeatable')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--include-archived', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--dest', type=Path, default=ROOT / 'tools')
    args = parser.parse_args()
    if args.command == 'sectors':
        for key, title in data['sectors'].items():
            print(f"{key:12} {sum(i['sector'] == key for i in data['items']):3}  {title}")
        return
    chosen = data['items']
    if args.repo:
        wanted = {v.casefold() for v in args.repo}
        unknown = wanted - {i['repo'].casefold() for i in chosen}
        if unknown:
            parser.error('Unknown repository: ' + ', '.join(sorted(unknown)))
        chosen = [i for i in chosen if i['repo'].casefold() in wanted]
    if args.category:
        chosen = [i for i in chosen if i['sector'] in args.category]
    if not args.include_archived:
        chosen = [i for i in chosen if not i['archived']]
    if args.command == 'list':
        for i in chosen:
            print(f"{i['repo']} | {i['output']} | {i['description']}")
        print(f'{len(chosen)} repositories')
        return
    if not (args.all or args.repo or args.category):
        parser.error('Choose --repo, --category, or --all')
    if not args.dry_run and not shutil.which('git'):
        parser.error('Git is required')
    failures = 0
    for i in chosen:
        target = args.dest.resolve() / i['repo'].lower().replace('/', '--')
        if target.exists():
            print(f'SKIP existing: {target}')
            continue
        print(f"{(i['url'] + '.git')} -> {target}")
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            result = subprocess.run(['git', 'clone', '--depth', '1', '--', (i['url'] + '.git'), str(target)], check=False)
            failures += result.returncode != 0
    print(f'{len(chosen)} selected; ' + ('dry run, no files written' if args.dry_run else f'{failures} failed'))
    if failures:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
