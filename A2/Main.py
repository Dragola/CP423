# imports
from Q1 import PositionalIndex, preprocess_text, search_phrase
from Q2 import *
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

        # tokenize the file text
        uniqueWords = preprocess_text(text)
        
        # add the words/tokens from the token list into the position index
        for word in uniqueWords:
            invertedIndex.addIndex(word, documentId, uniqueWords[word])

        # close the file after reading it
        stream.close()

        # add the document to the list of documents
        document: dict = {documentId: file}
        documents.update(document)
        
        # increment the document ID for the next file
        documentId += 1

    return invertedIndex

# output based on lecture slide (Week 2- Part 2 SLide 9) #DEBUG
def writePositionalIndex():
    stream = open("./positionalIndex.txt", "w")


    # print document and their ID's
    for docID in documents:
        stream.write(documents[docID] + "| docID= " + str(docID) + "\n")

    # space for index
    stream.write("\n")

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

def checkToLoadDataFiles():
    global positionalIndex

    # generate positional index only if it wasn't generated previously
    if (positionalIndex == None):
        print("Creating Positional Index...")

        # read all the files and create the inverted index
        positionalIndex = createPositionalIndex()

        print("Finished creating Positional Index.")

        # write index to txt file #DEBUG
        writePositionalIndex()

'''
Main function
'''
if __name__ == "__main__":
    option = ""

    # keep asking for an option until program is exited
    while option != "0":
        print("Options:")
        print("0 = Exit program\n")
        print("1 = Phrase Query\n")
        print("2 = TD-IDF\n")
        print("3 = Cosine\n")

        # get input
        option = input("Enter an option: ")

        # attempt to get int value from input
        try:
            option_num = int(option)
        except:
            print("That's not a number, please try again with a number")
            option_num = -1

        match option_num:
            case -1: # no number provided (skip)
                print("\n")

            case 0: # exit program
                exit()

            case 1: # phrase query
                # TODO- Does this need to be processed (remove stop words or punctuation?) or just pass it in?
                phrase = input("Enter a phrase to query: ")

                checkToLoadDataFiles()

                # run the function for phrase query
                result_list = search_phrase(positionalIndex.indexList, phrase)

                # output the result
                # TODO- Should print the position the phrase starts at.
                print("Documents that contain the phrase" + result_list)

            case 2: # TD-IDF
                checkToLoadDataFiles()
                
                # generate the TF-IDF matrix
                td_ifd_matrix = generate_tfidf_matrix()

                # create query vector

                # call other functions that need to be called for this

                # output result

            case 3: # Cosine
                print("Cosine option")
                checkToLoadDataFiles()

                # call functions to run this

                # output result
                
            case _:
                print("Invalid option")
                