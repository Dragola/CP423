# imports
from Q1 import preprocess_text
from Q2 import InvertedIndex
from Q3 import *
import os

# Properties
# the list of ID's to document names- used in output
documents: dict = {}

# the Inverted Index that holds a list of all the word --> posting list pairs
invertedIndex: InvertedIndex = None

'''
Reads all the documents in the data folder, tokenize the text, and stores it in the Inverted Index data structure.
'''
def createInvertedIndex():
    global documents

    # create new Inverted Index from Q2
    invertedIndex = InvertedIndex()

    # get a list of all the files in the data directory
    list_of_file_names = os.listdir("./data/") 

    # the document ID for the current file
    documentId = 1 

    # loop through each file and add to the documents dict
    for file in list_of_file_names:
        # set up the path to the file
        filePath = "./data/" + file
       
        # open the file for reading
        stream = open(filePath, "r") 

        # get the text form the file
        text = stream.read()

        # tokenize the file text (Q1)
        uniqueWords = preprocess_text(text)
        
        # add the words/tokens from the token list into the inverted index list
        for word in uniqueWords:
            invertedIndex.addIndex(word, documentId)

        # close the file after reading it
        stream.close()

        # add the document to the list of documents
        document: dict = {documentId: file}
        documents.update(document)
        
        # increment the document ID for the next file
        documentId += 1

    return invertedIndex

'''
Main function
'''
if __name__ == "__main__":
    # get the number of query that the user wants to run
    user_input_query_number = input("How many queries are you running? ")
    query_number = int(user_input_query_number)

    # loop through each query
    for i in range(query_number):
        print("Query #" + str(i+1) + ":")

        # get the query sentence
        user_input_sentence = input("Input Sentence: ")

        # get the operators to apply to the query
        user_input_operation_sequence = input("Input operation sequence: ")

        # processes the sentence (Q1)
        operators = user_input_operation_sequence.strip().split(",")
        preprocessed_sentence = preprocess_text(user_input_sentence)

        # new string for the query
        preprocessed_query = ""
        
        # index of operator list
        operator_index = 0

        # create tha actual query by adding the words + operators together
        for word in preprocessed_sentence:
            # if there's an operator add the word followed by the operator
            if (operator_index < len(operators)):
                text = word + " " + operators[operator_index].strip() + " " 
            # if no more operators then just add the word
            else :
                text = word
            preprocessed_query += text
            operator_index += 1

        # output query after being processed
        print("\nExpected preprocessed query: " + preprocessed_query)

        # check query before continuing
        if (check_query_format_valid(preprocessed_query) == True):
            
            # generate invertedIndex only if it wasn't generated previously
            if (invertedIndex == None):
                print("\nGenerating inverted index for first time. Please wait...")

                # read all the files and create the inverted index (Q2)
                invertedIndex = createInvertedIndex()
            
            # run the query (Q3)
            result, total_comparisons = process_query(preprocessed_query, invertedIndex, len(documents))

            # indicate output
            print("\nOutput:")

            # output number of matched documents
            print("Number of matched documents: " + str(len(result)))
            
            # output min number of comparisons
            print("Minimum number of comparisons required: " + str(total_comparisons))
            
            # output the list of document names (+ ID's) that satisfies the query
            print("List of retrieved document names")
            for documentId in result:
                print(documents[documentId] + " | ID= " + str(documentId))
    
    