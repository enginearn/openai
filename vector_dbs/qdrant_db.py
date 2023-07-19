#!/usr/bin/env python3

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrant_client.models import Filter, FieldCondition, Range
import numpy as np

# Create a client
client = QdrantClient(host="localhost", port=6333)

# Create a collection
client.recreate_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)

# Insert points
vectors = np.random.rand(100, 100)
client.upsert(
    collection_name="my_collection",
    points=[
        PointStruct(
            id=idx,
            vector=vector.tolist(),
            payload={"color": "red", "rand_number": idx % 10}
        )
        for idx, vector in enumerate(vectors)
    ]
)

# Search
query_vector = np.random.rand(100)
hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    limit=5  # Return 5 closest points
)

# Search with filter
hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    query_filter=Filter(
        must=[  # These conditions are required for search results
            FieldCondition(
                key='rand_number',  # Condition based on values of `rand_number` field.
                range=Range(
                    gte=3  # Select only those results where `rand_number` >= 3
                )
            )
        ]
    ),
    limit=5  # Return 5 closest points
)
