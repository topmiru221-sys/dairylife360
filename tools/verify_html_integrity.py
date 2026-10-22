#!/usr/bin/env python3
"""Pre-merge single-file HTML structural gate. Requires Python 3 only.
Usage: python tools/verify_html_integrity.py index.html [baseline-index.html]
"""
import hashlib
import re
import sys
from pathlib import Path

def scan(filename):
    data = Path(filename).read_bytes()
    html = data.decode("utf-8-sig")
    scripts = len(re.findall(r"<script\b", html, re.I))
    closes = len(re.findall(r"</script\s*>", html, re.I))
    ids = re.findall(r"(?<![\w-])id\s*=\s*[\"']([^\"']+)[\"']", html, re.I)
    static_ids = [x for x in ids if "$" not in x]
    duplicates = sorted(set(x for x in static_ids if static_ids.count(x) > 1))
    tests = {
        "doctype": html.lstrip().lower().startswith("<!doctype html"),
        "html end": bool(re.search(r"</html>\s*$", html, re.I)),
        "script envelope": scripts == closes,
        "traditional Chinese": "zh-Hant" in html[:1500],
        "Niubao": "牛寶" in html,
        "uterine feature": all(x in html for x in ("dl1710", "PVD", "PMN")),
        "version title": bool(re.search(r"<title>[^<]*V18\.5\.17\.10", html, re.I)),
        "static id uniqueness": not duplicates,
    }
    print(filename, "bytes:", len(data), "sha256:", hashlib.sha256(data).hexdigest())
    print("scripts", scripts, closes, "IDs", len(static_ids), "duplicates", duplicates[:10])
    for name, ok in tests.items():
        print("PASS" if ok else "FAIL", name)
    return tests, set(static_ids)

if __name__ == "__main__":
    if not 2 <= len(sys.argv) <= 3:
        raise SystemExit("Usage: verify_html_integrity.py index.html [baseline-index.html]")
    tests, ids = scan(sys.argv[1])
    if len(sys.argv) == 3:
        _, original_ids = scan(sys.argv[2])
        missing = original_ids - ids
        tests["baseline ID preservation"] = not missing
        print("Missing baseline IDs:", len(missing), sorted(missing)[:20])
    if not all(tests.values()):
        raise SystemExit(1)
    print("Structural gate passed; JS behavior and browser QA still required.")
