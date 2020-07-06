import urllib.request
import sys
import json

def getStockData(inputString):
    baseURL = 'https://www.alphavantage.co/query?'
    function = 'function=GLOBAL_QUOTE'
    symbol = '&symbol=' + inputString
    apiKey = '&apikey=' + 'ZSPQ42689WZEZ0HD'
    url = baseURL + function + symbol + apiKey
    connection = urllib.request.urlopen(url)

    return(connection.read().decode())

def main():
    #ask for stock symbols from user (infinitely)
    symbol_list=[]
    symbol = input("Please enter a stock symbol (enter 'quit' to exit): ")
    while (symbol != 'quit'):
        symbol_list.append(symbol)
        symbol = input("Please enter another stock symbol (enter 'quit' to exit): ")

    stock_dictionaries = []
    #get stock info from API
    for stock in symbol_list:
        #print the JSON-formatted response
        jsondata = getStockData(stock)
        print(jsondata)
        #convert the JSON to a python dictionary
        stock_dictionaries.append(json.loads(jsondata))

    #print the price only
    for dict in stock_dictionaries:
        print('The current price of ' + dict['Global Quote']['01. symbol'] + ' is: ' + dict['Global Quote']['05. price'])

main()
