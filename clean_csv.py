import csv

def clean_csv(input_file, output_file, expected_columns=5):
    error_lines = []
    cleaned_lines = []

    with open(input_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Check for irregularities
            columns = line.split(',')
            if len(columns) != expected_columns:
                error_lines.append((line_number, len(columns), line.strip()))
            else:
                # Check for inconsistent quoting or special characters
                if any('"' in col and not col.startswith('"') and not col.endswith('"') for col in columns):
                    error_lines.append((line_number, len(columns), line.strip()))
                else:
                    cleaned_lines.append(line)

    # Write cleaned content to the new file
    with open(output_file, 'w') as clean_file:
        for line in cleaned_lines:
            clean_file.write(line)

    return error_lines, output_file

# Define the input and output file paths
input_file_path = '/Users/nehiljain/code/jaffle_shop_duckdb/seeds/raw_brewery_inventory.csv'
output_file_path = '/Users/nehiljain/code/jaffle_shop_duckdb/seeds/cleaned_raw_brewery_inventory.csv'

# Clean the CSV file and get error lines
errors, cleaned_file = clean_csv(input_file_path, output_file_path)

if errors:
    print("Irregularities found in the following lines:")
    for error in errors:
        print(f"Line {error[0]}: {error[2]}")
else:
    print(f"No irregularities found. Cleaned file saved to {cleaned_file}.")
