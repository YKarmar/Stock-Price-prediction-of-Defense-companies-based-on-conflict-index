
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('event_data.xlsx')



data = {}
for i in range (1997,2025):
    data[i]=0




for i in range(len(df['Year'])):
    data[df['Year'][i]] += 1


keys = list(data.keys())
values = list(data.values())
    
plt.bar(keys, values)
plt.xlabel('Count')
plt.ylabel('Year')
plt.title('Polictical violence by year')
plt.show()



import seaborn as sns



months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



month = {}
for i in range (1997,2025):
    for x in months:
        month[(i,x)]=0



for i in range(len(df['Year'])):
    month[(df['Year'][i],df['Month'][i])] += df['Events'][i]



months = [key[1] for key in month.keys()]
event_counts = list(month.values())

# Plotting the bar plot
plt.figure(figsize=(10, 6))
plt.bar(months, event_counts, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Number of Events')
plt.title('Events per Month')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# # violence in Middle East
# 


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('middle.xlsx')



EType={}



yr = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]



name = []




for x in df['SUB_EVENT_TYPE']:
    if x not in name:
        name.append(x)
    for i in yr:
        EType[(x,i)]= 0


# In[53]:


for i in range (len(df['SUB_EVENT_TYPE'])):
    EType[(df['SUB_EVENT_TYPE'][i],df['YEAR'][i])] += 1



import numpy as np



ye = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
event_matrix = np.zeros((24,len(ye)))
for j in range(len(ye)):
    for i in range(24):
        event_matrix[i, j] = EType[(name[i],ye[j])]



import seaborn as sns



plt.figure(figsize=(11, 8))
sns.heatmap(event_matrix, annot=True, fmt='g',
            xticklabels=ye, yticklabels=name)
plt.xlabel('Year')
plt.ylabel('Event Type')
plt.title('Event Count Heatmap')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




attack = {}
for y in ye:
    attack[y] = 0




for i in range(len(df['SUB_EVENT_TYPE'])):
    if (df['SUB_EVENT_TYPE'][i] == 'Attack'):
        attack[df['YEAR'][i]] +=1



keys = list(attack.keys())
values = list(attack.values())

# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Year')
plt.ylabel('Event count')
plt.title('Attack count by years')
plt.show()


# In[61]:


months = [1,2,3,4,5,6,7,8,9,10,11,12]




from datetime import datetime




attack2023 = {}
for m in months:
    attack2023[m] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if(df['YEAR'][i]==2023 and df['SUB_EVENT_TYPE'][i] == 'Attack'):
        date_string = df['EVENT_DATE'][i]
        month_as_int = date_string.month
        attack2023[month_as_int] +=1

keys = list(attack2023.keys())
values = list(attack2023.values())

# Plotting
# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Month')
plt.ylabel('Event count')
plt.title('Attack in 2023')
plt.show()




Armed = {}
for y in ye:
    Armed[y] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if (df['SUB_EVENT_TYPE'][i] == 'Armed clash'):
        Armed[df['YEAR'][i]] +=1




keys = list(Armed.keys())
values = list(Armed.values())

# Plotting
plt.bar(keys, values)
plt.xlabel('years')
plt.ylabel('Event count')
plt.title('Armed clash count')
plt.show()



Armed2017 = {}
for m in months:
    Armed2017[m] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if(df['YEAR'][i]==2017 and df['SUB_EVENT_TYPE'][i] == 'Armed clash'):
        date_string = df['EVENT_DATE'][i]
        month_as_int = date_string.month
        Armed2017[month_as_int] +=1

keys = list(Armed2017.keys())
values = list(Armed2017.values())

# Plotting
# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Months')
plt.ylabel('Event count')
plt.title('Armed clash in 2017')
plt.show()



