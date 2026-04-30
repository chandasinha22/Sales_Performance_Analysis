import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')
print("Raw shape:", df.shape)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
print("Dates converted to datetime.")

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.strftime('%b')
df['Quarter'] = df['Order Date'].dt.quarter.map(
    {1:'Q1', 2:'Q2', 3:'Q3', 4:'Q4'}
)
df['Profit Margin %'] = (df['Profit'] / df['Sales'] * 100).round(2)
print("New columns added: Year, Month, Month Name, Quarter, Profit Margin %.")

df.to_csv("sales_cleaned.csv", index=False)
print("Cleaned file saved as 'sales_cleaned.csv'.")

print("\nFinal shape:", df.shape)
print("New columns:", ['Year','Month','Month Name','Quarter','Profit Margin %'])
print("\nSample output:")
print(df[['Order Date','Year','Month Name','Quarter','Sales','Profit','Profit Margin %']].head())