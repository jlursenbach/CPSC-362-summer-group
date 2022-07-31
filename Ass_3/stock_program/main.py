from pythonProjects.stockProgramV3.pullBasicStockData import getBasicStockData
from pythonProjects.stockProgramV3.back_testing import startBackTesting
from pythonProjects.stockProgramV3.tentative_portfolio import tentative_Portfolio
from pythonProjects.stockProgramV3.getHistoricalData import retrieveHistoricalData
from pythonProjects.stockProgramV3.baseClass import stockProgram


def adapterGetData(obj):
    obj.getData()

def interfaceGetData(obj, symbol):
    obj.setSymbol(symbol)
    obj.getData()


def interfaceBackTest(obj, strat, historicalData):
    obj.setStratName(strat)
    #obj.setStrat()
    obj.setHistoricalData(historicalData)
    #obj.getData()

def interfaceCreatePortfolio(obj, fileName):
    obj.setPortfolio()
    obj.savePortfolio(fileName)


def interfaceUpdatePortfolio(obj, fileName, symbol, data, strategy = ""):
    obj.loadPortfolio(fileName)
    obj.setSymbol(symbol)
    if symbol not in obj.portfolio:
        obj.insertNewEntry()

    if type(data) is dict:
        obj.setBasicData(data)

    else:
        obj.setBackTestResults(data, strategy)

    obj.savePortfolio(fileName)

def interfaceLoadPortfolio(obj, fileName):
    obj.loadPortfolio(fileName)
    obj.output()

def main():
    #base = stockProgram()
    scrapper = getBasicStockData()
    backtesting = startBackTesting()
    userPortfolio = tentative_Portfolio()
    histData = retrieveHistoricalData()



    help = "lookup <stock symbol>\n" \
           "description: gets data for selected stock\n\n" \
           "createPortfolio <file name>\n" \
           "description: creates a portfolio\n\n" \
           "backtest <stock symbol> <strategy>\n"\
           "        strategies: SmaCross, Rsi\n"\
           "example: backtest GOOG SmaCross\n"\
           "descrtiption: backtest a stock with strategy\n\n" \
           "update <file name> <stock symbol> <optional: -bd -bt>\n"\
           "        -bd: load basic data for stock into portfolio\n" \
           "        -bt: load backtest results for stock int portfolio\n" \
           "example: update test1 GOOG -bd\n"\
           "example: update test1 GOOG -bt\n"\
           "example: update test1 GOOG -bd -bt\n"\
           "description: add stock data to a portfolio\n\n"\
           "load <file name>\n" \
           "description: loads a portfolio and displays it's contents\n\n" \
           "exit\n" \
           "description: exits program\n\n" \
           "clear\n" \
           "description: clears screen\n"


    while True:
        userInput = ""
        userInput = input("enter command> ")
        cmd = userInput.split()

        if len(cmd) > 6:
            print(f"[!] {str(userInput)} is not a recognized command")
            continue


        if cmd[0] == "lookup":

            #getting basic stock data and historical data
            print("basic data: ")
            interfaceGetData(scrapper, cmd[1])
            print(scrapper)
            print()



        elif cmd[0] == "backtest":
            #conducting back testing
            interfaceGetData(histData, cmd[1])
            interfaceBackTest(backtesting, cmd[2], histData.historicalData)
            adapterGetData(backtesting)
            print("back testing results: ")
            print(backtesting.bt.run())
            print()
            # obj2.bt.plot()
            # obj2.bt.plot()


        elif cmd[0] == "createPortfolio":
            interfaceCreatePortfolio(userPortfolio, cmd[-1])

        elif cmd[0] == "update":

            if "-bd" in cmd and len(scrapper.stockData) > 0:
                interfaceUpdatePortfolio(userPortfolio, cmd[1], cmd[2], scrapper.stockData)

            if "-bt" in cmd:
                interfaceUpdatePortfolio(userPortfolio, cmd[1], cmd[2], backtesting.bt.run(),
                                         backtesting.strategyName)

        elif cmd[0] == "load":
            interfaceLoadPortfolio(userPortfolio, cmd[-1])


        elif cmd[0] == "exit":
            exit()

        elif cmd[0] == 'help':
            print(help)

        elif cmd[0] == 'clear':
            print("\n"*1000)

        else:
            print(f"[!] {userInput} is not a recognized command")

    #print(userPortfolio.portfolio)

if __name__ == '__main__':
    main()


