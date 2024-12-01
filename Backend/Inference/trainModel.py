import os
import pickle
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def process_csv_directory(input_dir, output_dir):
    """
    Processes a directory of CSV files, trains a decision tree on each, 
    and saves the trained models to the output directory.

    Parameters:
        input_dir (str): Path to the input directory containing CSV files.
        output_dir (str): Path to the output directory to save decision tree models.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            # Load the CSV file into a DataFrame
            file_path = os.path.join(input_dir, filename)
            df = pd.read_csv(file_path)

            # Ensure the DataFrame has at least two columns (features + target)
            if df.shape[1] < 2:
                print(f"Skipping {filename}: not enough columns for features and target.")
                continue

            # Assume the target variable is in the last column
            X = df.iloc[:, :-1]  # Features
            y = df.iloc[:, -1]   # Target variable

            # Train a DecisionTreeClassifier
            clf = DecisionTreeClassifier()
            clf.fit(X, y)

            # Save the trained model
            model_filename = os.path.splitext(filename)[0] + "_tree.pkl"
            model_path = os.path.join(output_dir, model_filename)
            with open(model_path, "wb") as model_file:
                pickle.dump(clf, model_file)
            print(f"Processed {filename} -> {model_filename}")

# Example usage
if __name__ == "__main__":
    input_directory = "increasedDF"  # Replace with path to DF
    output_directory = "increasedForest"  # Replace with path to Forest

    process_csv_directory(input_directory, output_directory)
