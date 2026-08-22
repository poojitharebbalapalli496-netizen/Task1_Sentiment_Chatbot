import chromadb
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing database
client = chromadb.PersistentClient(path="./chroma_db")

# Get existing collection
collection = client.get_or_create_collection(
    name="knowledge_base"
)

# Delete all existing records
existing = collection.get()

if existing["ids"]:
    collection.delete(ids=existing["ids"])

print("Old knowledge cleared successfully!")

# Add clean knowledge
knowledge = [
    (
        "Our customer service is available 24 hours a day.",
        "company_information"
    ),
    (
        "Customers can return products within 30 days of purchase.",
        "return_policy"
    ),
    (
        "Standard delivery usually takes 3 to 5 business days. Express delivery is available within 1 to 2 business days.",
        "delivery_information"
    ),
    (
        "Premium members receive free standard shipping on all orders.",
        "membership_information"
    )
]

for i, (text, source) in enumerate(knowledge, start=1):

    doc_id = f"doc_{i}"

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"source": source}]
    )

    print(f"Added: {doc_id} - {source}")

print("\nClean database created successfully!")
print("Total documents:", collection.count())