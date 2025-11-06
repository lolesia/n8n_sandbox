from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://8b1aa2c1-b650-4e9f-b5ac-63c4f7120ab1.us-west-1-0.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.1FL1mA8zjvZuCBDzfJc5_HSxg1zcmvvMqpbg8YPpvcM",
)
collection = "github_commits"

# 1️⃣ Загружаем все points
scroll = qdrant_client.scroll(
    collection_name=collection,
    limit=1000,  # можно по 1000 за раз
    with_payload=True
)

points_to_delete = []

while scroll:
    points, next_page = scroll
    for point in points:
        if "branch" not in (point.payload or {}):
            points_to_delete.append(point.id)
    if not next_page:
        break
    scroll = qdrant_client.scroll(
        collection_name=collection,
        limit=1000,
        with_payload=True,
        offset=next_page
    )

# 2️⃣ Удаляем все без branch
if points_to_delete:
    qdrant_client.delete(collection_name=collection, points_selector=points_to_delete)
    print(f"✅ Deleted {len(points_to_delete)} points without 'branch' field.")
else:
    print("🎉 No points without 'branch' found.")