Armed2018 = {}
for m in months:
    Armed2018[m] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if(df['YEAR'][i]==2018 and df['SUB_EVENT_TYPE'][i] == 'Armed clash'):
        date_string = df['EVENT_DATE'][i]
        month_as_int = date_string.month
        Armed2018[month_as_int] +=1

keys = list(Armed2018.keys())
values = list(Armed2018.values())

# Plotting
# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Months')
plt.ylabel('Event count')
plt.title('Armed clash in 2018')
plt.show()



Violent = {}
for y in ye:
    Violent[y] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if (df['SUB_EVENT_TYPE'][i] == 'Violent demonstration'):
        Violent[df['YEAR'][i]] +=1
        
keys = list(Violent.keys())
values = list(Violent.values())

# Plotting
plt.bar(keys, values)
plt.xlabel('years')
plt.ylabel('Event count')
plt.title('Violent demonstration by year')
plt.show()



Violent2019 = {}
for m in months:
    Violent2019[m] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if(df['YEAR'][i]==2019 and df['SUB_EVENT_TYPE'][i] == 'Violent demonstration'):
        date_string = df['EVENT_DATE'][i]
        month_as_int = date_string.month
        Violent2019[month_as_int] +=1

keys = list(Violent2019.keys())
values = list(Violent2019.values())

# Plotting
# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Month')
plt.ylabel('Event count')
plt.title('Violent demonstration in 2019')
plt.show()




drone = {}
for y in ye:
    drone[y] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if (df['SUB_EVENT_TYPE'][i] == 'Air/drone strike'):
        drone[df['YEAR'][i]] +=1
        
keys = list(drone.keys())
values = list(drone.values())

# Plotting
plt.bar(keys, values)
plt.xlabel('Years')
plt.ylabel('Event count')
plt.title('Air/drone strike by year')
plt.show()



drone2016 = {}
for m in months:
    drone2016[m] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if(df['YEAR'][i]==2016 and df['SUB_EVENT_TYPE'][i] == 'Air/drone strike'):
        date_string = df['EVENT_DATE'][i]
        month_as_int = date_string.month
        drone2016[month_as_int] +=1

keys = list(drone2016.keys())
values = list(drone2016.values())

# Plotting
# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Month')
plt.ylabel('Event count')
plt.title('Air/drone strike in 2016')
plt.show()



drone = {}
for y in ye:
    drone[y] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if (df['SUB_EVENT_TYPE'][i] == 'Shelling/artillery/missile attack'):
        drone[df['YEAR'][i]] +=1
        
keys = list(drone.keys())
values = list(drone.values())

# Plotting
plt.bar(keys, values)
plt.xlabel('Years')
plt.ylabel('Event count')
plt.title('Shelling/artillery/missile attack by year')
plt.show()


missile2019 = {}
for m in months:
    missile2019[m] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if(df['YEAR'][i]==2019 and df['SUB_EVENT_TYPE'][i] == 'Shelling/artillery/missile attack'):
        date_string = df['EVENT_DATE'][i]
        month_as_int = date_string.month
        missile2019[month_as_int] +=1

        
keys = list(missile2019.keys())
values = list(missile2019.values())

# Plotting
# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Month')
plt.ylabel('Event count')
plt.title('Shelling/artillery/missile attack by year in 2019')
plt.show()



missile2017 = {}
for m in months:
    missile2017[m] = 0
    
for i in range(len(df['SUB_EVENT_TYPE'])):
    if(df['YEAR'][i]==2017 and df['SUB_EVENT_TYPE'][i] == 'Shelling/artillery/missile attack'):
        date_string = df['EVENT_DATE'][i]
        month_as_int = date_string.month
        missile2017[month_as_int] +=1

        
keys = list(missile2017.keys())
values = list(missile2017.values())

# Plotting
# Plotting
plt.figure(figsize=(11, 8))
plt.bar(keys, values)
plt.xlabel('Month')
plt.ylabel('Event count')
plt.title('Shelling/artillery/missile attack by year in 2017')
plt.show()






