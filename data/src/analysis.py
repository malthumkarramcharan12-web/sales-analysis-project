import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sales.csv')

df['Order Date'] = pd.to_datetime(df['Order Date'])

sales_by_region = df.groupby('Region')['Sales'].sum()
profit_by_category = df.groupby('Category')['Profit'].sum()

print("Top Region:", sales_by_region.idxmax())
print("Best Category:", profit_by_category.idxmax())

sales_by_region.plot(kind='bar', title='Sales by Region')
plt.show()
