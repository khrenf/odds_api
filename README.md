# odds_api

Backend service for https://www.kobyrenfert.me/calculator
Python + FastAPI framework

Tool for working with betting odds. Takes in American odds ("+155, -145") and returns
the respective probabilities after removing house edge. These are useful for calculating
expected value of a bet. 

The service is hosted on a DigitalOcean Ubuntu virtual machine and a JS+React frontend serves as the client. AWS API Gateaway sits between the front and backend.
