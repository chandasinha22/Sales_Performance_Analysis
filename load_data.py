import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chanda@2525", 
    database="sales_project"
)

print("MySQL connected!")

df = pd.read_csv("sales_cleaned.csv")

df.columns = df.columns.str.replace(' ', '_').str.replace('%', 'pct')

print("Columns:", df.columns.tolist())
print("Rows to load:", len(df))

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sales;")
cursor.execute("""
    CREATE TABLE sales (
        Row_ID INT,
        Order_ID VARCHAR(20),
        Order_Date DATE,
        Ship_Date DATE,
        Ship_Mode VARCHAR(30),
        Customer_ID VARCHAR(20),
        Customer_Name VARCHAR(50),
        Segment VARCHAR(20),
        Country VARCHAR(30),
        City VARCHAR(30),
        State VARCHAR(30),
        Postal_Code VARCHAR(10),
        Region VARCHAR(20),
        Product_ID VARCHAR(20),
        Category VARCHAR(30),
        Sub_Category VARCHAR(30),
        Product_Name VARCHAR(200),
        Sales FLOAT,
        Quantity INT,
        Discount FLOAT,
        Profit FLOAT,
        Year INT,
        Month INT,
        Month_Name VARCHAR(5),
        Quarter VARCHAR(3),
        Profit_Margin_pct FLOAT
    )
    """)

print("Table 'sales' created.")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))
    
    conn.commit()
print("Data loaded:", len(df))
cursor.close()
conn.close()