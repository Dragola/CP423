from Q1 import preprocess_text
from Q2 import InvertedIndex
#from Q3 import ?
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
def outputInvertedIndex():
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

    invertedIndex = createInvertedIndex() # read all the files and create the inverted index

    # sort the documentID's
    # NOTE: docuemntID set becomes a list
    invertedIndex.sortDocumentIDs()

    outputInvertedIndex() # DEBUG ONLY
    
    # call method to run the query- Q3

    # output results after query is executed (need to do)
    '''
    Output:
    Number of matched documents: 270
    Minimum number of comparisons required: 671
    List of retrieved document names
    '''