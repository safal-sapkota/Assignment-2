#first install 
# pip install spacy scispacy transformers torch
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_ner_bc5cdr_md-0.5.1.tar.gz
from transformers import AutoTokenizer
from collections import Counter

def count_tokens(file_path, model_name='dmis-lab/biobert-v1.1'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = tokenizer.tokenize(text)
    return Counter(tokens)

def print_top_tokens(token_counts, top_n=30):
    print(f"Top {top_n} tokens:")
    for token, count in token_counts.most_common(top_n):
        print(f"{token}: {count}")

# Usage
input_file = 'combined_texts.txt'
token_counts = count_tokens(input_file)
print_top_tokens(token_counts)