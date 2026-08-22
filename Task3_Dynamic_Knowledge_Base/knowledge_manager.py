import chromadb

# Connect to persistent ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Get knowledge collection
collection = client.get_or_create_collection(
    name="knowledge_base"
)


def view_knowledge():
    total = collection.count()

    print("\n===== KNOWLEDGE BASE =====")
    print("Total documents:", total)

    if total == 0:
        print("Knowledge base is empty.")
        return

    results = collection.get(
        include=["documents", "metadatas"]
    )

    for i in range(len(results["ids"])):
        print(f"\nID: {results['ids'][i]}")
        print("Information:", results["documents"][i])
        print("Source:", results["metadatas"][i]["source"])


def update_knowledge(document_id, new_text, new_source):
    existing = collection.get(ids=[document_id])

    if not existing["ids"]:
        print("\nDocument not found.")
        return

    collection.update(
        ids=[document_id],
        documents=[new_text],
        metadatas=[{"source": new_source}]
    )

    print("\nKnowledge updated successfully!")


def delete_knowledge(document_id):
    existing = collection.get(ids=[document_id])

    if not existing["ids"]:
        print("\nDocument not found.")
        return

    collection.delete(ids=[document_id])

    print("\nKnowledge deleted successfully!")


# Display current knowledge
view_knowledge()
update_knowledge(
    "doc_4",
    "Standard delivery usually takes 3 to 5 business days. Express delivery is available within 1 to 2 business days.",
    "delivery_information"
)

view_knowledge()
delete_knowledge("doc_5")

view_knowledge()