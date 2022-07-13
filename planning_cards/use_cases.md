# Use Cases


```
{
"ID": UC-1,
"Name": "Return Stock Data",

"Description": "A user inputs valid stock symbol and recieves relevant data for that stock.",

"Primary Actor": "User",

"Preconditions": [
            "User has a stock symbol to supply the system", 
            "User has access to the system",
            "yFinance library is imported and installed on system"
            ],

"Postconditions": [
                "Stock data is retrieved and displayed to the user"
            ],
"Main Success Scenario (flow)": {
                        1: User inputs a valid stock symbol into a text box
                        2: User presses return or selects a button that activates the text box
                        3: The system uses the stock symbol to call yFinance app and return stock data in a JSON
                        4: System will display the stock data
                       }
}
```
