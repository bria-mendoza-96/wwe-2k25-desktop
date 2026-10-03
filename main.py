"""Wwe 2k25 Desktop — Local Windows and macOS helper for Wwe 2k25 data paths, config and export caches, and export folders."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='wwe_2k25_desktop',
        description='Local Windows and macOS helper for Wwe 2k25 data paths, config and export caches, and export folders.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Wwe 2k25 Desktop')
    print('Find the Wwe 2k25 folder fast and keep a local spare.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
