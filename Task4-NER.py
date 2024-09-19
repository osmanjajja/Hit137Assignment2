import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Function to split text into smaller chunks


def split_text(text, max_length=100000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# Function to extract entities using SciSpaCy models


def extract_entities_spacy(text_chunks, nlp_model):
    diseases = []
    drugs = []
    for chunk in text_chunks:
        doc = nlp_model(chunk)
        for ent in doc.ents:
            if ent.label_ == "DISEASE":
                diseases.append(ent.text)
            elif ent.label_ == "CHEMICAL":
                drugs.append(ent.text)
    return diseases, drugs

# Function to extract entities using BioBERT


def extract_entities_biobert(text_chunks):
    tokenizer_biobert = AutoTokenizer.from_pretrained(
        "dmis-lab/biobert-base-cased-v1.1")
    model_biobert = AutoModelForTokenClassification.from_pretrained(
        "dmis-lab/biobert-base-cased-v1.1")
    nlp_biobert = pipeline("ner", model=model_biobert,
                           tokenizer=tokenizer_biobert, aggregation_strategy="simple")

    diseases = []
    drugs = []
    for chunk in text_chunks:
        ner_results = nlp_biobert(chunk)
        for ent in ner_results:
            if "disease" in ent["entity"].lower():
                diseases.append(ent["word"])
            elif "drug" in ent["entity"].lower():
                drugs.append(ent["word"])
    return diseases, drugs

# Function to compare two models' entity extractions


def compare_entities(entities_1, entities_2, label_1, label_2):
    print(f"Comparing {label_1} with {label_2}")
    common_entities = set(entities_1).intersection(set(entities_2))
    print(
        f"Common entities between {label_1} and {label_2}: {len(common_entities)}")
    print(f"Unique to {label_1}: {len(set(entities_1) - set(entities_2))}")
    print(f"Unique to {label_2}: {len(set(entities_2) - set(entities_1))}")


# Load SciSpaCy models
print("Loading SciSpaCy models...")
nlp_sci_sm = spacy.load("en_core_sci_sm")
nlp_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")

# Read the text file
print("Reading the text file...")
with open("combined_texts.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split the text into smaller chunks
text_chunks = split_text(text)

# Extract entities using SciSpaCy models
print("Extracting entities using en_core_sci_sm...")
diseases_sci_sm, drugs_sci_sm = extract_entities_spacy(text_chunks, nlp_sci_sm)
print("Extracting entities using en_ner_bc5cdr_md...")
diseases_bc5cdr_md, drugs_bc5cdr_md = extract_entities_spacy(
    text_chunks, nlp_bc5cdr_md)

# Extract entities using BioBERT
print("Extracting entities using BioBERT...")
diseases_biobert, drugs_biobert = extract_entities_biobert(text_chunks)

# Compare SciSpaCy models
compare_entities(diseases_sci_sm, drugs_sci_sm, diseases_bc5cdr_md,
                 drugs_bc5cdr_md, "en_core_sci_sm", "en_ner_bc5cdr_md")

# Compare SciSpaCy with BioBERT
compare_entities(diseases_bc5cdr_md, drugs_bc5cdr_md,
                 diseases_biobert, drugs_biobert, "en_ner_bc5cdr_md", "BioBERT")
