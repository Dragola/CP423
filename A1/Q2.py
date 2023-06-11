'''
IndexList:
 - Stores a list of key-value pair for the tokens and posting lists.
    - The key is the word/token.
    - The value is the posting list that's stored in a set array. This is so that when adding documentID's there are no duplicate ID's.
'''
class InvertedIndex:
    indexList: dict

    def __init__(self):
       # create indexList on object initialization
       self.indexList = {}
    
    # adds/updates an index
    def addIndex(self, word: str, documentID: int):

        # check if index already exists in the dictionary
        if word in self.indexList:
            newDocumentID = {documentID}
            # add document ID to existing index
            self.indexList[word].update(newDocumentID) 

        # if index wasn't already in list
        else:
            # create a new set with the initial document ID
            newSet = {documentID} 

            # add index to the dictionary with the document ID set
            self.indexList[word] = newSet 

    # print the list of inverted index's (DEBUG)
    def printIndexList(self):
        print("Printing inverted Index...", end="\n")
        for index in self.indexList:
            print(index + " --> ", end= "")
            print(self.indexList[index], end= "\n")
        print("\n")

'''
Tests for the InvertedIndex class
'''
# add a single word with one document ID
def test_single_index_single_doc():
    print("test_single_index_single_doc:")
    index = InvertedIndex()

    index.addIndex("word", 1)

    index.printIndexList()

# add multiple words with 1 document ID each
def test_multiple_index_single_doc():
    print("test_multiple_index_single_doc:")
    index = InvertedIndex()

    index.addIndex("word1", 1)
    index.addIndex("word2", 1)
    index.addIndex("word3", 2)
    index.addIndex("word4", 3)
    index.addIndex("word5", 5)

    index.printIndexList()

# add a sginel word but with multiple docuemnt ID's
def test_single_index_multi_doc():
    print("test_single_index_multi_doc:")
    index = InvertedIndex()

    index.addIndex("word", 1)
    index.addIndex("word", 2)
    index.addIndex("word", 3)
    index.addIndex("word", 4)
    index.addIndex("word", 5)

    index.printIndexList()


# add multiple words with multiple document ID's in each word
def test_multiple_index_multi_doc():
    print("test_multiple_index_multi_doc:")
    index = InvertedIndex()

    index.addIndex("word1", 1)
    index.addIndex("word1", 2)
    index.addIndex("word1", 3)

    index.addIndex("word2", 4)
    index.addIndex("word2", 5)
    index.addIndex("word2", 6)

    index.addIndex("word3", 7)
    index.addIndex("word3", 8)
    index.addIndex("word3", 9)

    index.addIndex("word4", 10)
    index.addIndex("word4", 11)
    index.addIndex("word4", 12)

    index.addIndex("word5", 13)
    index.addIndex("word5", 14)
    index.addIndex("word5", 15)

    index.printIndexList()

# only runs tests if this file is being run
# if __name__ == "__main__":
#     test_single_index_single_doc()
#     test_multiple_index_single_doc()
#     test_single_index_multi_doc()
#     test_multiple_index_multi_doc()