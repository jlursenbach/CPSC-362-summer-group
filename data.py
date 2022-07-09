# We are using a Library called Yahoo_fin
# To install the Yahoo_fin library just run the command:
# pip3 install yahoo_fin

# The method to get this in the Yahoo_fin library is get_data().
from yahoo_fin.stock_info import get_data


#get_data(ticker, start_date = None, end_date = None, index_as_date = True, interval = “1d”)


amazon_weekly= get_data("amzn", start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")
#print(amazon_weekly)

# collect historical data for many tickers 
# create a list of the tickers, an empty dictionary, and 
# iterate through the list appending each pandas dataframe 
# to the empty dictionary:
ticker_list = ["amzn", "aapl", "ba"]
historical_datas = {}
for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker)
print(historical_datas["aapl"])