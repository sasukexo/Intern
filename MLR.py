# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iCImFRe0jnihvCaO3Ui0m20z4wMx_8m0
"""



from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
df=pd.read_csv('/content/drive/MyDrive/SGTL-Accident_data1.csv')
df.head()
df.describe()

df.duplicated().sum()

df=df.dropna()
df.isna().sum()

df.corr()

sns.heatmap(df.corr())

numerical=[i for i in df.columns if df[i].dtype!='O']
print('The numerica variables are',numerical)

df2=df.drop(['SPV'],axis=1)
df2.head()

df2.shape
categorical_new=[i for i in df2.columns if df2[i].dtype=='O']
print(categorical_new)

for i in categorical_new:
    print(df2[i].value_counts())

df3=pd.concat([df2],axis=1)
df3.head()

y=df3.iloc[:,1]
y.head()

plt.figure(figsize=(20, 8))

ax =sns.countplot(x = y, palette='muted')
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')


plt.title('Cause of accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 8))

ax = sns.countplot(x='MONTH', hue='ACC_TYPE', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('No of accidents on each month and their type')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 8))

ax = sns.countplot(x='PRIMARY_REASON', hue='ACC_TYPE', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(50, 50))

ax = sns.countplot(x='SECONDARY_REASON', hue='ACC_TYPE', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(50, 50))

ax = sns.countplot(x='SECONDARY_REASON', hue='MONTH', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(50, 50))

ax = sns.countplot(x='ACC_TYPE', hue='ROAD_CONDITION', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 8))

ax = sns.countplot(x='CHAINAGE', hue='Count', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

y=df3.iloc[:,2]
y.head()

plt.figure(figsize=(20, 28))

ax =sns.countplot(x = y, palette='muted')
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')


plt.title('Cause of accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 8))

ax = sns.countplot(x='ACC_TYPE', hue='DIR', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 8))

ax = sns.countplot(x='ACC_TYPE', hue='LANE_TYPE', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 8))

ax = sns.countplot(x='ACC_TYPE', hue='ACCIDENT_CAUSE_TYPE', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
df=pd.read_csv('/content/drive/MyDrive/SGTL-Accident_data1.csv')




# Convert the 'DATE' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2023
filtered_df = df[df['Year'] == year]

# Group the data by month and calculate the number of accidents
monthly_accidents = filtered_df.groupby('Month').size()

# Generate a bar chart to represent the data
monthly_accidents.plot(kind='bar', figsize=(10, 6))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.show()

# Convert the 'DATE' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2022
filtered_df = df[df['Year'] == year]

# Group the data by month and calculate the number of accidents
monthly_accidents = filtered_df.groupby('Month').size()

# Map month numbers to month names
month_names = pd.Series(['January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'])
monthly_accidents.index = month_names[monthly_accidents.index - 1]

# Generate a bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', figsize=(15, 10))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

# Convert the 'DATE' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2021
filtered_df = df[df['Year'] == year]

# Group the data by month and calculate the number of accidents
monthly_accidents = filtered_df.groupby('Month').size()

# Map month numbers to month names
month_names = pd.Series(['January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'])
monthly_accidents.index = month_names[monthly_accidents.index - 1]

# Generate a bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', figsize=(15, 10))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2022
filtered_df = df[df['Year'] == year]

# Group the data by month and accident type, calculate the number of accidents
monthly_accidents = filtered_df.groupby(['Month', 'ACC_TYPE']).size().unstack()

# Map month numbers to month names
month_names = pd.Series(['January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'])
monthly_accidents.index = month_names[monthly_accidents.index - 1]

# Generate a stacked bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', stacked=False, figsize=(20, 10))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.legend(title='Accident Type')

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2021
filtered_df = df[df['Year'] == year]

# Group the data by month and accident type, calculate the number of accidents
monthly_accidents = filtered_df.groupby(['Month', 'ACC_TYPE']).size().unstack()

# Map month numbers to month names
month_names = pd.Series(['January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'])
monthly_accidents.index = month_names[monthly_accidents.index - 1]

# Generate a stacked bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', stacked=False, figsize=(20, 10))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.legend(title='Accident Type')

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2022
filtered_df = df[df['Year'] == year]

# Group the data by month and accident type, calculate the number of accidents
monthly_accidents = filtered_df.groupby(['Month', 'SECONDARY_REASON']).size().unstack()

# Map month numbers to month names
month_names = pd.Series(['January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'])
monthly_accidents.index = month_names[monthly_accidents.index - 1]

# Generate a stacked bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', stacked=True, figsize=(20, 20))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.legend(title='Cause of accident')

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2022
filtered_df = df[df['Year'] == year]

# Group the data by month and accident type, calculate the number of accidents
monthly_accidents = filtered_df.groupby(['Month', 'CHAINAGE']).size().unstack()

# Map month numbers to month names
month_names = pd.Series(['January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'])
monthly_accidents.index = month_names[monthly_accidents.index - 1]

# Generate a stacked bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', stacked=True, figsize=(30, 30))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.legend(title='Accident Type')

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2022
filtered_df = df[df['Year'] == year]

# Group the data by month and accident type, calculate the number of accidents
monthly_accidents = filtered_df.groupby(['Month', 'ACC_TYPE']).size().unstack()

# Generate a stacked bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', stacked=False, figsize=(20, 10))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.legend(title='Accident Type')

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 8))

ax = sns.countplot(x='SECONDARY_REASON', hue='FATAL', data=df3, palette='muted')

for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.title('Cause of Accident')
plt.show()

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Extract the month and year values from the 'DATE' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Filter the data for a specific year
year = 2023
filtered_df = df[df['Year'] == year]

# Group the data by month and accident type, calculate the number of accidents
monthly_accidents = filtered_df.groupby(['Month', 'ACC_TYPE']).size().unstack()

# Map month numbers to month names
month_names = pd.Series(['January', 'February', 'March', 'April', 'May', 'June',
                         'July', 'August', 'September', 'October', 'November', 'December'])
monthly_accidents.index = month_names[monthly_accidents.index - 1]

# Generate a stacked bar chart to represent the data
ax = monthly_accidents.plot(kind='bar', stacked=False, figsize=(20, 10))
plt.title(f'Accidents per Month - {year}')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.legend(title='Accident Type')

# Add data labels to the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

