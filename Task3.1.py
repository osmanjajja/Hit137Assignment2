import csv
from collections import Counter
import re


def get_top_words(file_path, output_csv, top_n=30):
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert to lowercase for uniformity

    # Use regular expressions to extract words (removes punctuation and splits by spaces)
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrences of each word
    word_count = Counter(words)

    # Get the top 'top_n' most common words
    top_words = word_count.most_common(top_n)

    # Write the top words and their counts into a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Word', 'Count'])  # Write header
        writer.writerows(top_words)  # Write the top words and their counts

    print(f"Top {top_n} common words have been written to {output_csv}")


# File paths
# .txt file path
input_text_file = 'D:\CDU-MsCyberSecurity\Semester2\HIT137-SoftwareNow\Hit137Assignment2\combined_texts.txt'
output_csv_file = 'top_30_common_words.csv'  # Output CSV file path

# Run the function
get_top_words(input_text_file, output_csv_file)
