# Use Cases


```
{
  "ID":"UC-1",
  "Name": "Generate a List of Stocks",
  "Description": "User is provided with a complete list of stocks available on the Down Jones Index",
  "Primary Actor": "User",
  "Preconditions": ["User has access to the page", 
                    "User chooses to display the list of stocks by selecting button or opening page"],
  "Postconditions": ["Visually populate a complete visual list of available stocks",
                     "Manipulatable",
                     "Selectable"],
  "Main Success Scenario": {1: "User opens page or clicks "populate list" button",
                            2: "User is provided a complete list of stocks to look through"}
}

{
"ID": "UC-4",
"Name": "select specific stock from the list",
"Description: "The user will select a stock, the data for that stock will be returned.",
"Primary Actor: "User",
"Preconditions: ["user has a list of stocks to choose from",
                 "(optional) user could filter stocks to aid in choice",
                 (optional) user could sort stocks to aid in choice],
"Postconditions: ["stock data is displayed to user"],
"Main Success Scenario (flow)": {1: "user looks through a list of stocks",
                                 2: "user selects a stock (text link or check box?)",
                                 3: "data for stock is returned in (drop-down, pop-up, new page, different frame?)"} 
}

{
"ID": "UC-5",
"Name": "Viewing Stock Data",
"Description": "Upon selecting a stock, the user is able to view data related to the stock",
"Primary Actor": "User",
"Pre-condition": ["Stocks have been retrieved and displayed to user",
                  "User has selected a stock",
                  "developer has retrieved data for individual stocks"
                  "a data output format has been decided on"],
"Post condtion": ["User is able to view data related to the selected stock"],
"Main success scenario (flow)": {1: "User selects a stock from a list of stocks", 
                                 2: "system displays data related to selected stock"}
}

```

# Developer Use Cases
```

{
"ID": "DC-7",
"Name": "get stock data from yahoo finance",
"Description: "The developer will get stock data from yahoo finance by using the yfinance python module.",
"Primary Actor: "Developer",
"Preconditions: "yfinance is imported",
"Postconditions: "stock data is retrieved",
"Main Success Scenario (flow)": {1: "requiest for stock data sent to yFinance with Rest API",
                                 2: "data is returned in a json, .csv, or pydict",
                                 3: "data is placed into the webpage or a temporary database for viewing or access"} 
}

{
"ID": "DC-9",
"Name": "Interactive Display System for Stock Data",
"Description": The developer creates an interactive display system for Stock Data for the user",
"Primary Actor": "Developer"
"Preconditions": ["Stock data is retrieved"],
"Postconditions": ["Configuration of interactive display system for user"],
"Main success scenario" : {1: "Chosen stock data is chosen to be implemented", 
                           2: "The system configures a display system for chosen stock data", 
                           3: Display system becomes available for user to interact with"}
}
```
