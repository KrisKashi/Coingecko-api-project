import requests
response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=gbp, timeout=10")
data_btc = response.json()
price = (data_btc["bitcoin"]["gbp"])
print (f"Bitcoin price is £{price}")