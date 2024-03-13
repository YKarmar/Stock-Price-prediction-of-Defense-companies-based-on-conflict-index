# Stock-Price-prediction-of-Defense-companies-based-on-conflict-index
The Topic that our team chose is “Stock Price prediction of Defense companies based on conflict index” using ACLED Conflict index. For example using this data set we can track Drone strikes happening in the middle east and if the amount of drone strikes increases we can see if it correlates to stock price. We could also track event types that usually lead to drone strike increase and predict stock price from that. 

# Overview of the Repo
There are two main folders of our repo. One of them is regarding the analysis on the middle east conflict dataset and the second one is regarding the analysis on the stock price on the defense companies.

# Third Party Model
In this project we used Panda, Numpy, yfinance,seaborn and also pytorch

# Dataset
The dataset that we are using are from https://acleddata.com/curated-data-files/ and also the stock data set are from Yahoo https://finance.yahoo.com/quote/LMT

# File Structure
1. The first part of our notebook file is to Analysis how the stock price of has been affect during the War period in Russian this include the stock price for different induristires relate the the defense companies such as Meta Farbrication, Farm Heavery construction and so on.
2. The second part of our notebook is to compare the performance of the stock with S&P 500 to shows that while most companies are affected by the war but these defense relate companies were not
3. Then the third part we will start analysis the middle east conflict index and find a time that has suddent increase in number of the conflict event
4. After that we will run into specific type of event that will affect the stock the most
5. Since we only analysis on one companies the LMT we will find out how LMT relate to other companies so we can also have a analysis on other companies relate to the conflict index.
6. Finally we make our conclusion that the conflict indenese will have a positive relationship with the defense companies.

# How to run our code
First we need to go to https://acleddata.com/curated-data-files/ to download the dataset from Middle East and also other csv file in our data folder. Then we can open our notebook file and run every cell in the code.
