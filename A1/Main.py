from Q1 import preprocess_text
from Q2 import InvertedIndex
from Q3 import process_query
import os

files: list[str] # the files that we index from

# read through all files, process the text, and return the inverted index
def createInvertedIndex():
    global files

    invertedIndex = InvertedIndex()
    
    files = os.listdir("./data/") # get a list of all the files in the data directory
    #print(files) # remove later (DEBUG ONLY)

    documentId = 1 # the document ID for the current file

    # loop through each file
    for file in files:
        filePath = "./data/" + file # set up the path to the file
        text = open(filePath, "r") # open the file for reading
        line = text.readline() # get the first line

        # keep reading lines from the file until EOF is reached
        while line != "":
            #print("line= " + line) # DEBUG ONLY

            #call method from Q1 (missing the module)
            uniqueWords = preprocess_text(line)
            
            # add the words/tokens from the line into the index list
            for word in uniqueWords:
                invertedIndex.addIndex(word, documentId)
            
            line = text.readline() # get the next line in the file

        text.close() # close the file after reading it
        

        print("Finished document " + str(documentId)) # DEBUG ONLY

        documentId += 1 # increment the document ID for the next file

    return invertedIndex

'''
Function to output the inverted index to verify integrity (DEBUG ONLY)
'''
def outputInvertedIndex(invertedIndex: InvertedIndex):
    file = open("./InvertedIndex.txt", "w")

    documentID = 1 # document ID

    # write each file name + document ID to the txt file
    for documentName in files:
        file.write(documentName + "| DocumentID= " + str(documentID) + "\n")
        documentID += 1

    file.write("\n\n")

    # write each index and posting set to the txt file
    invertedIndexDictionary = invertedIndex.indexList
    for index in invertedIndexDictionary:
        file.write(index)
        file.write(" --> {")
        for documentID in invertedIndexDictionary[index]:
            file.write(str(documentID) + ", ")
        file.write("}- size= " + str(len(invertedIndexDictionary[index])) + "\n")
    
    file.close()

if __name__ == "__main__":
    # process the input (need to do)
    '''
    Input sentence: “lion stood thoughtfully for a moment”
    Input operation sequence: [OR, OR, OR]

    Expected preprocessed query: “lion OR stood OR thoughtfully OR moment”
    '''
    # get query
    user_input_query_number = input("How many queries are you running? ")
    query_number = int(user_input_query_number)
    for i in range(query_number):
        # get the query
        print("Query #" + str(i) + ":")      
        user_input_sentence = input("Input Sentence: ")
        user_input_operation_sequence = input("Input operation sequence: ")

        # need to processes the input (remove common words)
        # Ex. “lion stood thoughtfully for a moment” --> “lion OR stood OR thoughtfully OR moment”
        operators = user_input_operation_sequence.strip().split()
        preprocessed_sentence = preprocess_text(user_input_sentence) # returning a set with no elements...

        print("preprocessed_sentence from function: ", end="")
        print(preprocessed_sentence)

        preprocessed_query = ""
        operator_index = 0
        for word in preprocessed_sentence:
            text = word + " " + operators[operator_index] + " "
            preprocessed_query += text
            operator_index += 1

        print("Expected preprocessed query: " + preprocessed_query)
    
        # invertedIndex = createInvertedIndex() # read all the files and create the inverted index

        # # sort the documentID's
        # # NOTE: docuemntID set becomes a list
        # invertedIndex.sortDocumentIDs()

        # outputInvertedIndex(invertedIndex) # DEBUG ONLY
        
        # # call method to run the query- Q3
        # result = process_query(user_input, invertedIndex, len(files))


        # # output results after query is executed (need to do)
        # '''
        # Output:
        # Number of matched documents: 270
        # Minimum number of comparisons required: 671
        # List of retrieved document names
        # '''
        # print("Number of matched documents: " + str(len(result)))
        # print("Minimum number of comparisons required: We need to record this")
        # print("List of retrieved document names")

        # for documentID in result:
        #     print(files[documentID])
    
    