#!/usr/bin/env python3
# --------------------------------------------------------------------
# CPSC 362-01
# Coding Team:   Group 1
__authors__ = ["Olvin Bolanos", "Anthony Cao", "Thomas Tran", "Jacob Ursenbach", "Greg Zhang"]
__copyright__ = "Open Source"
__credits__ = ["Olvin Bolanos", "Anthony Cao", "Thomas Tran", "Jacob Ursenbach", "Greg Zhang"]
__license__ = None
__version__ = "0.0.5"
__maintainer__ = "Jacob Ursenbach"
__email__ = "jacob.ursenbach@gmail.com"
__status__ = "Production"
__last_update__ = 20220716
# --------------------------------------------------------------------
#
# getStockData class Returns predefined set of stock data for a stock symbol given by user 
#

import yfinance
import yahoo_fin.stock_info as stockInfo


class getStockData:
    def __init__(self, symbol: str = None):
        """

        :param symbol:
        """
        self.stockSymbol = None
        self.stockData = {"Opening Price": None, "Closing Price": None, "PE_ratio": None,
                          "PS_ratio": None, "Company_Cash_Reserve": None, "Company_Debt": None,
                          "bid": None, "volume": "", "ask": None}

        if symbol:
            self.set_symbol(symbol)
            self.retrieveData()

    def retrieveData(self):
        """

        :return:
        """
        getInfo = yfinance.Ticker(self.stockSymbol)
        getInfo2 = stockInfo.get_quote_table(self.stockSymbol)

        self.stockData["Company_Cash_Reserve"] = getInfo.info["totalCash"]
        self.stockData["Company_Debt"] = getInfo.info["totalDebt"]

        self.stockData["Opening Price"] = getInfo2["Open"]
        self.stockData["bid"] = getInfo2["Bid"]
        self.stockData["volume"] = getInfo2["Volume"]
        self.stockData["ask"] = getInfo2["Ask"]
        self.stockData["Closing Price"] = getInfo2["Previous Close"]
        self.stockData["PE_ratio"] = getInfo2["PE Ratio (TTM)"]

        val = stockInfo.get_stats_valuation(self.stockSymbol)
        val = val.iloc[:, : 2]
        val.columns = ["Attribute", "Recent"]

        PS = float(val[val.Attribute.str.contains("Price/Sales")].iloc[0,1])

        self.stockData["PS_ratio"] = PS

    def set_symbol(self, symbol: str):
        """

        :param symbol:
        :return:
        """
        self.stockSymbol = symbol

    def return_data(self):
        """

        :return:
        """
        return {self.stockSymbol: self.stockData}

    def scrape_stock(self, symbol: str) -> str:
        """

        :param symbol:
        :return:
        """


def main():
    scraper = getStockData("FB")
    scraper.retrieveData()
    print(scraper.return_data())


if __name__ == "__main__":
    main()

"""self.stockData["open"] = getInfo.info["open"]
        self.stockData["bid"] = getInfo.info["bid"]
        self.stockData["volume"] = getInfo.info["volume"]
        self.stockData["ask"] = getInfo.info["ask"]
        self.stockData["close"] = getInfo.info["regularMarketPreviousClose"]"""

