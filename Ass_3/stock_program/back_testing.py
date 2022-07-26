from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

from backtesting.test import SMA, GOOG

class startBackTesting:
    def __init__(self):
        self.historicalData = pd.DataFrame()

    def getBackTestingResults(self, dataFrame):
        self.setDataFrame(dataFrame)
        self.bt = Backtest(self.historicalData, SmaCross,
                           cash=10000, commission=.002,
                           exclusive_orders=True)


    def setDataFrame(self, dataFrame):
        self.historicalData = dataFrame


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




