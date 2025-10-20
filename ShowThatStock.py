#imports the things neccessary to graph and retrieve data, using the API Yfinance
import time
import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt

#A dictionary that translates what the user would think to type into the actual values that yfinance actually accepts
how_long_dict = {
    "1 day": '1d',
    "5 days": '5d',
    "1 month": '1mo',
    "3 months": '3mo',
    "6 months": '6mo',
    "1 year": '1y',
    "2 years": '2y',
    "5 years": '5y',
    "10 years": '10y', 
    "Year to date": 'ytd',
    "Max": "max"
}
#Asks how many stocks the user wants to see
how_many = int(input("How many stocks would you like to look at? "))
for num in range(how_many):

#Asks what stocks the user wants to see, and the history that they want to see it
    what_stock = input("What stock do you want to see? ")
    how_long = input("How much of the stock history do you want to be able to see? ")

#makes the Ticker value what stock the user wants to see
    
    actual_val_of_data = how_long_dict[how_long]

    #makes the code go zzzzzzzz....
    time.sleep(5)
#Translates the history of the data the user wants to see to the value that yfinance actually takes in
    hist = yf.download(tickers=what_stock, period=actual_val_of_data)

#loops through how long history is, and assigns all values to the variable df
    df = hist

#accesses the dataframe, using the closing price of the stock, and distplays the plot with a title of 'THE STOCK Stock Prices Over Time'
    df[['High']].plot(title=f'{what_stock.upper()} Stock Prices Over Time')

#makes the actual graph itself, making the x label 'Date', the y label 'Close Price' making a grid, and then finally plotting it

    plt.xlabel('Date')
    plt.ylabel('High Price')
    plt.grid(True)
    plt.show()

