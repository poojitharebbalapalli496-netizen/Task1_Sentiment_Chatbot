import os
import xml.etree.ElementTree as ET


DATA_PATH = "data/MedQuAD"


def load_medquad():
    data = []

    for root_dir, _, files in os.walk(DATA_PATH):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(root_dir, file)

                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()

                    questions = root.findall(".//Question")
                    answers = root.findall(".//Answer")

                    for question, answer in zip(questions, answers):
                        q_text = question.text.strip() if question.text else ""
                        a_text = answer.text.strip() if answer.text else ""

                        if q_text and a_text:
                            data.append({
                                "question": q_text,
                                "answer": a_text
                            })

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return data


if __name__ == "__main__":
    records = load_medquad()

    print("Total Q&A pairs:", len(records))

    if records:
        print("\nSample Question:")
        print(records[0]["question"])

        print("\nSample Answer:")
        print(records[0]["answer"][:500])