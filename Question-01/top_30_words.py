from collections import Counter
import csv
import re

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        # Remove punctuation and split into words
        words = re.findall(r'\w+', text)
        return Counter(words)

def save_top_words(word_counts, output_file, top_n=30):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        for word, count in word_counts.most_common(top_n):
            writer.writerow([word, count])

# Usage
input_file = 'combined_texts.txt'
output_file = 'top_30_words.csv'

word_counts = count_words(input_file)
save_top_words(word_counts, output_file)

print(f"Top 30 words saved to {output_file}")