
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df1 = pd.read_csv('IXIC.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('IXIC')
df2 = pd.read_csv('LMT.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('LMT')
df3 = pd.read_csv('NOC.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('NOC')
df4 = pd.read_csv('RTX.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('RTX')


combined_df = pd.concat([df1, df2, df3, df4], axis=1)

correlation_matrix = combined_df.corr()


plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)


plt.title('Stock Correlation Heatmap')

heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, horizontalalignment='right')
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=45)


plt.show()




