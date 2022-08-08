# Assignment 5

Coding Team:
• Anthony Cao -
• Greg Zhang - 
• Jacob Ursenbach - 
• Olvin Bolanos  - 
• Thomas Tran -

### GitHub Repo:
[https://github.com/jlursenbach/CPSC-362-summer-group](https://github.com/jlursenbach/CPSC-362-summer-group)
### Zip of the program
[stock_program.zip](Assignment%205%20276e5293852c4b55b3fa9c0fc76a9f5c/stock_program.zip)

# Portfolio Demo:
[![image](https://user-images.githubusercontent.com/61986930/183350232-49a00b9f-d920-4e93-a796-046301de7ce8.png)](https://www.youtube.com/watch?v=XziPngL4h6o)

# 1: Apply Adapter, Decorator, and Strategy design patterns.

## Decorator:

> Professor reviewed and approved the decorator pattern in class
> 

```python
#this was confirmed by the professor that it was implemented correctly
def decoratorGetData(method):
    def wrapper(self):
        if self.strategyName == "SmaCross":
            self.strategy = SmaCross

        elif self.strategyName == "Rsi":
            self.strategy = rsiOscillator

        elif self.strategyName == "DCA":
            self.strategy = DCA
            self.historicalData = self.historicalData * (10 ** -6)

        method(self)

    return wrapper
```

## Strategy:

> Professor reviewed and approved the strategy pattern in class
> 

```python
"""Backtesting.py which is a module we used has already implemented
the strategy design pattern. The class called Strategy is the 
common interface that is used by the other strategy classes

An indicator that we did use the strategy pattern is that we passed
our strategy classes as a parameter in the Backtest() 

self.strategy is a variable tha contains the strategy classes that we can pass to backtest
for example self.strategy = SmaCross

self.bt = Backtest(self.historicalData, self.strategy, cash = self.cashAmount, commission=0.002,
                           exclusive_orders=True)"""

#strategy class
class SmaCross(Strategy):
    """simple moving average crossover strat"""
    n1 = 50
    n2 = 100

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

#strategy class
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

"""def decoratorInputAmountToInvest(method):
    def wrapper(self):
        self.amountToInvest = int(input("input amount to invest: "))

        method(self)

    return wrapper"""

#strategy class
class DCA(Strategy):

    amountToInvest = 10
    #@decoratorInputAmountToInvest
    def init(self):

        self.dayOfTheWeek = self.I(lambda x: x, self.data.Close.s.index.dayofweek)

    def next(self):

        if self.dayOfTheWeek[-1] == 1:
            self.buy(size = math.floor(self.amountToInvest / self.data.Close[-1]))
```

## Adapter Pattern:

> Professor reviewed and approved the adapter pattern in class
> 

```python
#we demo'd our adapter pattern in class and you aprroved of it
#adaptees using this adapter are pullBasicStockData and getHistoricalData
#this adapter gets called in the view class method interfaceGetData
class getDataAdapter:
    def __init__(self, **adaptedMethod):
        self.__dict__.update(adaptedMethod)

class View:
    def __init__(self):
        pass
    def interfaceGetData(self, obj, symbol):
        obj.setSymbol(symbol)
        getDataAdapter(data=obj.getData())
```

# 2: Apply one suitable architectural pattern, e.g., Model-View-Controller (MVC) pattern or layered architecture pattern. Note that although the View in MVC is naturally implemented with a graphical user interface (GUI), it does not mean the View is GUI. You can implement MVC without a GUI.

```jsx
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
        print(obj)

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
```

# 3: Test each of the relevant SOLID design principles to your program and explain whether the design and architecture of your program conforms to the design principles.

- S - Single Responsibility
    - Yes it conforms to Single responsibility
    Every class has just one job.
    The class backtesting is solely responsible for conducting the backtesting and returning the results
    Getting historical data is responsible for getting the data and nothing else
    Pull basic stock data gets the data and does nothing else
    Tentative_portfolio creates and manages portfolios
- O - Open Closed
    - We wrote the code so that it was open to extension but closed to modification
    - This was implemented by using interface methods
    - new features can be implemented without having to modify any of our classes by simply writing a new class that can use our interface methods. The only class you would modify would be the views class if you wish to add more interface methods.
- L - Liskov substitution
    - Interface classes were not needed, as simple interface functions were good enough to implement this design principle
    - We implemented the relevant interface function for every class
- I - Interface segregation
    - This has been implemented through our production of client-specific interfaces
    - We did not use one general purpose interface
- D - Dependency Inversion
    - Each Class was written to be a self-contained module, which does not rely on lower-level module code. The Dependency inversion principle was satisfied through this abstraction.
    - Every module was written to act totally independently, and they interact through interface functions. The higher level modules like backtesting, use abstractions and do not rely on any code from the lower level modules. The only exception is our viewer class and controller class which do depend on each other.
    
    # 4: Conduct the refactoring practice by going through the above activities 1 - 3 and show the
    improved codes before and after. Was your original OO design from CRC modeling (the
    class design done in assignment #2) correct? If incorrect, briefly explain the problem of the
    original OO design and how you improved it.
    
    ## a:  Refactor code. Show before and after code:
    
    ### i: Before Code:
    
    ```python
    #please make sure to change the path of these if you are running it on your computer
    from pythonProjects.stockProgram.usingYahooApi import stockData
    from pythonProjects.stockProgram.back_testing import startBackTesting
    from pythonProjects.stockProgram.tentativePortfolio import tentative_Portfolio
    
    def main():
        scrapper = stockData()
        userPortfolio = tentative_Portfolio()
        obj2 = startBackTesting()
    
        help = "lookup <stock symbol>           gets data for selected stock\n" \
               "createPortfolio <file name>     creates a portfolio\n" \
               "update <file name>              add stock data to a portfolio after lookup\n" \
               "load <file name>                loads a portfolio and displays it's contents\n" \
               "exit                            exits program\n" \
               "clear                           clears screen\n"
    
        while True:
            userInput = ""
            userInput = input("enter command> ")
            cmd = userInput.split()
    
            if len(cmd) > 2:
                print(f"[!] {str(userInput)} is not a recognized command")
                continue
    
            if cmd[0] == "lookup":
    
                #getting basic stock data and historical data
    
                scrapper.scrape_stock(cmd[-1])
                print("basic data: ")
                print(scrapper)
                print()
                #print(scrapper.historicalData)
    
                #conduct back testing
                choice = input("select a backtesting strategy: ")
                obj2.getBackTestingResults(scrapper.historicalData)
                print("back testing results: ")
                print(obj2.bt.run())
                print()
                #obj2.bt.plot()
    
            elif cmd[0] == "createPortfolio":
                userPortfolio.setPortfolio()
                filename = cmd[-1]
                userPortfolio.savePortfolio(filename)
    
            elif cmd[0] == "update":
                if scrapper.stockSymbol == "":
                    print("[!] error: a stock has not been selected for analysis yet")
                    continue
                userPortfolio.loadPortfolio(cmd[-1])
                userPortfolio.buildPortfolio(scrapper.stockSymbol, scrapper.stockData, obj2.bt.run())
                userPortfolio.savePortfolio(cmd[-1])
                print(f"[+] {scrapper.stockSymbol} stock data has been added to {cmd[-1]}")
    
            elif cmd[0] == "load":
                userPortfolio.loadPortfolio(cmd[-1])
                for key, value in userPortfolio.portfolio.items():
                    print(f"stock: {key}\n")
                    for key2, value2 in value.items():
                        if type(value2) is dict:
                            print(f'{key2}: ')
                            for key3, value3 in value2.items():
                                print(f'{key3}: {value3}')
    
                            print()
    
                        else:
                            print(f'{key2}: ')
                            print(value2)
                            print()
                    print("---------------------------------------------------------")
    
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
    
    # test = pd.DataFrame(data=obj1.stockData, index=[0])
    # print(test)
    # print(obj1.historicalData['Date'])
    #print(obj1.historicalData.columns.tolist())
    
    """Opening Price: 154.01
    Closing Price: 154.09
    PE_ratio: 24.87
    PS_ratio: 6.62
    Company_Cash_Reserve: 51511001088
    Company_Debt: 119980998656
    bid: 152.56 x 900
    volume: 53623945.0
    ask: 152.60 x 1000"""
    ```
    
    ### ii: After Code:
    
    ```python
    from pythonProjects.stockProgramV4.pullBasicStockData import GetBasicStockData
    from pythonProjects.stockProgramV4.back_testing import StartBackTesting
    from pythonProjects.stockProgramV4.tentative_portfolio import Tentative_Portfolio
    from pythonProjects.stockProgramV4.getHistoricalData import RetrieveHistoricalData
    from pythonProjects.stockProgramV4.returnJson import convertToJson
    from pythonProjects.stockProgramV3.baseClass import stockProgram
    
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
            print(obj)
    
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
    ```
    
    ## b: Was the original OO design from CRC modeling correct?
    
    ### Original CRC model:
    
    ![Untitled](Assignment%205%20276e5293852c4b55b3fa9c0fc76a9f5c/Untitled.png)
    
    Our original CRC model did not take into account ease of maintenance and extendibility. Adding new features such as getting historical data would require directly modifying one of our classes. Our improved code added interface functions so that our program now adhered to the OCP design principles. Adding new features became much simpler as we would not have to modify any of our existing classes, instead, we could just write a new class that would use our interface functions. Additionally, our classes are no longer directly dependent on one another. Instead, our classes are now dependent on the interface functions.
    
    # 5:  Practice continuous integration by showing working features from the integrated modules
    and demo the completed application.
    
    # Acceptance criteria
    
    - Evidence of refactoring, continuous integration, and continuous deployment
    
    ## Evidence of refactoring:
    
    ### Before Code:
    
    ```r
    #please make sure to change the path of these if you are running it on your computer
    from pythonProjects.stockProgramV2.pullStockData import stockData
    from pythonProjects.stockProgramV2.back_testing import startBackTesting
    from pythonProjects.stockProgramV2.tentative_portfolio import tentative_Portfolio
    
    def main():
        scrapper = stockData()
        userPortfolio = tentative_Portfolio()
        obj2 = startBackTesting()
    
        help = "lookup <stock symbol>           gets data for selected stock\n" \
               "createPortfolio <file name>     creates a portfolio\n" \
               "update <file name>              add stock data to a portfolio after lookup\n" \
               "load <file name>                loads a portfolio and displays it's contents\n" \
               "exit                            exits program\n" \
               "clear                           clears screen\n"
    
        while True:
            userInput = ""
            userInput = input("enter command> ")
            cmd = userInput.split()
    
            if len(cmd) > 6:
                print(f"[!] {str(userInput)} is not a recognized command")
                continue
    
            if cmd[0] == "lookup":
    
                #getting basic stock data and historical data
    
                scrapper.scrape_stock(cmd[-1])
                print("basic data: ")
                print(scrapper)
                print()
                #print(scrapper.historicalData)
    
            elif cmd[0] == "backtest":
                #conducting back testing
                obj2.retrieveHistoricalData(cmd[1])
                obj2.setStrategyName(cmd[2])
                obj2.getBackTestingResults()
                print("back testing results: ")
                print(obj2.bt.run())
                print()
                # obj2.bt.plot()
                # obj2.bt.plot()
    
            elif cmd[0] == "createPortfolio":
                userPortfolio.setPortfolio()
                filename = cmd[-1]
                userPortfolio.savePortfolio(filename)
    
            elif cmd[0] == "update":
    
                userPortfolio.loadPortfolio(cmd[1])
                if cmd[2] not in userPortfolio.portfolio:
                    userPortfolio.buildPortfolio(cmd[2])
    
                if "-bd" in cmd and len(scrapper.stockData) > 0:
                    userPortfolio.setBasicData(cmd[2], scrapper.stockData)
    
                if "-bt" in cmd:
                    userPortfolio.setBackTestResults(cmd[2], obj2.bt.run(), obj2.strategyName)
    
                userPortfolio.savePortfolio(cmd[1])
                print(f"[+] {cmd[2]} stock data has been added to {cmd[1]}")
    
            elif cmd[0] == "load":
                userPortfolio.loadPortfolio(cmd[-1])
                for key, value in userPortfolio.portfolio.items():
                    print(f"stock: {key}\n")
                    for key2, value2 in value.items():
                        if type(value2) is dict:
                            print(f'{key2}: ')
                            for key3, value3 in value2.items():
                                print(f'{key3}: {value3}')
    
                            print()
    
                        else:
                            print(f'{key2}: ')
                            print(value2)
                            print()
                    print("---------------------------------------------------------")
    
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
    
    # test = pd.DataFrame(data=obj1.stockData, index=[0])
    # print(test)
    # print(obj1.historicalData['Date'])
    #print(obj1.historicalData.columns.tolist())
    
    """Opening Price: 154.01
    Closing Price: 154.09
    PE_ratio: 24.87
    PS_ratio: 6.62
    Company_Cash_Reserve: 51511001088
    Company_Debt: 119980998656
    bid: 152.56 x 900
    volume: 53623945.0
    ask: 152.60 x 1000"""
    ```
    
    ### After Code
    
    ```r
    from pythonProjects.stockProgramV4.pullBasicStockData import GetBasicStockData
    from pythonProjects.stockProgramV4.back_testing import StartBackTesting
    from pythonProjects.stockProgramV4.tentative_portfolio import Tentative_Portfolio
    from pythonProjects.stockProgramV4.getHistoricalData import RetrieveHistoricalData
    from pythonProjects.stockProgramV4.returnJson import convertToJson
    
    from pythonProjects.stockProgramV3.baseClass import stockProgram
    
    #we demo'd our adapter pattern in class and you aprroved of it
    #adaptees using this adapter are pullBasicStockData and getHistoricalData
    #this adapter gets called in the view class method interfaceGetData
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
    ```
    
    ## Continuous Integration & Continuous Deployment:
    
    ![Untitled](Assignment%205%20276e5293852c4b55b3fa9c0fc76a9f5c/Untitled%201.png)
    
    ## Proper applications of design principles, design patterns, and an architectural pattern
    
    - These were discussed in detail in the above sections
