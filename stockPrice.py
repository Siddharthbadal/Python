import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token **********************'
}


def get_meta_data(ticker):
    url = 'https://api.tiingo.com/tiingo/daily/{}'.format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()


def get_price_data(ticker):
    url = 'https://api.tiingo.com/tiingo/daily/{}/prices'.format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]


def ticker(tid):
    context = {}
    context['ticker'] = tid
    context['Price'] = get_price_data(tid)

    return context


stock_ticker = input('Enter the ticker: ')
result = ticker(stock_ticker)

print(f"Open : {result['Price']['open']}")
print(f"High : {result['Price']['high']}")
print(f"Low  : {result['Price']['low']}")
print(f"Close: {result['Price']['close']}")
