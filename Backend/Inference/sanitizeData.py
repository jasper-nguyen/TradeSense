import os
import pandas as pd

def clean_csv_files(input_directory, output_directory):
    # Ensure the input directory exists
    if not os.path.exists(input_directory):
        print(f"Error: Input directory '{input_directory}' does not exist.")
        return

    # Ensure the output directory exists, create if necessary
    os.makedirs(output_directory, exist_ok=True)

    # Loop through all CSV files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_directory, filename)

            # Read the CSV file, skipping the first row (labels)
            try:
                df = pd.read_csv(file_path, header=None)

                # Drop the first row (the first row of data, not the header)
                df = df.drop(index=0)

                # Remove the first column, the second-to-last column, and the last column
                df_cleaned = df.drop(columns=[0, df.shape[1] - 2, df.shape[1] - 1])

                # Save the cleaned DataFrame to the output directory
                output_file_path = os.path.join(output_directory, filename)
                try:
                    df_cleaned.to_csv(output_file_path, index=False, header=False)
                    print(f"Cleaned file saved: {output_file_path}")
                except Exception as e:
                    print(f"Error saving {filename}: {e}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Correcting the directory paths (removing any extra spaces)
    input_directory_increased = "Datasets/increasedCSV"  # Replace with your input directory
    output_directory_increased = "Datasets/increasedDf"  # Replace with your output directory
    clean_csv_files(input_directory_increased, output_directory_increased)

    input_directory_decreased = "Datasets/decreasedCSV"  # Replace with your input directory
    output_directory_decreased = "Datasets/decreasedDf"  # Replace with your output directory
    clean_csv_files(input_directory_decreased, output_directory_decreased)
