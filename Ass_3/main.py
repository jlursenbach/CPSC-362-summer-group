
#please make sure to change the path of these if you are running it on your computer
from pythonProjects.stockProgram.usingYahooApi import stockData
from pythonProjects.stockProgram.back_testing import startBackTesting


def main():

    #getting basic stock data and historical data
    scrapper = stockData()
    scrapper.scrape_stock("ATVI")
    #print(scrapper)
    #print(scrapper.historicalData)

    #conduct back testing
    obj2 = startBackTesting()
    obj2.getBackTestingResults(scrapper.historicalData)
    print(obj2.bt.run())
    obj2.bt.plot()




if __name__ == '__main__':
    main()

# test = pd.DataFrame(data=obj1.stockData, index=[0])
# print(test)
# print(obj1.historicalData['Date'])
#print(obj1.historicalData.columns.tolist())