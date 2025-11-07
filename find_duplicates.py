import requests
import json
from collections import defaultdict
import hashlib


# === Настройки подключения ===
from qdrant_client import QdrantClient

client = QdrantClient(
    url="https://8b1aa2c1-b650-4e9f-b5ac-63c4f7120ab1.us-west-1-0.aws.cloud.qdrant.io", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.1FL1mA8zjvZuCBDzfJc5_HSxg1zcmvvMqpbg8YPpvcM",
)


def fetch_all_points(collection_name, batch_size=100):
    scroll_filter = None
    all_points = []

    while True:
        result, scroll_filter = client.scroll(
            collection_name=collection_name,
            scroll_filter=scroll_filter,
            limit=batch_size,
            with_payload=True,
            with_vectors=True,
        )
        if not result:
            break
        all_points.extend(result)
        if scroll_filter is None:
            break

    print(f"Fetched {len(all_points)} points total.")
    return all_points

points = fetch_all_points("github_commits")


# === 1. Загружаем все поинты ===
def fetch_all_points(limit=1000):
    url = f"{QDRANT_URL}/collections/{COLLECTION}/points/scroll"
    payload = {"limit": limit, "with_payload": True, "with_vector": False}
    points = []
    next_page = None

    while True:
        if next_page:
            payload["scroll"] = {"offset": next_page}
        r = requests.post(url, json=payload)
        r.raise_for_status()
        data = r.json()["result"]
        batch = data.get("points", [])
        if not batch:
            break
        points.extend(batch)
        next_page = data.get("next_page_offset")
        if not next_page:
            break
        print(f"Fetched {len(points)} points...")
    return points


def hash_point(p):
    # Хэшируем payload и вектор (округлив до 6 знаков, чтобы избежать шумов)
    vec_hash = hashlib.md5(json.dumps([round(x,6) for x in p.vector]).encode()).hexdigest()
    payload_hash = hashlib.md5(json.dumps(p.payload, sort_keys=True).encode()).hexdigest()
    return vec_hash + payload_hash

seen = {}
duplicates = []

for p in points:
    h = hash_point(p)
    if h in seen:
        duplicates.append((p.id, seen[h]))
    else:
        seen[h] = p.id

print(f"Found {len(duplicates)} duplicates.")
for dup in duplicates[:10]:
    print("Duplicate pair:", dup)
