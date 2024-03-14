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
First we need to go to ShayaunB_MiddleE_andStockPrice.zip to download the dataset from Middle East then, to use the conflict index data set in the zip its compressed using RAR so please use winRAR or something like that to extract it and also put other csv file in our data folder into the same folder with the main notebook file. Then we can open our notebook file and run every cell in the code. 

If you want to use ShayaunB_MiddleE_andStockPrice.zip please unzip and then there will be all the csv and python code, to use the conflict index data set in the zip its compressed using RAR so please use winRAR or something like that to extract it. Once You have the folder ready it is plug and play. Be sure to real docstrign for what each function produces as well as the code with only show one graph at a time and pause there so for the code to continue you must close that graph and it will autmotically move on. Conflict index event data set is large so it takes a few seconds for the code to generate the graph. 

If you want to use LSTM to predict stock data, you need to enter the FinalProj-Qiuyi Yang folder, download the RTX_new.csv file, ensure that the Pytorch environment is installed in the system, and then run the LSTM.py file to obtain prediction results. You can adjust the length of input data and parameters of the LSTM network to obtain different prediction results. Multiple adjustments of parameters may lead to more satisfactory results.
