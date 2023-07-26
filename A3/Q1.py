import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Part 1- Retrieve the specified webpage as raw HTML using the requests library
url = "https://en.wikipedia.org/wiki/List_of_Canadian_provinces_and_territories_by_historical_population"
response = requests.get(url)
html_content = response.content

# Part 2- Decode the HTML into a tree-structured Python object with the BeautifulSoup library
soup = BeautifulSoup(html_content, 'html.parser')

# Part 3- Utilize BeautifulSoup to identify and extract only the tables we're interested in
tables = soup.find_all('table', class_='wikitable')

# Part 4- Merge the tables, sanitize the text, and transform them into a single Python dictionary
data = {}
i = 0
for table in tables:
    df = pd.read_html(str(table))[0]
    df = df.applymap(lambda x: BeautifulSoup(str(x), 'html.parser').get_text())
    data[i] = df.to_dict()
    i+=1

# Part 5- Construct a pandas dataframe out of this dictionary
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

# print the final database
print("Merged Pandas Table:")
print(merged_df)
print("\n")

# Part 6- Locate all h2 elements on the HTML page and display their text content
headers = soup.find_all("h2")

header_list = []
#iterate over each header
for header in headers:
    # get the text from the header
    headline_text = header.get_text()

    # split the text at '[' so that [edit] is removed from the actual header
    headline_text_split = headline_text.split("[")

    # add header text to list
    header_list.append(headline_text_split[0])

# print header texts
print("H2 elements (aka headers):")
for text in header_list:
    print(text)
print("\n")

# Part 7- Generate a list of all the hyperlinks embedded within the tables
links = soup.find_all("a", {"href": True, "title": True})

link_list = []
link_names = []
# iterate over each link
for data in links:
    # extract the text
    text = data['title']

    # strip any whitespace
    text = text.strip()

    # check if the title associated with the link is in the tables
    if (text in merged_df['Name'].values):
        # ensure the link doesn't already exists in the list
        if (data['href'] not in link_list):
            # add title to the list
            link_names.append(text)

            # add link to the list
            link_list.append(data['href'])

# print the retrieved links to indicate what webpages will be downloaded
print("Hyperlinks retrieved that will be downloaded next:")
for link in link_list:
    print(link)
print("\n")

# Part 8- Download every webpage by traversing the links included in the list created in the previous step
# the domain for the URL
domain = "https://en.wikipedia.org/"

# the folder where the webpages will be downloaded to
folder = "./webpages"

# create directory for webpages
if (os.path.exists("./webpages") == False):
    os.mkdir("./webpages")

print("Downloading webpages, please wait...\n")

i = 0
# iterate over each link
for link in link_list:

    # create the URL
    url = domain + link

    # get the webpage
    response = requests.get(url)

    # open the file to write
    output = open(folder + "/" + link_names[i] + ".html", "wb")

    # write the webpage to the file
    output.write(response.content)
    output.close()
    i += 1

    # wait 5 seconds before downloading the next one (don't want to spam the server)
    time.sleep(5)

# indicate downloading completed
print("Webpages downloaded. Please check the " + folder + " folder.")
