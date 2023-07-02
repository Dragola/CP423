# imports
from Q1 import PositionalIndex, preprocess_text
import os

# Properties
# the list of ID's to document names- used in output
documents: dict = {}

# the Positional Index that will hold all the document data
positionalIndex: PositionalIndex = None

'''
Reads all the documents in the data folder, tokenize the text, and stores it in the Inverted Index data structure.
'''
def createPositionalIndex():
    global documents

    # create new Inverted Index from Q2
    invertedIndex = PositionalIndex()

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
        
        wordPosition = 1

        # add the words/tokens from the token list into the position index list
        for word in uniqueWords:
            invertedIndex.addIndex(word, documentId, wordPosition)
            wordPosition += 1

        # close the file after reading it
        stream.close()

        # add the document to the list of documents
        document: dict = {documentId: file}
        documents.update(document)
        
        # increment the document ID for the next file
        documentId += 1

    return invertedIndex

# output based on lecture slide (Week 2- Part 2 SLide 9) (DEBUG ONLY)
def writePositionalIndex():
    stream = open("./positionalIndex.txt", "w")
    for word in positionalIndex.indexList:
        # print first line (word/token + document frequency)
        firstLine = "{" + word + ": (" + str(positionalIndex.indexList[word][0]) + ", {\n"
        stream.write(firstLine)

        # determine what's the last element in the docID dict (to determine line format)
        docDict: dict = positionalIndex.indexList[word][1]
        docDictToList: list = list(docDict.keys())
        lastElement = docDictToList[-1]

        # print each docId and positional list
        for doc in positionalIndex.indexList[word][1]:
            # first to second last element in list
            if doc != lastElement:
                docLine = "doc" + str(doc) + ": [" + str(positionalIndex.indexList[word][1][doc]) + "],\n"
            # last element in list
            else:
                docLine = "doc" + str(doc) + ": [" + str(positionalIndex.indexList[word][1][doc]) + "]} )\n"
            stream.write(docLine)

        # write last line for word/token
        stream.write("}\n\n")
    stream.close()

'''
Main function- we'll use this one to use Q1 and Q2
'''
if __name__ == "__main__":
    # generate invertedIndex only if it wasn't generated previously
    if (positionalIndex == None):
        print("Creating Positional Index...")

        # read all the files and create the inverted index (Q2)
        positionalIndex = createPositionalIndex()

        print("Finished creating Positional Index.")

    # write index to txt file
    writePositionalIndex()