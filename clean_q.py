from qdrant_client import QdrantClient

# 🔗 Подключение к Qdrant Cloud
qdrant_client = QdrantClient(
    url="https://8b1aa2c1-b650-4e9f-b5ac-63c4f7120ab1.us-west-1-0.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.1FL1mA8zjvZuCBDzfJc5_HSxg1zcmvvMqpbg8YPpvcM",
)

collection_name = "github_commits"

# 🧹 Полная очистка коллекции
try:
    qdrant_client.delete(
        collection_name=collection_name,
        points_selector={"filter": {}}
    )
    print(f"✅ Все points из коллекции '{collection_name}' удалены.")
except Exception as e:
    print(f"❌ Ошибка при очистке коллекции: {e}")
