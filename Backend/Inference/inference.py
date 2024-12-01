import os
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class InferenceModel:
    def __init__(self, dataframe_path, increased_path,decreased_path):
        """
        Initializes the InferenceModel class.
        """
        self.dataframe_path = dataframe_path
        self.increased_path = increased_path
        self.decreased_path = decreased_path
        self.dataframe = self._load_dataframe()

    def _load_dataframe(self):
        """Loads the input DataFrame from the given path."""
        if not os.path.exists(self.dataframe_path):
            raise FileNotFoundError(f"Input DataFrame file not found: {self.dataframe_path}")
        
        df = pd.read_csv(self.dataframe_path)
        if df.empty:
            raise ValueError("The provided DataFrame is empty.")
        
        return df
    def evaluate_models(self, treesPath):
        """
        Evaluates the input DataFrame against all decision tree models in the directory
        and ranks them by confidence score.
    
        Returns:
            pd.DataFrame: A DataFrame ranking the models by confidence score.
        """
        if not os.path.exists(treesPath):
            raise FileNotFoundError(f"The directory {self.trees_dir} does not exist.")

        scores = []
    
        for filename in os.listdir(treesPath):
            if filename.endswith(".pkl"):
                # Load the decision tree model
                model_path = os.path.join(treesPath, filename)
                with open(model_path, "rb") as model_file:
                    clf = pickle.load(model_file)  # Just load the model (without feature names)

                # Check if the model is indeed a DecisionTreeClassifier
                if not isinstance(clf, DecisionTreeClassifier):
                    print(f"Skipping {filename}: not a valid decision tree model.")
                    continue

                # Get feature names from the model using the tree structure
                feature_names = clf.feature_names_in_ if hasattr(clf, "feature_names_in_") else self.dataframe.columns.tolist()

                # Align features: add missing features and drop extra features
                aligned_dataframe = self.dataframe.copy()

                # List missing and extra features
                missing_features = [f for f in feature_names if f not in aligned_dataframe.columns]
                extra_features = [f for f in aligned_dataframe.columns if f not in feature_names]

                # Add missing features as zero-filled columns
                for feature in missing_features:
                    aligned_dataframe[feature] = 0

                # Drop extra features
                aligned_dataframe = aligned_dataframe[feature_names]

                # Calculate confidence score
                try:
                    confidences = clf.predict_proba(aligned_dataframe).max(axis=1)
                    average_confidence = confidences.mean()
                    scores.append((filename, average_confidence))

                    print( "most recent price data performed on file :" +filename + "with an average confidence of :"+str(average_confidence))
                except Exception as e:
                    print(f"Error evaluating {filename}: {e}")

        # Rank models by confidence score
        ranked_scores = pd.DataFrame(scores, columns=["Model", "Confidence Score"])
        ranked_scores = ranked_scores.sort_values(by="Confidence Score", ascending=False).reset_index(drop=True)
        
        return ranked_scores

    def calculate_weighted_average(self, results):
        """
        Calculates the weighted average of the confidence scores for models.

        Args:
            results (pd.DataFrame): DataFrame containing models and their corresponding confidence scores.
    
        Returns:
            float: Weighted average of confidence scores.
        """
        # Ensure 'weights' is numeric by converting to pd.Series (if it's an Index or non-numeric object)
        if isinstance(results['Confidence Score'], pd.Series):
            confidences = results['Confidence Score']
        else:
            confidences = pd.Series(results['Confidence Score'])

        # Assuming you have a 'weights' column or you can compute weights (e.g., by confidence score or model type)
        weights = confidences  # In case weights are the confidence scores themselves

        # Ensure weights are numeric
        weights = pd.to_numeric(weights, errors='coerce')  # Coerce any non-numeric values to NaN (optional)

        # Calculate weighted sum
        weighted_sum = (confidences * weights).sum()  # Sum of weighted confidences

        # Calculate total weight
        total_weights = weights.sum()  # Sum of weights

        if total_weights == 0:
            raise ValueError("Total weights sum to zero, cannot compute weighted average.")

        # Compute weighted average
        weighted_average = weighted_sum / total_weights

        return weighted_average


    def compare_increased_and_decreased(self):
        """
        Compares the weighted average confidence scores for two sets of models and DataFrames.
    
        Parameters:
        increasedPath (str): Path to the DataFrame for the "increased" scenario.
        increasedDir (str): Directory containing decision trees for the "increased" scenario.
        decreasedPath (str): Path to the DataFrame for the "decreased" scenario.
        decreasedDir (str): Directory containing decision trees for the "decreased" scenario.

        Returns:
            None: Prints the results of the comparison.
        """
        # Evaluate models
        print("calculating confidence for increased class model")
        increased_results = self.evaluate_models(self.increased_path)
        print("calculating confidence for decreased class model")
        decreased_results = self.evaluate_models(self.decreased_path)

        # Calculate weighted averages
        increased_avg = self.calculate_weighted_average(increased_results)
        decreased_avg = self.calculate_weighted_average(decreased_results)

        # Print comparison results
        print("Weighted Average Confidence Scores:")
        print(f"Increased: {increased_avg:.4f}")
        print(f"Decreased: {decreased_avg:.4f}")

        if increased_avg > decreased_avg:
            print("The 'Increased' models performed better on average.")
        elif decreased_avg > increased_avg:
            print("The 'Decreased' models performed better on average.")
        else:
            print("Both sets of models performed equally well.")


# Example usage
if __name__ == "__main__":
    # Paths for increased and decreased scenarios
    #currentPath = "increasedDF/BTC_2024-10_to_2024-12.csv"  # Replace with actual path
    currentPath = "increasedDF/BTC_2012-01_to_2012-03.csv"  # Replace with actual path
    increasedDir = "increasedForest"       # Replace with actual directory
    decreasedDir = "decreasedForest"       # Replace with actual directory

    # Compare the models
    inferenceModel= InferenceModel( currentPath, increasedDir, decreasedDir)
    inferenceModel.compare_increased_and_decreased()

