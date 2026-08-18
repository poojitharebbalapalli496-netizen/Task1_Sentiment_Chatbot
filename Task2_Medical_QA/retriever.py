from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data_loader import load_medquad


class MedicalRetriever:
    def __init__(self):
        self.data = load_medquad()

        self.questions = [item["question"] for item in self.data]

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def search(self, query, top_k=3):
        query_vector = self.vectorizer.transform([query])

        similarities = cosine_similarity(
            query_vector,
            self.question_vectors
        ).flatten()

        best_indices = similarities.argsort()[-top_k:][::-1]

        results = []

        for index in best_indices:
            results.append({
                "question": self.data[index]["question"],
                "answer": self.data[index]["answer"],
                "score": float(similarities[index])
            })

        return results


if __name__ == "__main__":
    retriever = MedicalRetriever()

    query = input("Enter a medical question: ")

    results = retriever.search(query)

    print("\nTop matching results:\n")

    for result in results:
        print("Question:", result["question"])
        print("Similarity:", round(result["score"], 3))
        print("Answer:", result["answer"][:500])
        print("-" * 60)