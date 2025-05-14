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

    

