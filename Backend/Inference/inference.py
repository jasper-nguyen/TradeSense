import os
import pickle
from sklearn.metrics import mean_squared_error
import numpy as np

class ModelEvaluator:
    def __init__(self, baseline_model_path, increased_models_dir, decreased_models_dir):
        # Load baseline model
        print(f"Loading baseline model from {baseline_model_path}...")
        self.baseline_model = self.load_model(baseline_model_path)
        self.increased_models_dir = increased_models_dir
        self.decreased_models_dir = decreased_models_dir

    def load_model(self, model_path):
        """Load a model from a pickle file."""
        try:
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
                print(f"Model loaded successfully from {model_path}")
                return model
        except Exception as e:
            print(f"Error loading model from {model_path}: {e}")
            return None

    def evaluate_model(self, model, X_test, y_test):
        """Evaluate a given model using MSE."""
        try:
            print(f"Evaluating model {model}...")
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            print(f"Model MSE: {mse:.4f}")
            return mse
        except Exception as e:
            print(f"Error evaluating model: {e}")
            return None

    def evaluate_models_in_directory(self, models_dir, X_test, y_test):
        """Evaluate all models in a given directory and return their MSEs."""
        mse_scores = []
        print(f"Evaluating models in directory: {models_dir}")
        for filename in os.listdir(models_dir):
            if filename.endswith('.pkl'):
                model_path = os.path.join(models_dir, filename)
                print(f"Processing model: {filename}")
                model = self.load_model(model_path)
                if model is not None:
                    mse = self.evaluate_model(model, X_test, y_test)
                    if mse is not None:
                        mse_scores.append(mse)
        return mse_scores

    def compare_average_scores(self, X_test, y_test):
        """Compare the average MSE of models in both directories."""
        print("Evaluating models in the increasedDf directory...")
        increased_mse_scores = self.evaluate_models_in_directory(self.increased_models_dir, X_test, y_test)
        
        print("Evaluating models in the decreasedDf directory...")
        decreased_mse_scores = self.evaluate_models_in_directory(self.decreased_models_dir, X_test, y_test)

        # Calculate average MSE for both sets of models
        avg_increased_mse = np.mean(increased_mse_scores) if increased_mse_scores else None
        avg_decreased_mse = np.mean(decreased_mse_scores) if decreased_mse_scores else None

        # Print results
        if avg_increased_mse is not None:
            print(f"Average MSE for increased models: {avg_increased_mse:.4f}")
        else:
            print("No models evaluated in increasedDf.")

        if avg_decreased_mse is not None:
            print(f"Average MSE for decreased models: {avg_decreased_mse:.4f}")
        else:
            print("No models evaluated in decreasedDf.")

        # Compare the results
        if avg_increased_mse is not None and avg_decreased_mse is not None:
            if avg_increased_mse < avg_decreased_mse:
                print("Increased models perform better.")
            else:
                print("Decreased models perform better.")


# Example usage
if __name__ == "__main__":
    baseline_model_path = "Datasets/currentPriceData/regression_tree_BTC_2024-12_to_2025-02.pkl"  # Replace with actual path to the baseline model
    increased_models_dir = "Datasets/increasedForest"  # Replace with actual path to increased models
    decreased_models_dir = "Datasets/decreasedForest"  # Replace with actual path to decreased models

    # Example data for testing (should be the same structure used during training)
    # This assumes you have test data in X_test and y_test for evaluation.
    X_test = np.random.rand(100, 5)  # Replace with actual test data (100 samples, 5 features)
    y_test = np.random.rand(100)  # Replace with actual target data (100 samples)

    evaluator = ModelEvaluator(baseline_model_path, increased_models_dir, decreased_models_dir)
    evaluator.compare_average_scores(X_test, y_test)


