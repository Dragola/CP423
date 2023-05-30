'''
IndexList:
 - Stores key-value pairs (aka index - documentID list).
    - The key is the word/token.
    - The value is a set that holds the document ID's for the word/token.
'''
class InvertedIndex:
    indexList: dict

    def __init__(self):
       self.indexList = {}
    
    # adds/updates an index
    def addIndex(self, word: str, document: int):

        # check if index already exists in the dictionary
        if word in self.indexList:
            self.indexList[word].add(document) # add document ID to existing index

        # if index wasn't already in list
        else:
            newSet = {document} # create a new set and add the document ID to it
            self.indexList[word] = newSet # add index to the dictionary with the document ID

    # print the list of inverted index's
    def printIndex(self):
        print("Printing inverted Index...", end="\n\n")
        for index in self.indexList:
            print(index + " --> ", end= "")
            print(self.indexList[index], end= "\n")


'''
Tests for the InvertedIndex class
'''
# add a single word with one document ID
def test_single_index_single_doc():
    index = InvertedIndex()

    index.addIndex("word", 1)

    index.printIndex()

# add multiple words with 1 document ID each
def test_multiple_index_single_doc():
    index = InvertedIndex()

    index.addIndex("word1", 1)
    index.addIndex("word2", 1)
    index.addIndex("word3", 2)
    index.addIndex("word4", 3)
    index.addIndex("word5", 5)

    index.printIndex()

# add a sginel word but with multiple docuemnt ID's
def test_single_index_multi_doc():
    index = InvertedIndex()

    index.addIndex("word", 1)
    index.addIndex("word", 2)
    index.addIndex("word", 3)
    index.addIndex("word", 4)
    index.addIndex("word", 5)

    index.printIndex()


# add multiple words with multiple document ID's in each word
def test_multiple_index_multi_doc():
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

    index.printIndex()

if __name__ == "__main__":
    test_single_index_single_doc()
    test_multiple_index_single_doc()
    test_single_index_multi_doc()
    test_multiple_index_multi_doc()