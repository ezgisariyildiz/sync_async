import requests
import os
import time

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']
results = []

# for symbol in symbols:
#     print('Working on symbol {}'.format(symbol))
#     response = requests.get(url.format(symbol, api_key))
#     results.append(response.json())
# print('You did it!')

def run_tasks():
    for symbol in symbols:
        response = requests.get(url.format(symbol, api_key))
        results.append(response.json())


print("Timer started...")
start = time.time()
run_tasks()
end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))