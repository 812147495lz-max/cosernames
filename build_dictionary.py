#!/usr/bin/env python3
"""Build a public, deduplicated English-column dictionary from the local CSV."""

import csv
import sys
from collections import OrderedDict


EXCLUDED_CREATORS = {"djawa", "韩国美女"}


def normalize(value):
    return " ".join((value or "").strip().split()).casefold()


def build(source, target):
    merged = OrderedDict()
    with open(source, encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            creator = (row.get("创作者") or "").strip()
            if not creator or normalize(creator) in EXCLUDED_CREATORS:
                continue
            aliases = [creator]
            aliases.extend((row.get("别名/变体") or "").replace(",", "/").split("/"))
            key = normalize(creator)
            entry = merged.setdefault(key, {"creator": creator, "aliases": []})
            seen = {normalize(item) for item in entry["aliases"]}
            for alias in aliases:
                alias = " ".join(alias.strip().split())
                if alias and normalize(alias) not in seen and normalize(alias) != key:
                    entry["aliases"].append(alias)
                    seen.add(normalize(alias))
    with open(target, "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["creator", "aliases"])
        writer.writeheader()
        writer.writerows(merged.values())
    return len(merged)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: build_dictionary.py SOURCE_CSV TARGET_CSV")
    print(f"entries={build(sys.argv[1], sys.argv[2])}")
