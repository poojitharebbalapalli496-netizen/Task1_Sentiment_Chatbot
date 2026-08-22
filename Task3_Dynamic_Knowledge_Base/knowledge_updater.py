import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="data/vector_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def add_information(text, source):

    existing = collection.get()

    if text in existing["documents"]:
        print("Information already exists. Skipping duplicate.")
        return

    embedding = model.encode(text).tolist()

    new_id = f"doc_{collection.count() + 1}"

    collection.add(
        ids=[new_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"source": source}]
    )

    print("Information added successfully!")
    print(f"ID: {new_id}")
    print(f"Text: {text}")
    print(f"Source: {source}")


if __name__ == "__main__":

    add_information(
        "Our customer service is available 24 hours a day.",
        "company_information"
    )

    add_information(
        "Customers can return products within 30 days of purchase.",
        "return_policy"
    )

    add_information(
        "Standard delivery usually takes 3 to 5 business days.",
        "delivery_information"
    )

    add_information(
        "Premium members receive free standard shipping on all orders.",
        "membership_information"
    )

    print(f"\nTotal documents: {collection.count()}")