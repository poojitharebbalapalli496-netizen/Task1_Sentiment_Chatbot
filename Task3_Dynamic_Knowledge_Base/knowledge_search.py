import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to persistent ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Get knowledge collection
collection = client.get_or_create_collection(
    name="knowledge_base"
)

# User query
query = input("Enter your question: ")

# Convert query into embedding
query_embedding = model.encode(query).tolist()

# Search top 3 relevant results
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=min(3, collection.count()),
    include=["documents", "metadatas", "distances"]
)

print("\n===== SEARCH RESULTS =====")

for i in range(len(results["documents"][0])):
    print(f"\nResult {i + 1}")
    print("Information:", results["documents"][0][i])
    print("Source:", results["metadatas"][0][i]["source"])
    print("Distance:", round(results["distances"][0][i], 4))