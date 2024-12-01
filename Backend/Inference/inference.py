import os
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor


class InferenceModel:
    def __init__(self, increased_path, decreased_path, current_model=None):
        """
        Initializes the InferenceModel class.

        Args:
            increased_path (str): Directory containing decision trees for the "increased" scenario.
            decreased_path (str): Directory containing decision trees for the "decreased" scenario.
            current_model (sklearn model): A single decision tree model to be evaluated.
        """
        self.increased_path = increased_path
        self.decreased_path = decreased_path
        self.current_model = current_model

        # Debugging: Print the type of the provided model
        print(f"Provided model type: {type(self.current_model)}")

        # Ensure the model is a valid decision tree classifier or regressor
        if not isinstance(self.current_model, (DecisionTreeClassifier, DecisionTreeRegressor)):
            raise ValueError("The provided model is not a valid decision tree model.")

    def evaluate_model(self, clf, features, target_column=None):
        """
        Evaluates a single model (current_model) by comparing it to other models in terms of prediction confidence.
        """
        if isinstance(clf, DecisionTreeClassifier):
            confidences = clf.predict_proba(features).max(axis=1)  # Maximum probability for classification
            average_confidence = confidences.mean()
        else:
            predictions = clf.predict(features)
            if target_column is not None:
                residuals = abs(predictions - target_column)  # Calculate residuals for regression
                average_confidence = residuals.mean()
            else:
                average_confidence = predictions.mean()  # If no target column, fallback to mean prediction confidence

        return average_confidence

    def evaluate_models(self, treesPath, features, target_column=None):
        """
        Evaluates models in the given directory by comparing their prediction confidence.
        """
        scores = []

        for filename in os.listdir(treesPath):
            if filename.endswith(".pkl"):
                model_path = os.path.join(treesPath, filename)
                try:
                    with open(model_path, "rb") as model_file:
                        clf = pickle.load(model_file)

                    # Check if the model is a classifier or regressor
                    if isinstance(clf, (DecisionTreeClassifier, DecisionTreeRegressor)):
                        # Perform the evaluation (either classification or regression)
                        model_confidence = self.evaluate_model(clf, features, target_column)
                    else:
                        print(f"Skipping {filename}: Not a valid decision tree model.")
                        continue

                    scores.append((filename, model_confidence))
                    print(f"Evaluated {filename} with an average confidence of: {model_confidence:.4f}")
                except Exception as e:
                    print(f"Error evaluating {filename}: {e}")

        ranked_scores = pd.DataFrame(scores, columns=["Model", "Confidence Score"])
        ranked_scores = ranked_scores.sort_values(by="Confidence Score", ascending=False).reset_index(drop=True)
        return ranked_scores

    def compare_current_model(self, features, target_column=None):
        """
        Compare the given model (`current_model`) with other models in increased and decreased directories.
        """
        if features is None:
            raise ValueError("Features for evaluation are required.")

        # Evaluate the current model
        print("Evaluating current model...")
        current_model_confidence = self.evaluate_model(self.current_model, features, target_column)
        print(f"Current model confidence: {current_model_confidence:.4f}")

        # Evaluate models in increased and decreased directories
        print("\nEvaluating models in increased directory...")
        increased_results = self.evaluate_models(self.increased_path, features, target_column)
        print("\nEvaluating models in decreased directory...")
        decreased_results = self.evaluate_models(self.decreased_path, features, target_column)

        # Compare the current model to the others
        increased_results = increased_results.append({
            "Model": "Current Model",
            "Confidence Score": current_model_confidence
        }, ignore_index=True)
        increased_results = increased_results.sort_values(by="Confidence Score", ascending=False).reset_index(drop=True)

        decreased_results = decreased_results.append({
            "Model": "Current Model",
            "Confidence Score": current_model_confidence
        }, ignore_index=True)
        decreased_results = decreased_results.sort_values(by="Confidence Score", ascending=False).reset_index(drop=True)

        return increased_results, decreased_results

    def load_and_evaluate_models(self, model_path, features, target_column=None):
        """Load the model and features and compare against other models."""
        # If model path is provided, load the current model
        if model_path:
            self.load_current_model(model_path)

        # Compare current model with others
        increased_results, decreased_results = self.compare_current_model(features, target_column)

        # Output results
        print("\nFinal Ranking in Increased Models:")
        print(increased_results)

        print("\nFinal Ranking in Decreased Models:")
        print(decreased_results)

        return increased_results, decreased_results



# Example usage
if __name__ == "__main__":
    # Initialize paths for directories containing decision trees
    increasedDir = "Datasets/increasedForest"  # Replace with actual directory
    decreasedDir = "Datasets/decreasedForest"  # Replace with actual directory
    modelPath = "Datasets/currentPriceData/BTC_2024-07_to_2024-09_tree.pkl"  # Path to the current model file
    csvPath = "Datasets/currentPriceData/BTC_2024-07_to_2024-09.csv"  # Path to the CSV file with features

    # Initialize the InferenceModel and compare models
    inferenceModel = InferenceModel(increasedDir, decreasedDir)
    inferenceModel.load_and_evaluate_models(modelPath, csvPath)








