## Class: GetStockData

### Description: 
This class takes a stock symbol as a parameter. It will then retrieve detailed information about the stock from yahoo finance and display it to the user. 

### Responsibilities:
1. Get stock data from yahoo finance
2. store data in JSON
3. display data to user??

### Collaborators:
1. BackTesting
2. CreateTentativePortfolio


## Class: BackTesting

### Description: 
This class will conduct backtesting based on the given stock and strategy the user chooses. Afterwards, it will display the results to the user.


### Responsibilities:
1. Allows the user to select a stock.
2. Display buy and sell strategies for the use to choose
3. Allows the user to click a button to start backtesting
4. conducts backtesting on the selected stock
5. Display backtesting result to the user

### Collaborators:
1. GetStockData
2. CreateTentativePortfolio


## Class CreateTentativePortfolio

### Description: 
This class will allow the user to create a tentative portfolio where the user can store their selected stocks along with their corresponding buy and sell strategies.

### Responsibilities:
1. Take user input to create a portfolio
2. Define an empty data structure that will serve as the portfolio
3. Store user-selected stock, and corresponding data inside portfolio
4. save portfolio so that it can be read and retrieved

### Collaborators:
1. BackTesting
2. GetStockData
