import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from collections import Counter
from nltk.corpus import stopwords
import nltk

# Download stopwords from NLTK (if not already downloaded)
nltk.download('stopwords')

# Get the list of English stopwords from NLTK
stop_words = set(stopwords.words('english'))

def filter_entities(entities):
    """Filter out stop words from extracted entities."""
    return [word for word in entities if word.lower() not in stop_words]

def process_in_chunks(text, chunk_size=1000000):
    """Process long texts in chunks to avoid memory issues."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def extract_entities_scispacy_chunks(chunks, model_name='en_ner_bc5cdr_md'):
    """Extract disease and drug entities from chunks using SciSpaCy model."""
    nlp = spacy.load(model_name)
    diseases = []
    drugs = []
    for chunk in chunks:
        doc = nlp(chunk)
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == 'DISEASE'])
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == 'CHEMICAL'])
    return filter_entities(diseases), filter_entities(drugs)

def extract_entities_medical_ner(text, chunk_size=512):
    tokenizer = AutoTokenizer.from_pretrained("Clinical-AI-Apollo/Medical-NER")
    model = AutoModelForTokenClassification.from_pretrained("Clinical-AI-Apollo/Medical-NER")
    
    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    
    def process_chunk(chunk):
        results = ner_pipeline(chunk)
        return results

    # Split text into chunks
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    all_entities = []
    for chunk in chunks:
        all_entities.extend(process_chunk(chunk))

    return all_entities

def categorize_medical_ner_entities(entities):
    categories = {
        'DISEASE': [],
        'SYMPTOM': [],
        'MEDICATION': [],
        'PROCEDURE': [],
        'OTHER': []
    }
    
    for entity in entities:
        if entity['entity_group'] in ['DISEASE_DISORDER']:
            categories['DISEASE'].append(entity['word'])
        elif entity['entity_group'] in ['SIGN_SYMPTOM']:
            categories['SYMPTOM'].append(entity['word'])
        elif entity['entity_group'] in ['MEDICATION']:
            categories['MEDICATION'].append(entity['word'])
        elif entity['entity_group'] in ['DIAGNOSTIC_PROCEDURE']:
            categories['PROCEDURE'].append(entity['word'])
        else:
            categories['OTHER'].append(entity['word'])
    
    return {k: filter_entities(v) for k, v in categories.items()}

def compare_models(text):
    print("Processing with ScispaCy and Medical NER...")
    chunks = process_in_chunks(text)
    
    scispacy_diseases, scispacy_drugs = extract_entities_scispacy_chunks(chunks)
    medical_ner_entities = extract_entities_medical_ner(text)
    medical_ner_categories = categorize_medical_ner_entities(medical_ner_entities)

    print("ScispaCy results:")
    print(f"Diseases: {len(scispacy_diseases)}, Drugs: {len(scispacy_drugs)}")
    
    print("\nMedical NER results:")
    for category, entities in medical_ner_categories.items():
        print(f"{category}: {len(entities)}")

    print("\nMost common diseases (ScispaCy):")
    print(Counter(scispacy_diseases).most_common(5))
    
    print("\nMost common drugs (ScispaCy):")
    print(Counter(scispacy_drugs).most_common(5))

    for category, entities in medical_ner_categories.items():
        print(f"\nMost common {category.lower()} (Medical NER):")
        print(Counter(entities).most_common(5))

# Usage
with open('combined_texts.txt', 'r', encoding='utf-8') as file:
    text = file.read()

compare_models(text)

