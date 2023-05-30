'''
indexList:
 - Stores key-value pairs.
    - the key will be the word/token for the index list
    - the value will be a set for the word/token
'''
class invertedIndex:
    indexList: dict = {}

    #def __init__(self):
        #self
    
    # add index for the word/token
    def addIndex(self, word: str, document: int):
        #check if index exists
        if word in self.indexList:
            previousSet = self.indexList[word] # get the current set

            newSet = previousSet.add(document) # add the document ID to the set

            self.indexList[word] = newSet # replace the set for the work/token
       
        # if word/token wasn't already in list
        else:
            newSet = {document} # new set with document ID added
            self.indexList[word] = newSet # add key and set value to the new set


'''
add some tests to ensure class works as intended:
 - Add a single word with 1, 2 and 5 document ID's
 - Add a few different words (all with 1 document ID)
 - Add a few different words with multiple ID's
'''