import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a medical text: ")

doc = nlp(text)

print("\nMedical Entities Found:\n")

for ent in doc.ents:
    print(f"Entity: {ent.text} | Type: {ent.label_}")