#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install yfinance
#!pip install -U pandas==1.3.5

#import yfinance as yf
#import pandas as pd
#import sys
 
#print("Python Version", sys.version)
#print("Yahoo Fianance lib : ", yf.__version__)
#print("Panadas : ", pd.__version__)


# In[2]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime
import statistics


# In[3]:


company='^gspc'
#company='ba'
#company='LMT'
#company='^YH31010010'
data = yf.download(company, start="2021-08-01", end="2024-01-01", auto_adjust=True, interval="1wk")
data


# In[4]:


max_price=data['Close'].max()
min_price=data['Close'].min()

event_data_U=[datetime(2022, 2, 24)]
event_U='2022/02/24\nRussia-Ukraine war'

event_data_GH=[datetime(2023, 10, 7)]
event_GH='2023/10/07\nGaza War'

plt.figure(figsize=(15,10))
plt.title('The effect of Russia-Ukraine and Gaza War on Lockheed Martin Corporation')
plt.xlabel('Date')
plt.ylabel('Price')
Plot_Price=data['Close'].plot()

ssss=Plot_Price.vlines(x=event_data_U, ymin=min_price, ymax=max_price, color='r', linestyle = '--', label=event_U)
Plot_Price.legend(bbox_to_anchor=(1, 1), loc='upper left')

x_pos_list=list(Plot_Price.get_xticks())
x_pos=x_pos_list[2]
Plot_Price.text(x_pos, min_price, event_U, {'color': 'red', 'fontsize': 20})


Plot_Price.vlines(x=event_data_GH, ymin=min_price, ymax=max_price, color='g', linestyle = '--', label=event_GH)
Plot_Price.legend(bbox_to_anchor=(1, 1), loc='upper left')

x_pos_=x_pos_list[8]
Plot_Price.text(x_pos_, min_price, event_GH, {'color': 'green', 'fontsize': 20})

plt.show()


# In[7]:


pip install-U notebook-as-pdf
pyppeteer-install


# In[ ]:




