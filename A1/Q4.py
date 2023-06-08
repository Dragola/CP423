from Q1 import preprocess_text
from Q2 import InvertedIndex
from Q3 import *
import os

documents: dict = {} # the files that we index from
invertedIndex: InvertedIndex = None

# read through all files, process the text, and return the inverted index
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
        text = open(filePath, "r") 

        # get the first line in the file
        line = text.readline() 

        # keep reading lines from the file until there are no more lines
        while line != "":
            #call method from Q1 to tokenize the line- a bit broken still
            uniqueWords = preprocess_text(line)
            
            # add the words/tokens from the line into the index list
            for word in uniqueWords:
                invertedIndex.addIndex(word, documentId)
            
            # get the next line in the file
            line = text.readline() 

        # close the file after reading it
        text.close() 
    
        print("Finished document " + str(documentId)) # DEBUG ONLY

        # add the document to the list of documents
        document: dict = {documentId: file}
        documents.update(document)
        
        # increment the document ID for the next file
        documentId += 1 
    return invertedIndex

'''
Function to output the inverted index to verify integrity (DEBUG ONLY)
'''
def outputInvertedIndex(invertedIndex: InvertedIndex):
    global documents

    # open file to write to
    file = open("./InvertedIndex.txt", "w")

    # write each file name + document ID to the file
    for documentId in documents.keys():
        file.write(documents[documentId] + "| DocumentID= " + str(documentId) + "\n")

    # add space for the inverted index
    file.write("\n\n")

    # write each index and posting list to the file
    invertedIndexDictionary = invertedIndex.indexList
    for index in invertedIndexDictionary:
        file.write(index)
        file.write(" --> {")
        for documentID in invertedIndexDictionary[index]:
            file.write(str(documentID) + ", ")
        file.write("}- size= " + str(len(invertedIndexDictionary[index])) + "\n")
    
    # close file
    file.close()

if __name__ == "__main__":
    # process the input
    '''
    Input sentence: “lion stood thoughtfully for a moment”
    Input operation sequence: [OR, OR, OR]

    Expected preprocessed query: “lion OR stood OR thoughtfully OR moment”
    '''
    # get the number of query that the user wants to run
    user_input_query_number = input("How many queries are you running? ")
    query_number = int(user_input_query_number)

    # get the query from user and process it until number of queries is reached
    for i in range(query_number):
        # get the query from user
        print("Query #" + str(i+1) + ":")      
        user_input_sentence = input("Input Sentence: ")
        user_input_operation_sequence = input("Input operation sequence: ")

        # processes the sentence (Q1)
        # Ex. “lion stood thoughtfully for a moment” --> “lion OR stood OR thoughtfully OR moment”
        operators = user_input_operation_sequence.strip().split(",")
        preprocessed_sentence = preprocess_text(user_input_sentence)

        # DEBUG ONLY
        print("preprocessed_sentence from function: ", end="")
        print(preprocessed_sentence)

        # new string to put query into
        preprocessed_query = ""
        operator_index = 0

        # add the operators to the processed sentence, forming the actual query
        for word in preprocessed_sentence:
            # if there's an operator add the word followed by the operator
            if (operator_index < len(operators)):
                text = word + " " + operators[operator_index].strip() + " " 
            # if there are no more operators then just add the word to the end
            else :
                text = word
            preprocessed_query += text
            operator_index += 1

        # output query after being processed
        print("Expected preprocessed query: " + preprocessed_query)

        # check query before continuing
        if (check_query_format_valid(preprocessed_query) == True):
            
            # generate invertedIndex if it wasn't previously
            if (invertedIndex == None):
                print("Generating inverted index. Please wait...")
                # read all the files and create the inverted index (Q2)
                invertedIndex = createInvertedIndex()

            # sort the documentID's (NOTE: each docuemntId set becomes a list)
            #TODO- is this needed?
            invertedIndex.sortDocumentIDs()

            # DEBUG ONLY- write documetns and inverted index to a file for verifying/debugging
            outputInvertedIndex(invertedIndex) 
            
            # run the query (Q3)
            result, total_comparisons = process_query(preprocessed_query, invertedIndex, len(documents))
           
            # output number of matched documents
            print("Number of matched documents: " + str(len(result)))
            
            #TODO- Should we only print if AND was used?
            # output min number of comnparisons (OR doesn't contribute to this, right?)
            print("Minimum number of comparisons required: " + str(total_comparisons))
            
            # output the list of document names (with their ID's) that satisfy the query
            print("List of retrieved document names")
            for documentId in result:
                print(documents[documentId] + " | ID= " + str(documentId))
    
    