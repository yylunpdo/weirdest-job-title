#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title to /output/entry.txt.

The title is a real-sounding senior role with one hilariously specific
twist: a person whose whole job is apologising on behalf of cars that
drive themselves -- and that keep cutting people off in traffic.
"""

import os

ENTRY = "Senior Apologizer for Self-Driving Cars"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
