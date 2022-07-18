# user cases

## ID: DC-1

### name: 
Return Stock Data

### description: 
The user supplies the system a valid stock symbol, upon which the system returns data for the given stock

### Primary Actor: 
User

### preconditions: 
1. User has a stock symbol to supply to the system
2. User has access to the system
3. yfinance module is imported on the system

### postconditions: 
stock data is retrieved and displayed for the user

### main success scenario:
1. User inputs a valid stock symbol
2. The system uses the stock symbol to retrieve stock data from yahoo finance
3. the system will display the stock data for the user


## ID: DC-2

### name: 
Get back testing results

### Description: 
After the user selects a stock for analysis. The system will provide a list of buy and sell strategies for the user to choose. Afterwards, the system will conduct back testing based on the stock and strategy the user chose and display the results to the user.


### Primary actor: 
user

### Pre-conditions: 
user has selected a stock for analysis

### Post conditions: 
User chooses buy and sell strategies provided by the system.

### Main success scenario: 
1. The system allows the user to select a stock.
2. The system will then display the buy and sell strategies to the user to select.
3. User will click the button to start back testing.
4. system will conduct back testing
5. System will display backtesting results to the user




## ID: DC-3

### name: 
create tentative portfolio

### description: 
The user creates a tentative portfolio containing stocks they have selected along with their corresponding buy and sell strategies.
#
## Primary actor: 
user

### pre-conditions: 
User has selected a stock for analysis, as well as choosing a buy and sell strategy for that stock that was provided by the system.

### post conditions: 
The user is able to store the selected stock and strategy inside a portfolio.

### Main success scenario:
1. User selects an option to create a tentative portfolio
2. The system will create an empty portfolio
3. User chooses stocks, backtesting results, and strategy name to store inside the portfolio
4. The system will store the selected stocks and corresponding data inside the portfolio
5. system will save the portfolio that can be retrieved by both system and user.



# user stories

### ID: BC-1

### name: 
Return Stock Data

### Actor:
user

### description: 
User inputs valid stock symbol, the system will then gather data from yahoo finance corresponding to the given stock and display the data for the user.


## ID: BC-2

### name: 
Get Back Testing Results

### actor: 
user

### description: 
The system will conduct backtesting on the given stock and strategy that the user chose. The results will be displayed for the user.


## ID: BC-3

### name: 
create tentative portfolio

### actor: 
user

### description: 
The user creates a tentative portfolio containing stocks they have selected along with their corresponding buy and sell strategies.
