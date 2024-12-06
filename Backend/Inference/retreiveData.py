import requests
import pandas as pd
import os
from datetime import datetime, timedelta
import time

# Constants
CRYPTO = 'BTC'  # Cryptocurrency symbol
API_KEY = '519a1532cfff52e51dfedcd5d693810d64e5708b75cc4d341e572cbc05abe2cf'  # Replace with your CryptoCompare API key
BASE_URL = 'https://min-api.cryptocompare.com/data/v2/histoday'

def fetch_price_data(coin, from_date, to_date, retries=3, delay=5):
    url = BASE_URL
    params = {
        'fsym': coin,
        'tsym': 'USD',
        'toTs': int(to_date.timestamp()),
        'limit': 2000,
        'api_key': API_KEY
    }
    
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # This will raise an exception for 4xx/5xx errors

            data = response.json()
            prices = data.get('Data', {}).get('Data', [])
            return pd.DataFrame(prices)  # Return the prices as a DataFrame

        except requests.exceptions.RequestException as e:
            # Handle all request-related exceptions (ConnectionError, Timeout, etc.)
            print(f"Attempt {attempt + 1}/{retries} failed: {e}")
            attempt += 1
            if attempt < retries:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)  # Wait before retrying
            else:
                print("Max retries exceeded. Could not fetch data.")
                return pd.DataFrame()  # Return an empty DataFrame if all attempts fail

def analyze_prices(prices, future_prices):
    if 'close' in prices.columns and 'close' in future_prices.columns:
        initial_average = prices['close'].max()
        future_average = future_prices['close'].max()
        print(f"Analyzing: Initial Avg = {initial_average}, Future Avg = {future_average}")  # Debug statement
        return future_average > initial_average
    else:
        return False

def save_to_csv(prices, folder, filename):
    prices.to_csv(os.path.join(folder, filename), index=False)
    print(f"Saved to {folder}: {filename}")  # Updated print statement

def main(folder1, folder2):
    os.makedirs(folder1, exist_ok=True)
    os.makedirs(folder2, exist_ok=True)

    coin_id = CRYPTO
    start_year = 2011  # Start from 2011
    end_year = datetime.now().year

    for current_year in range(start_year, end_year + 1):
        for month in range(1, 13):  # Iterate through all months
            month_start = datetime(current_year, month, 1)
            month_end = (month_start + pd.offsets.MonthEnd()).to_pydatetime()

            # Define the three-month period (current period)
            three_month_start = month_start
            three_month_end = month_start + pd.DateOffset(months=3) - timedelta(days=1)

            # Fetch data for the current three-month period
            prices = fetch_price_data(coin_id, three_month_start, three_month_end)

            if not prices.empty:
                prices['time'] = pd.to_datetime(prices['time'], unit='s')  # Convert timestamps to datetime
                prices = prices[(prices['time'] >= three_month_start) & (prices['time'] <= three_month_end)]

                # Define the following three-month period for comparison (future period)
                future_three_month_start = three_month_end + timedelta(days=1)  # Next day after current period ends
                future_three_month_end = future_three_month_start + pd.DateOffset(months=3) - timedelta(days=1)

                # Fetch data for the following three-month period (future)
                print(f"Fetching future data: {future_three_month_start} to {future_three_month_end}")  # Debugging
                future_prices = fetch_price_data(coin_id, future_three_month_start, future_three_month_end)

                if not future_prices.empty:
                    future_prices['time'] = pd.to_datetime(future_prices['time'], unit='s')  # Convert timestamps to datetime
                    future_prices = future_prices[(future_prices['time'] >= future_three_month_start) & (future_prices['time'] <= future_three_month_end)]

                    # Analyze prices
                    result = 'increased' if analyze_prices(prices, future_prices) else 'not_increased'

                    # Save only the current three-month period data
                    prices.rename(columns={'time': 'date', 'high': 'high_price'}, inplace=True)
                    filename = f"{CRYPTO}_{three_month_start.strftime('%Y-%m')}_to_{three_month_end.strftime('%Y-%m')}.csv"
                    if result == 'increased':
                        save_to_csv(prices, folder2, filename)
                    else:
                        save_to_csv(prices, folder1, filename)

                else:
                    print(f"Future data for {future_three_month_start} to {future_three_month_end} is empty.")

            # Sleep to avoid hitting the rate limit (original behavior)
            time.sleep(1)  # This sleep preserves the rate-limiting logic you originally had
    
# Example usage
folder1_path = "Datasets/decreasedCSV"
folder2_path = "Datasets/increasedCSV"
main(folder1_path, folder2_path)

