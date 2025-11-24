import requests

# === CONFIG ===
PAT_TOKEN = "MzI1NTE3NzM1MzI1OgoIeZvMVNlinUEw7WYPuhsUlWrA1"  # replace with your Personal Access Token
CONFLUENCE_BASE_URL = "https://luxproject.luxoft.com/confluence"  # your Confluence URL

# === ENDPOINT ===
url = f"{CONFLUENCE_BASE_URL}/rest/api/space?limit=25"

# === HEADERS ===
headers = {
    "Authorization": f"Bearer {PAT_TOKEN}",
    "Accept": "application/json"
}

# === REQUEST ===
try:
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        results = data.get("results", [])
        if not results:
            print("✅ PAT works, but no spaces available (empty list).")
        else:
            print("✅ PAT works, accessible spaces:")
            for space in results:
                print(f"- {space.get('name')} (key: {space.get('key')})")
    else:
        print(f"❌ Failed: HTTP {resp.status_code}")
        print(resp.text[:500])
except Exception as e:
    print("❌ Exception:", str(e))


###################################

from atlassian import Confluence

confluence = Confluence(
    url="https://luxproject.luxoft.com/confluence",
    token=PAT_TOKEN
)

try:
    spaces = confluence.get_all_spaces(limit=20)
    print("PAT OK, spaces:")
    for s in spaces.get("results", []):
        print(f"- {s['name']} (key: {s['key']})")
except Exception as e:
    print("ERROR:", e)
