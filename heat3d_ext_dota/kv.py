"""
Valve's KeyValues text, as Dota's scripts and localisation files are written:
`"key" "value"` pairs and `"key" { ... }` blocks, `//` comments, `#base`
lines and `[$CONDITION]` tags (ignored). A key that appears twice keeps its
first value, as the game reads most of these files.
"""

from __future__ import annotations

import re

_TOKEN = re.compile(r'"((?:[^"\\]|\\.)*)"|(\{)|(\})|//[^\n]*|(\[[^\]\n]*\])|(#base[^\n]*)|([^\s{}"\[]+)', re.S)


def parse(text: str) -> dict:
    """The file as nested dicts of strings."""
    text = text.lstrip("﻿")
    root: dict = {}
    stack = [root]
    key: str | None = None
    for m in _TOKEN.finditer(text):
        quoted, opened, closed, _cond, _base, bare = m.groups()
        if opened:
            child: dict = {}
            if key is not None:
                stack[-1].setdefault(key, child)
            stack.append(child if key is None or stack[-1].get(key) is child else {})
            key = None
        elif closed:
            if len(stack) > 1:
                stack.pop()
            key = None
        elif quoted is not None or bare is not None:
            word = quoted if quoted is not None else bare
            if key is None:
                key = word
            else:
                stack[-1].setdefault(key, word)
                key = None
    return root


def bases(text: str) -> list[str]:
    """The files a `#base` line names."""
    return re.findall(r'#base\s+"([^"]+)"', text)


def tokens(text: str) -> dict[str, str]:
    """A localisation file's `Tokens` block, keys lower case."""
    tree = parse(text)
    for top in tree.values():
        if isinstance(top, dict):
            found = top.get("Tokens") or top.get("tokens")
            if isinstance(found, dict):
                return {k.lower(): v for k, v in found.items() if isinstance(v, str)}
    return {}
