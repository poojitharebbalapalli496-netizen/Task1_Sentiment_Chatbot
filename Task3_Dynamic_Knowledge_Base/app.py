import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from datetime import datetime

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="Dynamic Knowledge Base",
    page_icon="📚",
    layout="wide"
)


# ---------------- LOAD RESOURCES ----------------
@st.cache_resource
def load_resources():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="knowledge_base"
    )

    return model, collection


model, collection = load_resources()


# ---------------- ADD KNOWLEDGE ----------------
def add_knowledge(text, source):

    text = text.strip()
    source = source.strip()

    existing = collection.get(
        include=["documents", "metadatas"]
    )

    documents = existing.get("documents", [])
    metadatas = existing.get("metadatas", [])

    # Strong duplicate prevention
    for old_text, old_metadata in zip(
        documents, metadatas
    ):
        if (
            old_text.strip().lower() == text.lower()
            and old_metadata.get("source", "").strip().lower()
            == source.lower()
        ):
            return False

    document_id = "doc_" + datetime.now().strftime(
        "%Y%m%d%H%M%S%f"
    )

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[document_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"source": source}]
    )

    return True


# ---------------- SEARCH ----------------
def search_knowledge(query):

    if collection.count() == 0:
        return None

    embedding = model.encode(query).tolist()

    return collection.query(
        query_embeddings=[embedding],
        n_results=min(3, collection.count()),
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )


# ---------------- TITLE ----------------
st.title("📚 Dynamic Knowledge Base")

st.write(
    "Update knowledge dynamically and retrieve "
    "the latest relevant information."
)


# ---------------- STATISTICS ----------------
total_documents = collection.count()

if total_documents > 0:

    data = collection.get(
        include=["metadatas"]
    )

    sources = set(
        metadata["source"]
        for metadata in data["metadatas"]
    )

else:
    sources = set()


col1, col2 = st.columns(2)

col1.metric(
    "📄 Total Documents",
    total_documents
)

col2.metric(
    "🏷️ Sources",
    len(sources)
)


# ---------------- ADD NEW INFORMATION ----------------
st.header("➕ Add New Information")

information = st.text_area(
    "Information",
    placeholder="Enter new information..."
)

source = st.text_input(
    "Source / Category",
    placeholder="Example: company_information"
)

if st.button("Add Knowledge"):

    if not information.strip() or not source.strip():

        st.warning(
            "Please enter both information and source."
        )

    elif add_knowledge(
        information,
        source
    ):

        st.success(
            "Knowledge added successfully!"
        )

        st.rerun()

    else:

        st.warning(
            "This information already exists."
        )


# ---------------- SEARCH ----------------
st.header("🔎 Ask the Knowledge Base")

question = st.text_input(
    "Your Question",
    placeholder="Example: What is the return policy?"
)

if st.button("Search Knowledge"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        results = search_knowledge(question)

        if results:

            st.subheader(
                "📚 Retrieved Information"
            )

            for i in range(
                len(results["documents"][0])
            ):

                st.write(
                    f"### Result {i + 1}"
                )

                st.write(
                    results["documents"][0][i]
                )

                st.caption(
                    f"Source: "
                    f"{results['metadatas'][0][i]['source']} | "
                    f"Distance: "
                    f"{results['distances'][0][i]:.4f}"
                )

                st.divider()


# ---------------- VIEW KNOWLEDGE ----------------
st.header("📖 Knowledge Base")

all_data = collection.get(
    include=[
        "documents",
        "metadatas"
    ]
)

if all_data["ids"]:

    for i in range(
        len(all_data["ids"])
    ):

        with st.container(border=True):

            st.write(
                f"**ID:** {all_data['ids'][i]}"
            )

            st.write(
                all_data["documents"][i]
            )

            st.caption(
                "Source: "
                + all_data["metadatas"][i]["source"]
            )

else:

    st.info(
        "Knowledge base is empty."
    )


# ---------------- UPDATE ----------------
st.header("✏️ Update Knowledge")

if all_data["ids"]:

    selected_id = st.selectbox(
        "Select document to update",
        all_data["ids"],
        key="update_select"
    )

    index = all_data["ids"].index(
        selected_id
    )

    updated_text = st.text_area(
        "Updated Information",
        value=all_data["documents"][index],
        key="updated_text"
    )

    updated_source = st.text_input(
        "Updated Source",
        value=all_data["metadatas"][index]["source"],
        key="updated_source"
    )

    if st.button("Update Knowledge"):

        embedding = model.encode(
            updated_text
        ).tolist()

        collection.update(
            ids=[selected_id],
            documents=[updated_text],
            embeddings=[embedding],
            metadatas=[
                {"source": updated_source}
            ]
        )

        st.success(
            "Knowledge updated successfully!"
        )

        st.rerun()


# ---------------- DELETE ----------------
st.header("🗑️ Delete Knowledge")

if all_data["ids"]:

    delete_id = st.selectbox(
        "Select document to delete",
        all_data["ids"],
        key="delete_select"
    )

    if st.button("Delete Knowledge"):

        collection.delete(
            ids=[delete_id]
        )

        st.success(
            "Knowledge deleted successfully!"
        )

        st.rerun()