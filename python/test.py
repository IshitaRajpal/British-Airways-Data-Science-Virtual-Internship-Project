import pandas as pd
import bs4

from bs4 import BeautifulSoup

soup = BeautifulSoup("https://www.kaggle.com/datasets/xontoloyo/data-penjualan-zara")
print(soup.prettify())
 # Display first few rows

test_data = "/Users/ishitarajpal/Documents/ishita_projects/python/ZARA sales export 2025-03-25 09-26-13.csv"

df = pd.read_csv(test_data)  # Use pd.read_excel(url) if it's an Excel file

#print(df)