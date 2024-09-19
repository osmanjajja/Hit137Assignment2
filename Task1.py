import os
import pandas as pd


def extract_texts_from_csv(directory, output_file_name='combined_texts.txt'):

    possible_columns = ['TEXT',
                        'SHORT-TEXT']  # List of possible column names
    try:
        # Open a text file for writing all extracted texts
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            # Loop through all the files in the directory
            for filename in os.listdir(directory):
                # Process only CSV files
                if filename.endswith('.csv'):
                    file_path = os.path.join(directory, filename)
                    try:
                        # Load the CSV file using pandas
                        df = pd.read_csv(file_path)

                        # Check for possible column names in each CSV file
                        text_column = None
                        for col in possible_columns:
                            if col in df.columns:
                                text_column = col
                                break

                        if text_column:
                            # Write each 'text' entry to the output file
                            for text in df[text_column]:
                                output_file.write(str(text) + '\n')
                        else:
                            print(
                                f"Warning: None of the expected text columns found in {filename}. Skipping file.")
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

        print(
            f"Text extraction completed. Combined texts saved to '{output_file_name}'.")

    except Exception as e:
        print(f"An error occurred while creating the output file: {e}")


# Path to the directory containing the CSV files
csv_directory = 'D:/CDU-MsCyberSecurity/Semester2/HIT137-SoftwareNow/Hit137Assignment2'

# Call the function to extract texts from the CSV files
extract_texts_from_csv(csv_directory)
