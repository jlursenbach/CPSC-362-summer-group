import yfinance
import yahoo_fin.stock_info as stockInfo


class getStockData:
    def __init__(self, symbol=""):
        self.stockSymbol = symbol
        self.stockData = {"stock_symbol": {"Product": None, "Opening Price": None, "Closing Price": None, "PE_ratio": None,
                          "PS_ratio": None, "Company_Cash_Reserve": None, "Company_Debt": None,
                          "Bid": None, "Volume": "", "Ask": None}}

    def output(self):
        for i in self.stockData["stock_symbol"]:
            print(f'{i}: {self.stockData["stock_symbol"][i]}')


    def retrieveData(self):
        getInfo = yfinance.Ticker(self.stockSymbol)
        getInfo2 = stockInfo.get_quote_table(self.stockSymbol)

        self.stockData["stock_symbol"]["Product"] = getInfo.info["longBusinessSummary"]
        self.stockData["stock_symbol"]["Company_Cash_Reserve"] = getInfo.info["totalCash"]
        self.stockData["stock_symbol"]["Company_Debt"] = getInfo.info["totalDebt"]

        self.stockData["stock_symbol"]["Opening Price"] = getInfo2["Open"]
        self.stockData["stock_symbol"]["Bid"] = getInfo2["Bid"]
        self.stockData["stock_symbol"]["Volume"] = getInfo2["Volume"]
        self.stockData["stock_symbol"]["Ask"] = getInfo2["Ask"]
        self.stockData["stock_symbol"]["Closing Price"] = getInfo2["Previous Close"]
        self.stockData["stock_symbol"]["PE_ratio"] = getInfo2["PE Ratio (TTM)"]

        val = stockInfo.get_stats_valuation(self.stockSymbol)
        val = val.iloc[:, : 2]
        val.columns = ["Attribute", "Recent"]

        PS = float(val[val.Attribute.str.contains("Price/Sales")].iloc[0,1])

        self.stockData["stock_symbol"]["PS_ratio"] = PS


def main():
    obj1 = getStockData("FB")
    obj1.retrieveData()
    obj1.output()
    #print(obj1.stockData)


if __name__ == "__main__":
    main()

"""self.stockData["open"] = getInfo.info["open"]
        self.stockData["bid"] = getInfo.info["bid"]
        self.stockData["volume"] = getInfo.info["volume"]
        self.stockData["ask"] = getInfo.info["ask"]
        self.stockData["close"] = getInfo.info["regularMarketPreviousClose"]"""
