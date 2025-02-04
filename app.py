# -*- coding: utf-8 -*-
"""Sales Data Analysis Using python libraries

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i2-E2QpAnXM086wCMxRY55q12dsCpsos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import pandas as pd

df = pd.read_excel("sales_data.xlsx", engine='openpyxl')
df.head()

"""What are the total sales over time (e.g., by month, quarter, or year)?"""

import matplotlib.pyplot as plt
import seaborn as sns

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['YearMonth'] = df['Order Date']

sales_over_time = df.groupby('YearMonth')['Sales'].sum()

fig=plt.figure(figsize=(12,6))
sales_over_time.plot(kind='line', figsize=(12, 6), title='Total Sales Over Time',color='orange')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales')
plt.title('Total Sales Over Time')
plt.show()

"""Which products, categories, or sub-categories generate the most revenue?"""

top_categories = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(top_categories)


top_sub_categories = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
print(top_sub_categories)


top_sub_categories.plot(kind='bar', figsize=(12, 6), title='Top Sub-Categories by Sales',color='green')
plt.ylabel('Total Sales')
plt.show()

top_categories.plot(kind='bar', figsize=(12, 6), title='Top Categories by Sales',color='red')
plt.ylabel('Total Sales')
plt.show()

"""How do sales vary by region, state, or city?"""

region_sales=df.groupby('Region')['Sales']
region_sales.plot(kind='bar', figsize=(12, 6), title='Region Sales',color='blue')
plt.ylabel('Total Sales')
plt.show()

"""Which customer segments (Consumer, Corporate) generate the highest sales?"""

segment_sales = df.groupby('Segment')['Sales'].sum()
segment_sales.plot(kind='pie', figsize=(8, 6), title='Sales by Customer Segment', color='orange')
plt.ylabel('Total Sales')
plt.show()

"""what are the sales based the region

"""

sales_region=df.groupby('Region')['Sales'].sum()
sales_region.plot(kind='barh',figsize=(8,6),title='Sales by the region')
plt.xlabel('Total Sales')
plt.ylabel('Region')
plt.show()

"""Who are the top customers by total sales?"""

total_sales_customer=df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

total_sales_customer.plot(kind='bar',figsize=(12,6),title='Total Sales by Customer',color='green')
plt.xlabel('Customer Name')
plt.ylabel('Total Sales')
plt.show()

"""What are the geographical trends in customer purchases?"""

geographical_trends=df.groupby('State')['Sales'].sum().sort_values(ascending=False)
geographical_trends.plot(kind='bar',figsize=(12,6),title='Geographical Trends',color='red')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.show()

"""What is the most popular shipping mode?"""

shipping_mode=df.groupby('Ship Mode')['Sales'].sum()
shipping_mode.plot(kind='bar',figsize=(12,6),title='Shipping Mode',color='yellow')
plt.xlabel('Ship Mode')
plt.ylabel('Total Sales')
plt.show()

import seaborn as sns

sns.boxplot(x='Ship Mode', y='Sales', data=df)
plt.title('Sales Distribution by Shipping Mode')
plt.show()

"""Which product categories and sub-categories are most and least profitable?"""

producT_category=df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
producT_category.plot(kind='barh',figsize=(12,6),title='Product Category',color='orange')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.show()

top_selling_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
top_selling_products.plot(kind='bar', figsize=(12, 6), title='Top Selling Products',color='green')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.show()

"""How does the performance of products vary by region or segment?"""

product_sales_bycity=df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)
product_sales_bycity.plot(kind='bar',figsize=(12,6),title='Product Sales by City',color='pink')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.show()

"""Highest and lowest City sales"""

# Compute highest and lowest selling separately
highest_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)
lowest_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=True).head(5)

# Plot highest selling cities
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # First subplot
plt.barh(highest_cities.index, highest_cities.values, color='orange')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.title('Top 5 Cities by Sales')

# Plot lowest selling products
plt.subplot(1, 2, 2)  # Second subplot
plt.barh(lowest_products.index, lowest_products.values, color='green')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.title('Bottom 5 Products by Sales')

# Adjust layout
plt.tight_layout()
plt.show()

regions_products=df.groupby(['Region','Product Name'])['Sales'].sum().head(5)
plt.figure(figsize=(12,6))
sns.barplot(x=regions_products.index.get_level_values(0), y=regions_products.values, hue=regions_products.index.get_level_values(1))
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Sales by Region and Product')
plt.show()

