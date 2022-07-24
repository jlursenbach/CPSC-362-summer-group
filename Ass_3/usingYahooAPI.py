import requests
import json
import pandas as pd
import pandas_datareader as pdr
import datetime as dt

class stockData:
    def __init__(self):
        self.stockData = {"Opening Price": None, "Closing Price": None, "PE_ratio": None,
                          "PS_ratio": None, "bid": None, "volume": "", "ask": None, "High": None,
                          "Low": None}

        self.historicalData = pd.DataFrame()

    def __str__(self):
        output = ""
        for key, value in self.stockData.items():
            output += f'{key}: {value}' + '\n'

        return output

    def retrieveHistoricalData(self):
        """getting historical stock data
        for the back testing module"""
        start = dt.datetime(2019, 1, 1)
        end = dt.datetime(2022, 7, 22)

        self.historicalData = pdr.get_data_yahoo(self.stockSymbol, start, end)

        #reformatting dataframe to fit the required format for backtesting
        self.historicalData.drop('Adj Close', axis=1, inplace=True)
        self.historicalData = self.historicalData.reindex(columns=
                                                          ['Open', 'High', 'Low', 'Close', 'Volume'])


    def retrieveBasicData(self):
        """retrieving basic stock data using yahoo finance api"""
        url = "https://yfapi.net/v6/finance/quote"
        querystring = {"symbols":"AAPL,USD"}
        headers = {'x-api-key': "pCJyFfGicf5sG8cbj16XO95hHDCtbqFNaqNuaWvn"}
        response = requests.request("GET", url, headers=headers, params=querystring)

        #converting response.txt into a dictionary
        requestedData = json.loads(response.text)["quoteResponse"]["result"][0]


        self.stockData["Opening Price"] = requestedData["regularMarketOpen"]
        self.stockData["Closing Price"] = requestedData["regularMarketPreviousClose"]
        self.stockData["PE_ratio"] = requestedData["trailingPE"]
        self.stockData["PS_ratio"] = requestedData["epsForward"]
        self.stockData["bid"] = requestedData["bid"]
        self.stockData["volume"] = requestedData["regularMarketVolume"]
        self.stockData["ask"] = requestedData["ask"]
        self.stockData["High"] = requestedData["regularMarketDayHigh"]
        self.stockData["Low"] = requestedData["regularMarketDayLow"]

    def set_symbol(self, symbol: str):
        """
        :param symbol:
        :return:
        """
        self.stockSymbol = symbol

    def return_data(self) -> dict:
        """
        :return:
        """
        return {self.stockSymbol: self.stockData}

    def scrape_stock(self, symbol: str) -> dict:
        """
        :param symbol:
        :return:
        """

        self.set_symbol(symbol)
        self.retrieveBasicData()
        self.retrieveHistoricalData()
        return self.return_data()




def main():

    obj1 = stockData()
    obj1.scrape_stock("AAPL")
    print(obj1)
    print(obj1.historicalData.columns.tolist())
    obj1.historicalData = obj1.historicalData.reindex(columns =
                                                      ['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
    #test = pd.DataFrame(data=obj1.stockData, index=[0])
    #print(test)
    #print(obj1.historicalData)
    #print(obj1.historicalData['Date'])

if __name__ == "__main__":
    main()










#print(stockData["quoteResponse"]["result"])

#for i in stockData["quoteResponse"]["result"]:
    #print(i)
"""headers = {
    'x-api-key': "pCJyFfGicf5sG8cbj16XO95hHDCtbqFNaqNuaWvn"
    }
url = "https://yfapi.net/v11/finance/quoteSummary"
querystring = {"symbols":"AAPL, assetProfile"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)"""

