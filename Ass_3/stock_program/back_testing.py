from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd
import pandas_datareader as pdr
from backtesting.test import SMA, GOOG
import talib


def decoratorGetData(method):
    def wrapper(self):
        if self.strategyName == "SmaCross":
            self.strategy = SmaCross

        elif self.strategyName == "Rsi":
            self.strategy = rsiOscillator

        method(self)

    return wrapper



class startBackTesting:
    def __init__(self):
        self.strategyName = ""
        self.historicalData = pd.DataFrame()
        self.strategy = None

    @decoratorGetData
    def getData(self):
        self.bt = Backtest(self.historicalData, self.strategy,
                           cash=10000, commission=.002,
                           exclusive_orders=True)

    def setStratName(self, name):
        self.strategyName = name

    def setHistoricalData(self, data):
        self.historicalData = data


class SmaCross(Strategy):
    """simple moving average crossover strat"""
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

class rsiOscillator(Strategy):

    upper = range(50, 85, 5)
    lower = range(10, 45, 5)
    rsiWindow = 14

    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsiWindow)

    def next(self):
        if crossover(self.rsi, self.upper):
            self.position.close()

        elif crossover(self.lower, self.rsi):
            self.buy()




