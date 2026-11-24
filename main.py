#!/usr/bin/env python3
"""Entry program for news-image-20261124.

Copies the bundled front-page image (entry.png, 1024x1024) to
/output/entry.png. Pure standard library, deterministic: every run
writes the exact same bytes, with no network, clock, or environment
dependence. Re-running overwrites the previous output with identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
