# import all necesarry libraies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the data
df=pd.read_csv('Supermart Grocery Sales - Retail Analytics Dataset.csv',parse_dates=['Order Date'])
print(df.info())

# Display first five rows in data
print(df.head())


# Check data type of each coloumns
print(df.info())


# change the data type of order date object to date time
df['Order Date'] =pd.to_datetime(df['Order Date'],format='mixed')
print(df.info())


# Applying group by function on category column and group the data on category
category=df.groupby("Category")
print(category.first())


# find the total sale by category
Sales_category=df.groupby("Category")["Sales"].sum()
print(Sales_category)


# Create a graph by total sales
Sales_category.plot(kind='bar')
plt.title('Category by Sales', fontsize = 14)
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()


# citywise total sales
city_name=df.groupby('City')
print(city_name.first())

# Total sales count
sales_total=df.groupby('City')['Sales'].sum()
print(sales_total)


# citywise total sale graph
sales_total.plot(kind='bar')
plt.title('SALES BY CITY',fontsize=15)
plt.xlabel('city')
plt.ylabel('Sales')
plt.show()


# Regional sales data
od=df.groupby('Region')['Sales'].sum()
print(od)


# Regional sales graph
od.plot(kind='bar')
plt.ylabel('Region')
plt.xlabel('Sales')
plt.show()


# count yearly sales
ndf=df.loc[(df['Order Date']>='2015-01-01')& (df['Order Date']<='2015-12-31')]
df['year'] = df['Order Date'].dt.year
yearly_sales = df.groupby('year')['Sales'].sum()
print(yearly_sales)


# Graph yearly sales count
yearly_sales.plot(kind='pie')
plt.title('YEARLY SALES COUNT', fontsize=15 )
plt.pie('Sales', labels='yearly_sales',autopct='%.1f%%')
plt.xlabel('year')
plt.ylabel('Sales'
plt.show()