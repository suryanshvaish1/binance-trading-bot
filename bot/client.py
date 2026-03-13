from binance.client import Client

def get_client(api_key, api_secret):
    client = Client(api_key, api_secret)

    # Set Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
