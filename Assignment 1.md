# Assignment #1
Total score: 30
Due date: 7/10
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
	Generate a list of stocks
	Sort the list
	Filter the list
	     - we need to decide what to sort & filter by 
	Select specific stock from the list
	View stock data 
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
	scrape a list of stocks from - somewhere - (Yahoo finance?)
	grab stock data from - somewhere - (Yahoo finance?)
		 - is there a REST API for this?
		  - https://algotrading101.com/learn/yahoo-finance-api-guide/
	put the data into .json or py-dict
	figure out an interactive display system for stock data	
		- display info from a py-dict or .json
		- create a number of frames
		- display info in a respective frame
		- scroll, filter, select
		
## Nonfunctional Requirements: 

## User
	Load the list within 3 seconds
	return a complete list (no parts missing)
	provide accurate data
	readability/understandability/organization
	
## Developer
 	Handle multiple users accessing system

	

