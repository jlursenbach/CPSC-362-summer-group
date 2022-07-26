
#please make sure to change the path of these if you are running it on your computer
from usingYahooAPI import stockData
from back_testing import startBackTesting
from tentativePortfolio import tentative_Portfolio


def main():
    end = 'y'
    scrapper = stockData()
    userPortfolio = tentative_Portfolio()
    while end == 'y':
        #getting basic stock data and historical data

        scrapper.scrape_stock(input("stock symbol: "))
        #print(scrapper)
        #print(scrapper.historicalData)

        #conduct back testing
        obj2 = startBackTesting()
        obj2.getBackTestingResults(scrapper.historicalData)
        #print(obj2.bt.run())
        #obj2.bt.plot()


        choice = input("Do you wish to create a portfolio? y\\n: ")
        if choice == 'y':
            userPortfolio.buildPortfolio(scrapper.stockSymbol, scrapper.stockData, obj2.bt.run())
            filename = input("save portfolio as: ")
            userPortfolio.savePortfolio(filename)

        elif choice == 'n':
            filename = input("enter portfolio name: ")
            userPortfolio.loadPortfolio(filename)

            choice = input("add another entry?: ")
            if choice == 'y':
                userPortfolio.buildPortfolio(scrapper.stockSymbol, scrapper.stockData, obj2.bt.run())
                userPortfolio.savePortfolio(filename)


        end = input('cont?: ')

    print()
    #userPortfolio.loadPortfolio(filename=input("enter portfolio name: "))
    #print(userPortfolio.portfolio)
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




    #print(userPortfolio.portfolio)




if __name__ == '__main__':
    main()

# test = pd.DataFrame(data=obj1.stockData, index=[0])
# print(test)
# print(obj1.historicalData['Date'])
#print(obj1.historicalData.columns.tolist())
