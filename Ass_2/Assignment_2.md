# Assignment 2 
Total score: 70 
Due date: 7/17 

## TEAM:
```
Olvin Bolanos
Anthony Cao
Thomas Tran
Jacob Ursenbach
Greg Zhang
```

## Goals 
• Analysis of customer requirements, writing user requirements, CRC modeling, and class 
or module design, beginning development 

## Requirements for this assignment 

### 1. Analyze all the features of the system specified in the project description document and 
identify all the requirements to implement the features. 
```

```
### 2. Write all the necessary use cases or user stories to implement the feature (a) of the system. 
See assignment #1 for feature (a).  
```

```
### 3. Create all the necessary CRC cards.  
```

```
### 4. Create a class or module diagram. You can use actual paper or a whiteboard to draw the 
diagram. You don’t need to use any UML tool to draw a diagram, although you are welcome 
to do it. 
```

```
### 5. Implement the feature (a) with at least one test case. ** No visual user interface is necessary. ** 
To get the data, use a free package, e.g., “yfinance” in Python, “yahoo-finance” in 
JavaScript, etc., or implement one yourself.  
stockData.py
```
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
        self.stock_symbol = None
        self.stock_data = {"Opening Price": None, "Closing Price": None, "PE_ratio": None,
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
```
stockDataTest.py
```
lines (14 sloc)  505 Bytes

import unittest
#reset the path for this if not using on my laptop
from pythonProjects.stockProgram.getStockData import StockData

class testCase(unittest.TestCase):
    def test(self):
        obj = StockData("8")
        obj.retrieveData()
        print(obj)


        for key, value in obj.stockData.items():
            #if value == None:

            self.assertTrue(value, key + " expected float, but got None")
            print()

if __name__ == '__main__':
    unittest.main()
```
[testCase1.png](testCase1.png)


# Acceptance criteria 
A list of all the necessary use cases or user stories and CRC cards in the format discussed in class 
that meet the requirements of all the features for both the user and developers to implement. 
Correct class diagram 
Functional feature (a) 
 
