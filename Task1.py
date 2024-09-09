# Importing required libraries
import os  # For file and directory handling
import pandas as pd  # For reading and manipulating CSV files

# Directory where your CSV files are located
csv_directory = r'D:\CDU-MsCyberSecurity\Semester2\HIT137-SoftwareNow\Hit137Assignment2'

# Name of the output text file that will store all the extracted text
output_file = 'extracted_text.txt'

# Column name containing the text in your CSV files (adjust if necessary)
text_column = 'TEXT'  # Ensure this matches the actual column name in your CSV files

# Initialize an empty list to store all extracted text from the CSV files
all_text = []

# Check if the directory exists before processing
if not os.path.exists(csv_directory):
    raise FileNotFoundError(f"The specified directory {
                            csv_directory} does not exist")

# Iterate over all the files in the specified directory
for filename in os.listdir(csv_directory):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        try:
            # Construct the full path to the CSV file
            file_path = os.path.join(csv_directory, filename)

            # Read the CSV file using pandas
            df = pd.read_csv(file_path)

            # Check if the specified column exists in the CSV
            if text_column not in df.columns:
                raise KeyError(
                    f"Column '{text_column}' not found in {filename}")

            # Extract the text from the specified column, drop any missing values, and convert to a list
            text_data = df[text_column].dropna().tolist()

            # Append the extracted text to the all_text list
            all_text.extend(text_data)

        except Exception as e:
            # Capture and print any error that occurs while processing individual CSV files
            print(f"Error processing file {filename}: {e}")

# Write all the extracted text into a single .txt file
if all_text:  # Proceed only if text has been extracted
    try:
        with open(os.path.join(csv_directory, output_file), 'w', encoding='utf-8') as f:
            # Join all text entries with a newline separator and write to the file
            f.write("\n".join(all_text))
        print(f"Text successfully extracted and saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")
else:
    print("No text extracted from the CSV files.")
