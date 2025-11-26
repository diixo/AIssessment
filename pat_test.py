#!/usr/bin/env python3
"""Quick sanity check that the Confluence PAT in auth.json works."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests


def load_confluence_auth() -> tuple[str, str]:
    auth_path = Path(__file__).resolve().parent / "auth.json"
    data = json.loads(auth_path.read_text(encoding="utf-8"))
    env = data["servers"]["confluence"]["env"]
    host = env.get("CONFLUENCE_HOST", "").strip()
    if not host:
        raise SystemExit("Missing CONFLUENCE_HOST in auth.json")
    if not host.startswith("http"):
        host = f"https://{host}"
    return host.rstrip("/"), env.get("CONFLUENCE_API_TOKEN", "").strip()


def main() -> int:
    host, token = load_confluence_auth()
    if not token:
        print("ERROR: Missing CONFLUENCE_API_TOKEN in auth.json")
        return 1

    url = f"{host}/rest/api/space?limit=20"
    try:
        resp = requests.get(
            url,
            headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
            timeout=10,
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        print("ERROR:", exc)
        return 1

    data = resp.json()
    results = data.get("results", [])
    if not results:
        print("PAT OK, but no spaces were returned (check permissions).")
        return 0

    print("PAT OK, spaces:")
    for space in results:
        name = space.get("name", "<unknown>")
        key = space.get("key", "?")
        print(f"- {name} (key: {key})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
