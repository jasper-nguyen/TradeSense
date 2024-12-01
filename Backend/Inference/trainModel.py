def evaluate_models(self, treesPath):
    scores = []
 
    for filename in os.listdir(treesPath):
        if filename.endswith(".pkl"):
            model_path = os.path.join(treesPath, filename)
            try:
                with open(model_path, "rb") as model_file:
                    clf = pickle.load(model_file)

                # Check if the model is either a classifier or regressor
                if isinstance(clf, DecisionTreeClassifier):
                    # For classifiers, use predict_proba
                    feature_names = clf.feature_names_in_ if hasattr(clf, "feature_names_in_") else self.dataframe.columns.tolist()
                    aligned_dataframe = self.dataframe[feature_names]

                    if not all(feature in aligned_dataframe.columns for feature in feature_names):
                        print(f"Missing some features in {filename}, skipping this model.")
                        continue

                    confidences = clf.predict_proba(aligned_dataframe).max(axis=1)  # Get max probability as confidence
                    average_confidence = confidences.mean()

                elif isinstance(clf, DecisionTreeRegressor):
                    # For regressors, use predict and calculate confidence based on residuals or similar
                    feature_names = clf.feature_names_in_ if hasattr(clf, "feature_names_in_") else self.dataframe.columns.tolist()
                    aligned_dataframe = self.dataframe[feature_names]

                    if not all(feature in aligned_dataframe.columns for feature in feature_names):
                        print(f"Missing some features in {filename}, skipping this model.")
                        continue

                    predictions = clf.predict(aligned_dataframe)
                    residuals = abs(predictions - self.dataframe['close'])  # Calculate residuals as measure of confidence
                    average_confidence = residuals.mean()  # You can modify this logic depending on what you're aiming to measure

                else:
                    print(f"Skipping {filename}: not a valid decision tree model.")
                    continue

                scores.append((filename, average_confidence))
                print(f"Evaluated {filename} with an average confidence of: {average_confidence:.4f}")
            except Exception as e:
                print(f"Error evaluating {filename}: {e}")

    ranked_scores = pd.DataFrame(scores, columns=["Model", "Confidence Score"])
    ranked_scores = ranked_scores.sort_values(by="Confidence Score", ascending=False).reset_index(drop=True)
    return ranked_scores
