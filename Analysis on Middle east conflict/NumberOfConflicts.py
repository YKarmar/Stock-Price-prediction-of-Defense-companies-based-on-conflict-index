#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from datetime import datetime
import statistics
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


path = r"C:\Users\fardin\Desktop\\{}"
results = pd.read_excel (path.format('paniz_data.xlsx'),index_col=0)


# In[3]:


fig, ax = plt.subplots(figsize=(15,10))
ax.set_title('Interstate conflicts data')

sns.heatmap(results, annot=True,fmt='g')


# In[ ]:




