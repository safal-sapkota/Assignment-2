import os
import glob

# Get all CSV files in the current directory
csv_files = glob.glob('*.csv')

# Open the final output file in write mode
with open('combined_texts.txt', 'w') as output_file:
    for file_name in csv_files:
        with open(file_name, 'r') as file:
            # Read the content of the CSV file
            data = file.read().splitlines()  # split into lines

            # Extract and write the text data to the combined file
            for row in data:
                columns = row.split(',')
                if len(columns) > 2:  # assuming the 'text' is in the third column
                    output_file.write(columns[2] + '\n')
