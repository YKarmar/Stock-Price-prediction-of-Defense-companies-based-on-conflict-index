# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df1 = pd.read_csv('IXIC.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('IXIC')
df2 = pd.read_csv('LMT.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('LMT')
df3 = pd.read_csv('NOC.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('NOC')
df4 = pd.read_csv('RTX.csv', index_col='Date', parse_dates=True)['Adj Close'].rename('RTX')

combined_df = pd.concat([df1, df2, df3, df4], axis=1)

# %%
# 使用Seaborn绘制箱线图
plt.figure(figsize=(12, 8))  # 设置图形的尺寸
sns.boxplot(data=combined_df)  # 绘制箱线图

plt.xticks(rotation=45)  # 旋转X轴的标签，以便更好地显示
plt.title('Stock Price Distribution')  # 设置图形的标题
plt.ylabel('Price')  # 设置Y轴的标签
plt.show()


# %%



