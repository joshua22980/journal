#!/usr/bin/env python3
"""Validate the assistant prompt without requiring network access."""

from pathlib import Path
from urllib.parse import urlparse
import re


ROOT = Path(__file__).resolve().parent.parent
PROMPT = (ROOT / "PROMPT.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")

REQUIRED_PROMPT_TEXT = (
    "10:00 AM",
    "12:30 PM",
    "2:30 PM",
    "4:35 PM",
    "MORNING_START",
    "CHECK_IN",
    "What are you working on right now, and are you stuck?",
    "15 or 30 minutes?",
    "[REPLACE WITH IANA TIME ZONE]",
    "Never fabricate results.",
)

missing = [text for text in REQUIRED_PROMPT_TEXT if text not in PROMPT]
assert not missing, f"PROMPT.md is missing required text: {missing}"

check_in = "What are you working on right now, and are you stuck?"
assert PROMPT.count(check_in) == 1, "The exact check-in question must occur once"

# Verify that documentation references are well-formed HTTPS links to the
# intended authoritative publishers. This is deterministic in restricted CI;
# checking whether remote servers are currently reachable is deliberately not.
links = re.findall(r"\[[^]]+\]\((https://[^)]+)\)", README)
allowed_hosts = {"www.nice.org.uk", "www.cochrane.org"}
assert links, "README.md must contain evidence links"
for link in links:
    parsed = urlparse(link)
    assert parsed.scheme == "https", f"Evidence link is not HTTPS: {link}"
    assert parsed.hostname in allowed_hosts, f"Unexpected evidence host: {link}"
    assert parsed.path and parsed.path != "/", f"Evidence link lacks a path: {link}"

print("Validated prompt contract and evidence-link structure.")
