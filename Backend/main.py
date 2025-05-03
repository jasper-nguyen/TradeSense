
from fastapi import FastAPI
import uvicorn
import numpy as np
from typing import Dict, Any
from Inference.inference import ModelEvaluator
from RetreivePrice.retreiver import Retriever
# Initialize FastAPI app
app = FastAPI()

# define paths for each currency
#BTC
baseline_model_path_BTC= "Inference/Datasets/BTC/currentPriceData/regression_tree_BTC_2024-12_to_2025-02.pkl"
increased_models_dir_BTC= "Inference/Datasets/BTC/increasedForest"
decreased_models_dir_BTC= "Inference/Datasets/BTC/decreasedForest"
#ETH
baseline_model_path_ETH= "Inference/Datasets/ETH/currentPriceData/regression_tree_ETH_2025-01_to_2025-03.pkl"
increased_models_dir_ETH= "Inference/Datasets/ETH/increasedETHForest"
decreased_models_dir_ETH= "Inference/Datasets/ETH/decreasedETHForest"
#
baseline_model_path_SOL= "Inference/Datasets/SOL/currentPriceData/regression_tree_SOL_2025-01_to_2025-03.pkl"
increased_models_dir_SOL= "Inference/Datasets/SOL/increasedSOLForest"
decreased_models_dir_SOL= "Inference/Datasets/SOL/decreasedSOLForest"

# test parameters 
X_test = np.random.rand(100, 5)  
y_test = np.random.rand(100)  

#initialize evaluators
BTCevaluator = ModelEvaluator(baseline_model_path_BTC, increased_models_dir_BTC, decreased_models_dir_BTC)
ETHevaluator = ModelEvaluator(baseline_model_path_ETH, increased_models_dir_ETH, decreased_models_dir_ETH)
SOLevaluator = ModelEvaluator(baseline_model_path_SOL, increased_models_dir_SOL, decreased_models_dir_SOL)

#KEY FOR PRICE API
api_key = "519a1532cfff52e51dfedcd5d693810d64e5708b75cc4d341e572cbc05abe2cf"

#initialize retreivers for price 
sol_retriever = Retriever(api_key, "SOL")
btc_retriever = Retriever(api_key, "BTC")
eth_retriever = Retriever(api_key, "ETH")
    
# Define the API endpoint

#routes for getting AI prediction 
@app.get("/evaluate-BTC")
async def evaluate_BTC():
    result = BTCevaluator.compare_average_scores(X_test, y_test)
    return result

@app.get("/evaluate-ETH")
async def evaluate_ETH():
    result = ETHevaluator.compare_average_scores(X_test, y_test)
    return result

@app.get("/evaluate-SOL")
async def evaluate_SOL():
    result = SOLevaluator.compare_average_scores(X_test, y_test)
    return result

#routes for getting current price 
@app.get("/current-price-BTC")
async def current-price-BTC():
    result = btc_retriever.get_current_price()
    return result

@app.get("/current-price-ETH")
async def current-price-ETH():
    result = eth_retriever.get_current_price()
    return result

@app.get("/current-price-SOL")
async def current-price-SOL():
    result = sol_retriever.get_current_price()
    return result


# Run the app using uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
