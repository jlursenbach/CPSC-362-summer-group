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
	1.) Generate a list of stocks
	2.) Sort the list
	3.) Filter the list
	     - we need to decide what to sort & filter by 
	4.) Select specific stock from the list
	5.) View stock data 
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
	6.) scrape a list of stocks from - somewhere - (Yahoo finance?)
	7.) grab stock data from - somewhere - (Yahoo finance?)
		 - is there a REST API for this?
		  - https://algotrading101.com/learn/yahoo-finance-api-guide/
	8.) put the data into .json or py-dict
	9.) figure out an interactive display system for stock data	
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
 	Handle multiple users accessing system



## Use Cases
[Use Cases Link](https://github.com/jlursenbach/CPSC-362-summer-group/blob/4-assignment-1/use_cases.md)

UC-01         |  UC-02
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091324-204140ee-f2b4-48c7-98b0-066e475674e0.png" width="600">]() |  [<img src="" width="600">]()



UC-03        |  UC-04
:-------------------------:|:-------------------------:
 [<img src="" width="600">]() |  [<img src="https://user-images.githubusercontent.com/61986930/178091335-f3c88dbc-72c6-4a37-9d6f-51668f6d486a.png" width="600">]()



UC-05        |  DC-06
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091338-a0dd40a2-57e6-43a4-b290-9402fe9420d0.png" width="600">]() |  [<img src="" width="600">]()



DC-07         |  DC-08
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091344-a42be2b0-cff1-436a-becf-35005db22003.png" width="600">]() |  [<img src="" width="600">]()



DC-09        |  -
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091351-3b625ee7-e229-4c73-88c9-e288c6185b4d.png" width="600">]() |  -


## User Stories
[User Stories Link](https://github.com/jlursenbach/CPSC-362-summer-group/blob/4-assignment-1/user-stories.md)

UC-01         |  UC-02
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091357-c5d39a2b-9a9c-4e2a-a84c-d4775c12b988.png" width="400">]() |  [<img src="" width="600">]()


UC-03         |  UC-04
:-------------------------:|:-------------------------:
[<img src="" width="600">]() |  [<img src="https://user-images.githubusercontent.com/61986930/178091361-49375536-d6d3-4ec8-a400-22727c95e14c.png" width="400">]()


UC-05         |  UC-06
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091367-e98c4c57-4f95-4149-8838-5df8c4de1c9c.png" width="400">]() |  [<img src="" width="600">]()


UC-07         |  UC-08
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091374-8fd69928-632e-46be-8cd9-80d43d7ad626.png" width="400">]() |  [<img src="" width="600">]()


UC-09         |  UC-02
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/61986930/178091380-9d60232a-1cfe-4236-9862-5aa5e9dcb204.png" width="400">]() |  [<img src="" width="600">]()

