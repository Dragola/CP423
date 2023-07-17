import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Retrieve the specified webpage as raw HTML using the requests library
url = "https://en.wikipedia.org/wiki/List_of_Canadian_provinces_and_territories_by_historical_population"
response = requests.get(url)
html_content = response.content


# Decode the HTML into a tree-structured Python object with the BeautifulSoup library
soup = BeautifulSoup(html_content, 'html.parser')


# Utilize BeautifulSoup to identify and extract only the tables we're interested in
tables = soup.find_all('table', class_='wikitable')


# Merge the tables, sanitize the text, and transform them into a single Python dictionary
data = {}
i = 0
for table in tables:
    df = pd.read_html(str(table))[0]
    df = df.applymap(lambda x: BeautifulSoup(str(x), 'html.parser').get_text())
    data[i] = df.to_dict()
    i+=1


# Construct a pandas dataframe out of this dictionary
dfs = []
for i, table_data in data.items():
    df = pd.DataFrame(table_data)
    dfs.append(df)
# Regex function to ensure that all the Names in table matches
for df in dfs:
    df['Name'] = df['Name'].str.replace(r'\[.*?\]', '', regex=True)

merged_df = pd.merge(dfs[0], dfs[1], on='Name', how='outer')
for i in range(2, len(dfs)):
    merged_df = pd.merge(merged_df, dfs[i], on='Name', how='outer')

# Final Database
merged_df
