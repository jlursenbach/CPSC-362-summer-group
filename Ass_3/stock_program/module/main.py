from module.usingYahooAPI import GetBasicStockData
from module.back_testing import StartBackTesting
from module.tentativePortfolio import Tentative_Portfolio
from module.getHistoricalData import RetrieveHistoricalData
from module.returnJson import convertToJson



#we demo'd our adapter pattern in class and you aprroved of it
#adaptees using this adapter are pullBasicStockData and getHistoricalData
class getDataAdapter:
    def __init__(self, **adaptedMethod):
        self.__dict__.update(adaptedMethod)

class View:
    def __init__(self):
        pass
    def interfaceGetData(self, obj, symbol):
        obj.setSymbol(symbol)
        getDataAdapter(data=obj.getData())

    #used by
    #backtesting
    def interfaceBackTest(self, obj, strat, historicalData):
        obj.setStratName(strat)
        #obj.setStrat()
        obj.setHistoricalData(historicalData)
        #obj.setCashAmount(cash)
        obj.getData()

    def interfaceCreatePortfolio(self, obj, fileName):
        obj.setPortfolio()
        obj.savePortfolio(fileName)


    def interfaceUpdatePortfolio(self, obj, fileName, symbol, data, strategy = ""):
        obj.loadPortfolio(fileName)
        obj.setSymbol(symbol)
        if symbol not in obj.portfolio:
            obj.insertNewEntry()

        if type(data) is dict:
            obj.setBasicData(data)

        else:
            obj.setBackTestResults(data, strategy)

        obj.savePortfolio(fileName)

    def interfaceLoadPortfolio(self, obj, fileName):
        obj.loadPortfolio(fileName)
        obj.output()



class Model:
    def __init__(self):
        self.view = View()
        self.scrapper = GetBasicStockData()
        self.backtesting = StartBackTesting()
        self.userPortfolio = Tentative_Portfolio()
        self.histData = RetrieveHistoricalData()
        self.convert = convertToJson()


class Controller:
    def __init__(self, viewer, model):
        self.view = viewer
        self.model = model

    def lookup(self, cmd):
        # getting basic stock data and historical data
        print("basic data: ")
        self.view.interfaceGetData(self.model.scrapper, cmd[1])
        print(self.model.scrapper)
        print()

    def backTesting(self, cmd):
        self.view.interfaceGetData(self.model.histData, cmd[1])
        # interfaceBackTest(backtesting, cmd[2], histData.historicalData, cmd[3])
        self.view.interfaceBackTest(self.model.backtesting, cmd[2], self.model.histData.historicalData)
        print("back testing results: ")
        print(self.model.backtesting.bt.run())
        print()

    def create_portfolio(self, cmd):
        self.view.interfaceCreatePortfolio(self.model.userPortfolio, cmd[-1])

    def updatePortfolio(self, cmd):
        if "-bd" in cmd and len(self.model.scrapper.stockData) > 0:
            self.view.interfaceUpdatePortfolio(self.model.userPortfolio, cmd[1], cmd[2], self.model.scrapper.stockData)

        if "-bt" in cmd:
            self.view.interfaceUpdatePortfolio(self.model.userPortfolio,
                                               cmd[1], cmd[2], self.model.backtesting.bt.run(),
                                               self.model.backtesting.strategyName)

    def loadPortfolio(self, cmd):
        self.view.interfaceLoadPortfolio(self.model.userPortfolio, cmd[-1])


    def parse(self, cmd):
        help = "lookup <stock symbol>\n" \
               "description: gets data for selected stock\n\n" \
               "createPortfolio <file name>\n" \
               "description: creates a portfolio\n\n" \
               "backtest <stock symbol> <strategy> <amount to invest>\n" \
               "        strategies: SmaCross, Rsi 10000\n" \
               "example: backtest GOOG SmaCross\n" \
               "descrtiption: backtest a stock with strategy\n\n" \
               "update <file name> <stock symbol> <optional: -bd -bt>\n" \
               "        -bd: load basic data for stock into portfolio\n" \
               "        -bt: load backtest results for stock int portfolio\n" \
               "example: update test1 GOOG -bd\n" \
               "example: update test1 GOOG -bt\n" \
               "example: update test1 GOOG -bd -bt\n" \
               "description: add stock data to a portfolio\n\n" \
               "load <file name>\n" \
               "description: loads a portfolio and displays it's contents\n\n" \
               "exit\n" \
               "description: exits program\n\n" \
               "clear\n" \
               "description: clears screen\n"


        # lookup basic stock data
        if cmd[0] == "lookup":
            self.lookup(cmd)



        # gather historical data and conduct backtesting
        elif cmd[0] == "backtest":
            # conducting back testing
            self.backTesting(cmd)


        # creating portfolio
        elif cmd[0] == "createPortfolio":
            self.create_portfolio(cmd)


        # update portfolio
        elif cmd[0] == "update":
            self.updatePortfolio(cmd)

        # loading portfolio contents
        elif cmd[0] == "load":
            self.loadPortfolio(cmd)


        elif cmd[0] == "exit":
            exit()

        elif cmd[0] == 'help':
            print(help)

        elif cmd[0] == 'clear':
            print("\n" * 1000)

        #else:
            #print(f"[!] {userInput} is not a recognized command")


def main():
    view = View()
    model = Model()
    controller = Controller(view, model)
    while True:
        userInput = ""
        userInput = input("enter command> ")
        cmd = userInput.split()

        if len(cmd) > 6:
            print(f"[!] {str(userInput)} is not a recognized command")
            continue

        controller.parse(cmd)


if __name__ == '__main__':
    main()


"""file is saved as a pickle which is a python dict, when you return a pickle, if html does not 
python code, it uderstands json though, even though json and python dict is almost the same thing
if olvin, if the html he is writing needs to view the pickle, so write an adapter to convert
the pickle into a json."""
