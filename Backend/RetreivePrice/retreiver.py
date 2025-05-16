import requests

class Retriever:
    BASE_URL = 'https://min-api.cryptocompare.com/data/price'

    def __init__(self, api_key, crypto_symbol):
        self.api_key = api_key
        self.crypto_symbol = crypto_symbol

    #basic function for get current price
    def get_current_price(self):
        params = {
            'fsym': self.crypto_symbol,
            'tsyms': 'USD',
            'api_key': self.api_key
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get('USD')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching current price for {self.crypto_symbol}: {e}")
            return None




    def get_percent_change(self):
                url = 'https://min-api.cryptocompare.com/data/pricemultifull'
                params = {
                     'fsyms': self.crypto_symbol,
                     'tsyms': 'USD',
                     'api_key': self.api_key
                }
                try:
                    response = requests.get(url, params=params)
                    response.raise_for_status()
                    data = response.json()
                    print(data)

                    return round(data["RAW"][self.crypto_symbol]["USD"]["CHANGEPCT24HOUR"], 2)
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching percentage change for {self.crypto_symbol}: {e}")
                    return None


    def get_weekly_percent_change(self):
                url = "https://min-api.cryptocompare.com/data/v2/histoday"
                params = {
                    'fsym': self.crypto_symbol,
                    'tsym': 'USD',
                    'limit': 7,  # Last 8 days (index 0 = 7 days ago, index -1 = today)
                    'api_key': self.api_key
                }

                try:
                    response = requests.get(url, params=params)
                    response.raise_for_status()
                    data = response.json()

                    # Debug print to confirm data shape
                    print(data)

                    prices = data.get("Data", {}).get("Data", [])

                    if len(prices) < 2:
                        raise ValueError("Insufficient price data for weekly comparison")

                    price_today = prices[-1].get('close')
                    price_week_ago = prices[0].get('close')

                    if price_today is None or price_week_ago is None:
                        raise ValueError("Missing 'close' price in response")

                    percent_change = ((price_today - price_week_ago) / price_week_ago) * 100
                    return round(percent_change, 2)

                except (requests.exceptions.RequestException, ValueError, KeyError) as e:
                    print(f"Error fetching weekly percent change for {self.crypto_symbol}: {e}")
                    return None



    def get_monthly_percent_change(self):
        url = "https://min-api.cryptocompare.com/data/v2/histoday"
        params = {
            'fsym': self.crypto_symbol,
            'tsym': 'USD',
            'limit': 30,
            'api_key': self.api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            prices = data.get("Data", {}).get("Data", [])

            if len(prices) < 2:
                raise ValueError("Not enough data for 30-day comparison")

            price_today = prices[-1].get("close")
            price_30_days_ago = prices[0].get("close")

            if price_today is None or price_30_days_ago is None:
                raise ValueError("Missing price data in API response")

            percent_change = ((price_today - price_30_days_ago) / price_30_days_ago) * 100
            return round(percent_change, 2)

        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            print(f"Error fetching 30-day percentage change for {self.crypto_symbol}: {e}")
            return None



    def get_yearly_percent_change(self):
        try:
            url = "https://min-api.cryptocompare.com/data/v2/histoday"
            params = {
                'fsym': self.crypto_symbol,
                'tsym': 'USD',
                'limit': 365,
                'api_key': self.api_key
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            prices = data["Data"]["Data"]
            if len(prices) < 366:
                raise ValueError("Insufficient data returned for 365-day comparison")
            price_today = prices[-1]['close']
            price_1_year_ago = prices[0]['close']
            percent_change = ((price_today - price_1_year_ago) / price_1_year_ago) * 100
            return round(percent_change, 2)
        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            print(f"Error fetching 1-year percentage change for {self.crypto_symbol}: {e}")
            return None


    #NOTE: YOU GUYS CAN BUILD OFF OF THIS TO GET RANGES OF DATA IN CERTAIN FORMATS

        



# Example usage:
if __name__ == "__main__":
    api_key = "519a1532cfff52e51dfedcd5d693810d64e5708b75cc4d341e572cbc05abe2cf"

    sol_retriever = Retriever(api_key, "SOL")
    btc_retriever = Retriever(api_key, "BTC")
    eth_retriever = Retriever(api_key, "ETH")

    # Example print to confirm creation
    print("Retrievers created for:", sol_retriever.crypto_symbol, btc_retriever.crypto_symbol, eth_retriever.crypto_symbol)

    print(sol_retriever.get_current_price())

    

