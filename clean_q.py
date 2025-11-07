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


payload_schema = {
        "status":"green",
        "optimizer_status":"ok",
        "indexed_vectors_count":0,
        "points_count":49,
        "segments_count":2,
        "config":{
            "params":{
                "vectors":{
                    "":{
                    "size":1536,
                    "distance":"Cosine",
                    "hnsw_config":{
                        "m":24,
                        "ef_construct":256,
                        "payload_m":24
                    },
                    "on_disk":false,
                    "datatype":"float32"
                    }
                },
                "shard_number":1,
                "replication_factor":1,
                "write_consistency_factor":1,
                "on_disk_payload":true,
                "sparse_vectors":{
                    
                }
            },
            "hnsw_config":{
                "m":16,
                "ef_construct":100,
                "full_scan_threshold":10000,
                "max_indexing_threads":0,
                "on_disk":false
            },
            "optimizer_config":{
                "deleted_threshold":0.2,
                "vacuum_min_vector_number":1000,
                "default_segment_number":0,
                "max_segment_size":null,
                "memmap_threshold":null,
                "indexing_threshold":10000,
                "flush_interval_sec":5,
                "max_optimization_threads":null
            },
            "wal_config":{
                "wal_capacity_mb":32,
                "wal_segments_ahead":0,
                "wal_retain_closed":1
            },
            "quantization_config":null,
            "strict_mode_config":{
                "enabled":true,
                "unindexed_filtering_retrieve":false,
                "unindexed_filtering_update":false
            }
        },
        "payload_schema":{
            "message":{
                "data_type":"keyword",
                "params":{
                    "type":"keyword"
                },
                "points":0
            },
            "file":{
                "data_type":"keyword",
                "params":{
                    "type":"keyword"
                },
                "points":0
            },
            "author_name":{
                "data_type":"keyword",
                "params":{
                    "type":"keyword"
                },
                "points":0
            },
            "time":{
                "data_type":"datetime",
                "params":{
                    "type":"datetime",
                    "is_principal":null
                },
                "points":0
            },
            "branch":{
                "data_type":"keyword",
                "params":{
                    "type":"keyword"
                },
                "points":0
            }
        }
        }