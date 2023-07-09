# imports
from Q1 import PositionalIndex, preprocess_text, search_phrase
from Q2 import *
import os

# Properties
# the list of ID's to document names
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
# def writePositionalIndex():
#     stream = open("./positionalIndex.txt", "w")


#     # print document and their ID's
#     for docID in documents:
#         stream.write(documents[docID] + "| docID= " + str(docID) + "\n")

#     # space for index
#     stream.write("\n")

#     for word in positionalIndex.indexList:
#         # print first line (word/token + document frequency)
#         firstLine = "{" + word + ": (" + str(positionalIndex.indexList[word][0]) + ", {\n"
#         stream.write(firstLine)

#         # determine what's the last element in the docID dict (to determine line format)
#         docDict: dict = positionalIndex.indexList[word][1]
#         docDictToList: list = list(docDict.keys())
#         lastElement = docDictToList[-1]

#         # print each docId and positional list
#         for doc in positionalIndex.indexList[word][1]:
#             # first to second last element in list
#             if doc != lastElement:
#                 docLine = "doc" + str(doc) + ": [" + str(positionalIndex.indexList[word][1][doc]) + "],\n"
#             # last element in list
#             else:
#                 docLine = "doc" + str(doc) + ": [" + str(positionalIndex.indexList[word][1][doc]) + "]} )\n"
#             stream.write(docLine)

#         # write last line for word/token
#         stream.write("}\n\n")
#     stream.close()

def checkToLoadDataFiles():
    global positionalIndex

    # generate positional index only if it wasn't generated previously
    if (positionalIndex == None):
        print("\nCreating Positional Index for the first time...")

        # read all the files and create the inverted index
        positionalIndex = createPositionalIndex()

        print("Finished creating Positional Index.\n")

        # write index to txt file #DEBUG
        #writePositionalIndex()

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

        # get phrase
        phrase = input("Enter the query: ")

        # preprocess the phrase
        processed_text: dict = preprocess_text(phrase)

        match option_num:
            case -1: # no number provided (skip)
                print("\n")

            case 0: # exit program
                exit()

            case 1: # phrase query
                # generate the Positional index if it wasn't previously
                checkToLoadDataFiles()

                # create the phrase from the prepro
                phrase = ""
                for word in processed_text.keys():
                    phrase += word + " "

                # run the function for phrase query
                result_list = search_phrase(positionalIndex.indexList, phrase)

                # output the result
                print("Documents that contain the phrase\n")
                print("Read as { DocId: [Positions of the phrase], ...}")
                print(result_list)
                print()

            case 2: # TD-IDF
                # print options for TF-IDF
                print("Pick an option for the TF weight scheme:")
                print("1 = Binary\n")
                print("2 = Raw count\n")
                print("3 = Term Frequency\n")
                print("4 = Log Normalization\n")
                print("5 = Double Normalization\n")
                sub_option = input("Enter an option: ")

                # indication to continue or stop
                bad_input = False

                # attempt to get int value from input
                try:
                    option_num = int(sub_option)
                except:
                    bad_input = True
                
                # check valid option
                if (bad_input == False and option_num < 0 and option_num > 6):
                    bad_input = True
                
                # only continue if input is valid
                if(bad_input == False):
                    # generate the Positional index if it wasn't previously
                    checkToLoadDataFiles()

                    # generate the TF-IDF matrix
                    td_ifd_matrix = generate_tfidf_matrix(positionalIndex, len(documents), option_num)

                    # create query vector
                    query_vec = query_vector(processed_text, len(positionalIndex.indexList), positionalIndex)

                    # find top 5 relevant documents
                    top_5 = relevant_doc(query_vec, td_ifd_matrix, len(documents))
                    print("\nTF-IDF Result:")
                    print("Top 5 dopcumets are:")
                    for doc in top_5:
                        print("Document " + str(doc + 1))
                else:
                    print("Invalid input. Please make sure to enter a number between 1 and 5.\n")

            case 3: # Cosine
                # print options for TF-IDF
                print("Pick an option for the TF weight scheme:")
                print("1 = Binary\n")
                print("2 = Raw count\n")
                print("3 = Term Frequency\n")
                print("4 = Log Normalization\n")
                print("5 = Double Normalization\n")
                sub_option = input("Enter an option: ")

                # indication to continue or stop
                bad_input = False

                # attempt to get int value from input
                try:
                    option_num = int(sub_option)
                except:
                    bad_input = True
                
                # check valid option
                if (bad_input == False and option_num < 0 and option_num > 6):
                    bad_input = True
                
                # only continue if input is valid
                if(bad_input == False):
                    # generate the Positional index if it wasn't previously
                    checkToLoadDataFiles()

                    # generate the TF-IDF matrix
                    td_ifd_matrix = generate_tfidf_matrix(positionalIndex, len(documents), option_num)

                    # create query vector
                    query_vec = query_vector(processed_text, len(positionalIndex.indexList), positionalIndex)

                    # find top 5 relevant documents
                    top_5 = cosine_sim(query_vec, td_ifd_matrix, len(documents))
                    print("\nCosine Similarity Result:")
                    print("Top 5 dopcumets are:")
                    for doc in top_5:
                        print("Document " + str(doc + 1))
                else:
                    print("Invalid input. Please make sure to enter a number between 1 and 5.\n")

            case _:
                print("Invalid option!")
                