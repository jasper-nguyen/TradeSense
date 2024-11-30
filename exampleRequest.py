import requests
import pandas as pd

API_KEY = '519a1532cfff52e51dfedcd5d693810d64e5708b75cc4d341e572cbc05abe2cf'
CRYPTO = 'BTC'
BASE_URL = 'https://min-api.cryptocompare.com/data/v2/histoday'

def fetch_price_data(coin, from_date, to_date):
    url = BASE_URL
    params = {
        'fsym': coin,
        'tsym': 'USD',
        'toTs': int(to_date.timestamp()),  # End date as timestamp
        'limit': 2000,  # Max number of data points to return
        'api_key': API_KEY
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return pd.DataFrame()

    data = response.json()
    prices = data.get('Data', {}).get('Data', [])
    return pd.DataFrame(prices)

def find_earliest_valid_date(coin):
    start_date = datetime(2012, 1, 1)
    end_date = datetime.now()

    while True:
        prices = fetch_price_data(coin, start_date, end_date)
        if not prices.empty:
            return start_date
        start_date -= timedelta(days=30)  # Move backward by 30 days

def analyze_prices(prices):
    if 'high' in prices.columns:
        initial_average = prices['high'].mean()
        future_prices = prices['high'].iloc[-90:]  # Check the last 90 days
        future_average = future_prices.mean() if not future_prices.empty else None
        return future_average > initial_average if future_average else False
    else:
        return False

def save_to_csv(prices, folder, filename):
    prices.to_csv(os.path.join(folder, filename), index=False)
    print(f"Saved: {filename}")  # Print statement when a file is saved

def main(folder1, folder2):
    os.makedirs(folder1, exist_ok=True)
    os.makedirs(folder2, exist_ok=True)

    coin_id = CRYPTO
    start_date = find_earliest_valid_date(coin_id)
    end_date = datetime.now()

    current_year = start_date.year

    while current_year <= end_date.year:
        for month in range(1, 13):  # Iterate through each month
            month_start = datetime(current_year, month, 1)
            month_end = (month_start + pd.offsets.MonthEnd()).date()  # Get the end of the month

            if month_start < end_date:  # Ensure we don't go beyond the current date
                # Only fetch data for the specified year and month
                prices = fetch_price_data(coin_id, month_start, month_end)

                if not prices.empty:
                    # Process the data
                    prices['time'] = pd.to_datetime(prices['time'], unit='s')  # Convert timestamp to datetime
                    prices.rename(columns={'time': 'date', 'high': 'high_price'}, inplace=True)

                    result = 'increased' if analyze_prices(prices) else 'not_increased'
                    filename = f"{CRYPTO}_{month_start.strftime('%Y-%m')}_to_{month_end.strftime('%Y-%m')}.csv"
                    if result == 'increased':
                        save_to_csv(prices, folder2, filename)
                    else:
                        save_to_csv(prices, folder1, filename)

        # Move to the next year
        current_year += 1
        time.sleep(1)  # Delay for 1 second to avoid hitting the rate limit


# Example of fetching data
from datetime import datetime, timedelta

start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 4, 1)

prices = fetch_price_data(start_date, end_date)
print(prices.head())  # Check the fields returned
