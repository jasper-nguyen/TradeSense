import os
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_regression_tree_from_csv(input_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Loop through all CSV files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_directory, filename)
            try:
                # Read the cleaned CSV file into a DataFrame
                df = pd.read_csv(file_path, header=None)

                # Assume the last column is the target (y), and the rest are features (X)
                X = df.iloc[:, :-1]  # All columns except the last
                y = df.iloc[:, -1]   # The last column as the target

                # Split the data into training and testing sets
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Initialize and train the regression tree
                regressor = DecisionTreeRegressor(random_state=42)
                regressor.fit(X_train, y_train)

                # Evaluate the model (optional)
                y_pred = regressor.predict(X_test)
                mse = mean_squared_error(y_test, y_pred)
                print(f"Trained regression tree for {filename} with MSE: {mse:.4f}")

                # Save the trained model to the output directory as a .pkl file
                model_filename = os.path.join(output_directory, f"regression_tree_{filename.replace('.csv', '.pkl')}")
                with open(model_filename, 'wb') as model_file:
                    pickle.dump(regressor, model_file)
                print(f"Model saved to: {model_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
if __name__ == "__main__":
    input_directory = "Datasets/SOL/increasedSOLDf"  # Path to your cleaned CSV files
    output_directory = "Datasets/SOL/increasedSOLForest"  # Path to save the regression tree models
    train_regression_tree_from_csv(input_directory, output_directory)

    input_directory = "Datasets/SOL/decreasedSOLDf"  # Path to your cleaned CSV files
    output_directory = "Datasets/SOL/decreasedSOLForest"  # Path to save the regression tree models
    train_regression_tree_from_csv(input_directory, output_directory)

