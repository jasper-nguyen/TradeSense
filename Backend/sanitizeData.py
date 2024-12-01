import os
import pandas as pd

def clean_csv_files(input_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Loop through all CSV files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_directory, filename)

            # Read the CSV file without a header
            df = pd.read_csv(file_path, header=None)

            # Drop the first column (index 0) and the last column (use -1 to get the last column's index)
            df_cleaned = df.drop(columns=[0, df.shape[1] - 1])

            # Save the cleaned DataFrame to the output directory
            output_file_path = os.path.join(output_directory, filename)
            df_cleaned.to_csv(output_file_path, index=False, header=False)
            print(f"Cleaned file saved: {output_file_path}")

# Example usage
input_directory = input("path/to/input_directory")  # Replace with your input directory
output_directory = input("path/to/output_directory")  # Replace with your output directory
clean_csv_files(input_directory, output_directory)
