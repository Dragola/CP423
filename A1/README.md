# Text Retrieval & Search Engine (CP423)

### Assignment 1 - Group 6 Submission

## Members:
- Gadd, Bryan

- Jain, Maheep

- Khamphavong, Osaka

- Simion, Alexandra

Due Date/Submission Date: June 11th, 2023, 11:59pm

## Summary:
The purpose of this assignment was to create a functioning program to run queries against a dataset in Python. This involved preprocessing the data, implementing an inverted index data structure, taking input from the user, implementing a combination of 'OR', 'AND', & 'NOT' operations for the queries, testing the code for errors, and running a set of queries that return data from the dataset. 

## Requirments:
To run this project you will need to run the following command to install the required modules/libraries:

!pip install -r .\requirements.txt  

## Summary of files:
### Q1.
Contains the tokenization code. The function take some text (aka string) as input, tokenizes it, and outputs a unique list of workds/tokens. We use this function to process the input sentence and text in the data documents in Q4.

### Q2.
Holds the InvertedIndex class. This class is used to store the tokens and their posting lists in a dictionary list. A dictionary list was used to provide speedy indexing + easier locating of index's. It contains a few methods to add/updated and index, and print the index list (for debugging).

### Q3.
Contains the query processing code. There are 2 functions:
- The first take a query (string) and checks the format. We use this in Q4 before running the query.
- The second takes a query (string), the inverted index, and the total number of documents to processes the query. Once complete, the function returns a new posting list and the total number of comparisons required to create the new posting list. We use this in Q4 to process the query(s) and output the results.

### Q4.
The main file that handles the input and output of the program. This file uses the methods in the other 3 files.

The video demo focuses on Q4 since this file handles both the input and output.

## How to run the program:
1. Install the required libraries/modules (refer to instruction above).
2. Run Q4.py.
3. You will be prompted to ender the number of quieres your want to run. Enter a number and press enter.
4. Next, you will be asked to enter the sentence for the query. Enter your sentence and press enter.
    - Example: lion stood thoughtfully for a moment
    - Note: DO NOT ENTER "" around the sentence. Just enter the sentence only.
5. Finally, you will be asked to enter the operators. Make sure they are all uppercase and are seperated by comma's.
    - Example: OR, AND, OR NOT, AND NOT. 
    - Note: DO NOT ENTER brackets '[]'. Only enter the operators and seperate using comma's.
6. Wait for query output 
    - Note: Will take 2 minutes or more to run the first query as the inverted index has to be generated. This process involves reading and processing all the data files so the more data files the longer it will take.
7. Repeat Steps 4-6 if the number of queries is greater then 1.