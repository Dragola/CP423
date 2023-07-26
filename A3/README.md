# Text Retrieval & Search Engine (CP423)

### Assignment 3 - Group 6 Submission

## Members:
- Gadd, Bryan

- Jain, Maheep

- Khamphavong, Osaka

- Simion, Alexandra

Due Date/Submission Date: July 26th, 2023, 11:59pm

## Summary:
The purpose of this assignment is to create a webscarping and retrieve an information from webpage with the given URL. 

The task entails utilising the provided URL, which directs users to Wikipedia's archive of Canadian province population counts. The goal is to use the pandas library to import HTML tables from the website and modify them. The procedure involves getting the webpage's raw HTML using the requests library, decoding it into a Python object with BeautifulSoup, extracting the needed tables, joining them into a single dictionary, and constructing a pandas dataframe. The work also calls for locating and displaying the text content of the h2 elements on the page, creating a list of hyperlinks within the tables, and downloading webpages by clicking on those URLs.

## Requirments:
To run this project you will need to run the following command to install the required modules/libraries:

pip install -r .\requirements.txt

## Summary of files:
### Q1.
This file is the entire assignment containing all 8 parts of Q1. First, the specidied wikipedia webpage is retrieved. Next, it pulls table data and combines them into one pandas database framework which is then printed. After it pulls all the h2 (header) elements. Finally, it grads the hyperlinks that are embeded within the tables and downloads them.

How to read the poandas table:
- The column headers are the same as the headers from the tables just combined into one large table. If you look at each tables on the wikipedia page you can see how they all start with the province name then followed by the years (population of the province that year).
- For example if you look at the row for "Lower Canada" in the example below it reads that there was a population of 14000 in 1700, 29000 in 1750, ..., and 450000 in 1800. The rest of the row has NaN as the original table had no colums for those years so there's no data.

Assumptions:
1. Part 7- Any reference links who's title was in the merged table database was considered valid and is retrieved in Part 8.

## How to run the program:
1. Refer to Requirements section above to install the required libraries. You will not be able to run the file unless you have the required libraries installed.
2. Run Q1.py.
3. Wait for the program to finish running.
4. Check the terminal for the pandas table and ./webpages folder for the downloaded web pages.

## Program Example:
Merged Pandas Table:
                         Name     1700     1725     1750      1775    1800    1825 Confederated[d]        1841  ...        1981        1986        1991      1996      2001      2006      2011      2016      2021
0                Lower Canada  14000.0  29000.0  54500.0   96000.0  225000  450000             NaN         NaN  ...         NaN         NaN         NaN       NaN       NaN       NaN       NaN       NaN       NaN    
1               New Brunswick      nan      nan      nan       nan   10000   75000          1867.0  156,162[i]  ...    689375.0    709442.0    723900.0    738133    729498    729997    751171    747101    775610    
2                Newfoundland    500.0   5000.0  10000.0   16000.0   10000   45759             NaN         NaN  ...         NaN         NaN         NaN       NaN       NaN       NaN       NaN       NaN       NaN    
3                 Nova Scotia   1300.0   5000.0  14000.0   20000.0   57000  150000          1867.0  202,575[t]  ...    839805.0    873176.0    899942.0    909282    908007    913462    921727    923598    969383    
4        Prince Edward Island      nan    300.0   2500.0   10000.0   20000   28600          1873.0       47042  ...    121225.0    126646.0    129765.0    134557    135294    135851    140204    142907    154331    
5                Upper Canada      nan      nan      nan    8000.0   50000  158027             NaN         NaN  ...         NaN         NaN         NaN       NaN       NaN       NaN       NaN       NaN       NaN    
6                       Total  15800.0  39300.0  81000.0  150000.0  382000  907386             NaN         NaN  ...         NaN         NaN         NaN       NaN       NaN       NaN       NaN       NaN       NaN    
7                     Alberta      NaN      NaN      NaN       NaN     NaN     NaN          1905.0         nan  ...   2213650.0   2365825.0   2545553.0   2696826   2974807   3290350   3645257   4067175   4262635    
8            British Columbia      NaN      NaN      NaN       NaN     NaN     NaN          1871.0       62100  ...   2713615.0   2883367.0   3282061.0   3724500   3907738   4113487   4400057   4648055   5000879    
9                    Manitoba      NaN      NaN      NaN       NaN     NaN     NaN          1870.0    4,704[g]  ...   1013705.0   1063016.0   1091942.0   1113898   1119583   1148401   1208268   1278365   1342153    
10  Newfoundland and Labrador      NaN      NaN      NaN       NaN     NaN     NaN          1949.0   96,296[k]  ...    563750.0    568349.0    568474.0    551792    512930    505469    514536    519716    510550    
11      Northwest Territories      NaN      NaN      NaN       NaN     NaN     NaN          1870.0         nan  ...     45540.0     52238.0     57649.0     39672     37360     41464     41462     41786     41070    
12                    Nunavut      NaN      NaN      NaN       NaN     NaN     NaN          1999.0         nan  ...         nan         nan         nan     24730     26745     29474     31906     35944     36858    
13                    Ontario      NaN      NaN      NaN       NaN     NaN     NaN          1867.0  466,831[v]  ...   8534265.0   9101694.0  10084885.0  10753573  11410046  12160282  12851821  13448494  14223942    
14                     Quebec      NaN      NaN      NaN       NaN     NaN     NaN          1867.0  716,670[y]  ...   6369065.0   6532461.0   6895963.0   7138795   7237479   7546131   7903001   8164361   8501833    
15               Saskatchewan      NaN      NaN      NaN       NaN     NaN     NaN          1905.0         nan  ...    956440.0   1009613.0    988928.0    990237    978933    968157   1033381   1098352   1132505    
16                      Yukon      NaN      NaN      NaN       NaN     NaN     NaN          1898.0         nan  ...     23075.0     23504.0     27797.0     30766     28674     30372     33897     35874     40232    
17                     Canada      NaN      NaN      NaN       NaN     NaN     NaN             nan     1752380  ...  24083510.0  25309331.0  27296859.0  28846761  30007094  31612897  33476688  35151728  36991981    

[18 rows x 34 columns]


H2 elements (aka headers):
Contents
1700 to 1825
1841 to 1931
1941 to 1991
1996 to 2021
Notes


Hyperlinks retrieved that will be downloaded next:
/wiki/Nunavut
/wiki/Northwest_Territories
/wiki/Lower_Canada
/wiki/Nova_Scotia
/wiki/New_Brunswick
/wiki/Prince_Edward_Island
/wiki/Upper_Canada
/wiki/Alberta
/wiki/British_Columbia
/wiki/Manitoba
/wiki/Newfoundland_and_Labrador
/wiki/Ontario
/wiki/Quebec
/wiki/Saskatchewan
/wiki/Yukon
/wiki/Canada


Downloading webpages, please wait...

Webpages downloaded. Please check the ./webpages folder.
