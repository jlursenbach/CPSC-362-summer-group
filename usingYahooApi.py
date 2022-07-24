import requests
import json

class stockData:
    def __init__(self):
        self.stockData = {"Opening Price": None, "Closing Price": None, "PE_ratio": None,
                          "PS_ratio": None, "bid": None, "volume": "", "ask": None}

    def __str__(self):
        output = ""
        for key, value in self.stockData.items():
            output += f'{key}: {value}' + '\n'

        return output

    def retrieveData(self):
        url = "https://yfapi.net/v6/finance/quote"
        querystring = {"symbols":"AAPL,USD"}
        headers = {'x-api-key': "pCJyFfGicf5sG8cbj16XO95hHDCtbqFNaqNuaWvn"}
        response = requests.request("GET", url, headers=headers, params=querystring)

        requestedData = json.loads(response.text)
        requestedData = requestedData["quoteResponse"]["result"][0]


        self.stockData["Opening Price"] = requestedData["regularMarketOpen"]
        self.stockData["Closing Price"] = requestedData["regularMarketPreviousClose"]
        self.stockData["PE_ratio"] = requestedData["trailingPE"]
        self.stockData["PS_ratio"] = requestedData["epsForward"]
        self.stockData["bid"] = requestedData["bid"]
        self.stockData["volume"] = requestedData["regularMarketVolume"]
        self.stockData["ask"] = requestedData["ask"]

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
        self.retrieveData()
        return self.return_data()




def main():

    obj1 = stockData()
    obj1.scrape_stock("AAPL")
    print(obj1)

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

