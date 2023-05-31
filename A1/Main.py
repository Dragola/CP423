from Q1 import preprocess_text
from Q2 import InvertedIndex
import os

files: list[str] # the files that we index from

def retrieveFiles():
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
        
if __name__ == "__main__":
    # process the input
    '''
    Input sentence: “lion stood thoughtfully for a moment”
    Input operation sequence: [OR, OR, OR]

    Expected preprocessed query: “lion OR stood OR thoughtfully OR moment”
    '''

    invertedIndex = retrieveFiles() # read all the files and create the inverted index

    # output the inverted index to verify (DEBUG ONLY)
    file = open("./InvertedIndex.txt", "w")

    invertedIndexDictionary = invertedIndex.indexList
    for index in invertedIndexDictionary:
        file.write(index)
        file.write(" --> ")
        file.write(invertedIndexDictionary[index])
        file.write("\n")
    
    file.close()

    # call method to run the query- Q3

    # output results after query is executed
    '''
    Output:
    Number of matched documents: 270
    Minimum number of comparisons required: 671
    List of retrieved document names
    '''