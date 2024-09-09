# Read the CSV file using pandas
df = pd.read_csv(file_path)

# Print the column names to check if 'TEXT' exists
print(f"Columns in {filename}: {df.columns}")

# Proceed if 'TEXT' column exists, otherwise raise a warning or check alternative column names
if text_column in df.columns:
    # Extract the text from the specified column
    text_data = df[text_column].dropna().tolist()
    all_text.extend(text_data)
else:
    print(f"Column '{text_column}' not found in {filename}")
