from Q1 import preprocess_text
from Q2 import InvertedIndex
from Q3 import process_query
import os

documents: dict = {} # the files that we index from

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
    # process the input (need to do)
    '''
    Input sentence: “lion stood thoughtfully for a moment”
    Input operation sequence: [OR, OR, OR]

    Expected preprocessed query: “lion OR stood OR thoughtfully OR moment”
    '''
    # get the number of query that the user wants to run
    user_input_query_number = input("How many queries are you running? ")
    query_number = int(user_input_query_number)

    # get the query and process it for 
    for i in range(query_number):
        # get the query
        print("Query #" + str(i) + ":")      
        user_input_sentence = input("Input Sentence: ")
        user_input_operation_sequence = input("Input operation sequence: ")

        # need to processes the input (remove common words)
        # Ex. “lion stood thoughtfully for a moment” --> “lion OR stood OR thoughtfully OR moment”
        operators = user_input_operation_sequence.strip().split(",")
        preprocessed_sentence = preprocess_text(user_input_sentence) # returning a set with no elements...

        print("preprocessed_sentence from function: ", end="")
        print(preprocessed_sentence)

        preprocessed_query = ""
        operator_index = 0
        for word in preprocessed_sentence:
            if (operator_index < len(operators)):
                text = word + " " + operators[operator_index] + " " 
            else :
                text = word
            preprocessed_query += text
            operator_index += 1

        print("Expected preprocessed query: " + preprocessed_query)

        # read all the files and create the inverted index (TODO- Should only run once with multiple queries)
        invertedIndex = createInvertedIndex() 

        # sort the documentID's
        # NOTE: docuemntID set becomes a list
        invertedIndex.sortDocumentIDs()

        outputInvertedIndex(invertedIndex) # DEBUG ONLY
        
        # call method to run the query in Q3
        result = process_query(preprocessed_query, invertedIndex, len(documents))

        # output results after query is executed (need to do)
        '''
        Output:
        Number of matched documents: 270
        Minimum number of comparisons required: 671
        List of retrieved document names
        '''
        # output required info
        print("Number of matched documents: " + str(len(result)))
        print("Minimum number of comparisons required: We need to record/get this")
        print("List of retrieved document names")

        # output the file names
        for documentId in result:
            print(documents[documentId] + " | Id= " + str(documentId))
    
    