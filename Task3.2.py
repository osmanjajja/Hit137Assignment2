import csv
from collections import Counter
from transformers import AutoTokenizer


def get_top_tokens(file_path, output_csv, model_name="bert-base-uncased", top_n=30):
    # Load the AutoTokenizer from the pre-trained model
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Tokenize the text using the tokenizer
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_count = Counter(tokens)

    # Get the top 'top_n' most common tokens
    top_tokens = token_count.most_common(top_n)

    # Write the top tokens and their counts into a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Token', 'Count'])  # Write header
        writer.writerows(top_tokens)  # Write the top tokens and their counts

    print(f"Top {top_n} tokens have been written to {output_csv}")


# File paths
input_text_file = 'extracted_text.txt'  # .txt file path
output_csv_file = 'top_30_tokens.csv'  # Output CSV file path

# Run the function
get_top_tokens(input_text_file, output_csv_file)
