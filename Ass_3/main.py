
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
            #print(scrapper)
            #print(scrapper.historicalData)

            #conduct back testing

            obj2.getBackTestingResults(scrapper.historicalData)
            #print(obj2.bt.run())
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
