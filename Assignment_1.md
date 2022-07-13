# Assignment #1
Total score: 30
Due date: 7/10

## TEAM:
```
Olvin Bolanos
Anthony Cao
Thomas Tran
Jacob Ursenbach
Greg Zhang
```

## Goals

Analyzing customer requirements. Writing requirements for the users and developers using both
use case and user story format.

### Requirements for this assignment

One of the features of the portfolio management system: 

**feature #1, is “Customers select a stock from the Dow Jones index for detailed information about the stock for analysis.”.** 

1. Analyze the features and identify all the requirements to implement this feature, 
	such as:
	1) getting stock data (e.g., from Yahoo Finance), 
	2) finding out a list of stocks in Dow Jones, and detailed information 
	 	(e.g., Open, Close, Bid, Ask, Volume, PE ratio, EPS, analyst’s recommendation) 
	4) allowing customers to choose a stock to display the detailed information, etc.

2. Write all the necessary use cases AND user stories to implement the feature (a) of the
system.

### Acceptance criteria

A list of all the necessary use cases and user stories in the format discussed in class that meet the
requirements of the feature #1 for both the user and developers to implement it.
Note: Please expect that the user requirements can be changed as you go
through the project life cycle.

# TASK:

| note: (we need to run our assignment through prof. before submission. I am listening to him pull apart people's ideas.
> **“Customers select a stock from the Dow Jones index for detailed information about the stock for analysis.”.** 

# Requrements: 

<!--- 
comment block (not visible in final document)

--->

## Functional Requirements: 
	
### USER:
	1.) Supply a stock symbol
	2.) View stock data 
		- the product that the company sells
		- product popularity (consumer needs)
		- stock price trend chart 
		       (chart should show company performance up to 5 years)
		- opening and closing prices
		- PE ratio (price per earning)
		- PS ratio (price per share)
		- company cash reserve
		- company debt
		- company management effectiveness data 
				(return on asset and return on equity data)

### DEVELOPER:
	3.) Get stock data from yFinance
	  	- is there a REST API for this?
  		- https://algotrading101.com/learn/yahoo-finance-api-guide/
	4.) Display the stock data
		- display info from a py-dict or .json
		- create a number of frames
		- display info in a respective frame
		- scroll, filter, select
		
## Nonfunctional Requirements: 
> not required for this assignment

### User
	Load the list within 3 seconds
	return a complete list (no parts missing)
	provide accurate data
	readability/understandability/organization
	
### Developer
```
```


## Use Cases
![image](https://user-images.githubusercontent.com/61986930/178638910-8f879175-a7d4-49ae-b1f7-d8ecb4984b42.png)


## User Stories

![image](https://user-images.githubusercontent.com/61986930/178638942-8f6a8ecc-bbac-490b-8fb2-2707019baaab.png)


