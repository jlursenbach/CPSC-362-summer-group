from pytickersymbols import PyTickerSymbols


def output(stockList):
    #output stock list
    for i in stockList:
        print(f'Name: {i["name"]}\nSymbol: {i["symbol"]}\n')

def sortList(choice, stockList):
    #sorts list alphabetically by symbol
    if choice == '1':
        stockList = sorted(stockList, key=lambda d: d['symbol'])

    elif choice == '2':
        stockList = sorted(stockList, key=lambda d: d['symbol'], reverse=True)

    return stockList




def main():
    dowJones = PyTickerSymbols()

    #stockList is a list of dicts
    stockList = list(dowJones.get_stocks_by_index('DOW JONES'))
    output(stockList)

    while True:
        usrInput = input("press 1 to sort the list in ascending order\npress 2 to sort the list in descending order\n"
                         "press 3 to leave list unsorted: ")

        if usrInput == '1' or usrInput == '2':
            stockList = sortList(usrInput, stockList)

            #clear screen
            print("\n"*100)
            output(stockList)
            break

        elif usrInput == '3':
            break

        else:
            print("\n"*100)
            print(f"{usrInput} is not an acceptable input")

if __name__ == '__main__':
    main()




