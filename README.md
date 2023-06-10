Text Retrieval & Search Engine (CP423)

Assignment 1 - Group 6 Submission

  Members:
    Gadd, Bryan
    Jain, Maheep
    Khamphavong, Osaka
    Simion, Alexandra
    
Due Date/Submission Date: June 11th, 2023, 11:59pm

The purpose of this assignment was to create a functioning program to run queries against a dataset in Python. This involved preprocessing the data, implementing an inverted index data structure, taking input from the user, implementing a combination of 'OR', 'AND', & 'NOT' operations for the queries, testing the code for errors, and running a set of queries that return data from the dataset. 

To run this project you will need to install the following packages/modules:
  - !pip instal -r .\requirements.txt  
  - !pip install collections
  - !pip install re
  - !pip install nltk
  - collection
  - nltk
And of course, loop through each file to read the lines in each file, until the end of the files and list of files is reached, while creating a unique document ID for each file after reading. 

Q1. 
For preprocessing the text, we converted the text to lowercase using .lower() then tokenized the text by passing the dataset into word_tokenize(). We then removed any stopwords from the tokenized words, excluded special characters, removed whitespace, and eliminated single character words before returning the final token. We imported and downloaded stopwords and word_tokenize from nltk as certain functions from these modules were required to identify and remove stopwords amongst tokenizing the text. The functions strip() and sub() were used to remove white space and exclude special characters by identifying the characters we wanted to use (a-z and A-Z). 

Q2. 
We made a datastructure called InvertedIndex to store key-value pairs through the initialization of objects to store this data. We also had to define a few functions labeled addIndex(), sortDocumentIDs(), and a few testing methods that we use to call upon in other documents. The function addIndex() does exactly what it's titled to do. It checked to see if the index already exists in the dictionary. If it doesn't, it adds in the new index to the dictionary and creates a document ID. Using a for loop, sortDocumentIDs() sorts the documentIds for each index in the list. The testing methods are defined to use sortDocumentID() and addIndex() to add different combination(s) of word(s) to multiple or a single document ID. They also sort added words with multiple document IDs for each word. 

Q3.
Importing the data structure we created, we made 2 functions to check if the format of the query is valid (that it meets certain requirements) and to process the requests of the query. We added cases to check for and handle "AND", "OR", "NOT",  or combination of the three. If none were present or if the query is missing either a word, operation, and/or another word, it would print an error message. The process_query() function breaks down the query and process then checks if all the words in the query exists in the inverted list. If it exists, this information is appended and returned as a list of document IDs that obey the specifications of the query.

Q4. 
This is the main testing file. The previous 3 files are imported in here. As the testing file, it reads all the documents in the data folder, preprocesses and tokenizes the test, and stores it in the inverted index data structure. It asks the user to create the query, checks it, runs the query against the sorted document ids, then outputs the number of matched documents with the query. 

A video voiceover was later created to demonstrate some output against a user-created query on a dataset file. 


