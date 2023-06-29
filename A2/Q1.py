# imports
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

'''
PositionalIndex:
 - Stores a list of key-value pair for the tokens and their data.
    - The key is the word/token.
    - The value is a list. The first element of the list is the document frequency. The second is another dict that maps the doc ID's to a positional list (set).
'''
class PositionalIndex:
    indexList: dict

    def __init__(self):
       # create new dict on object initialization
       self.indexList = {}
	
    # adds/updates an index
    def addIndex(self, word: str, documentID: int, position: int):
        # check if word exists in the dict
        if word in self.indexList:

            # check if doc ID is already in dict
            if documentID in self.indexList[word][1]:
                # add the position to the list
                newPosition = {position}
                self.indexList[word][1][documentID].update(newPosition)

            # if doc ID doesn't exist
            else:
                # increment doc freq as a new doc is added to the list
                self.indexList[word][0] += 1

                # add the doc ID and set the position list
                newPosition = {position}
                self.indexList[word][1][documentID] = (newPosition)


        # if word isn't in dict
        else:
            # add the word to the dict with a new list containing the doc freq and dict for doc ID and positional list
            newDict: dict = {}
            self.indexList[word] = [1, newDict]

            # add the doc ID + position to the inner dict
            newPosition = {position}
            self.indexList[word][1][documentID] = newPosition

    # print the list of inverted index's (DEBUG)
    def printIndexList(self):
        print("Printing inverted Index...", end="\n")
        for word in self.indexList:
            print("Document Frequency = " + str(self.indexList[word][0]))
            print(word + ": ", end= "")
            print(self.indexList[word], end= "\n")
        print("\n")

'''
Tests for the PositionalIndex class
'''
# add a single word
def test_single_word_single_doc_single_position():
    print("test_single_word_single_doc_single_position:")
    index = PositionalIndex()

    index.addIndex("word", 1, 1)

    index.printIndexList()

# add the same word and document but different positions
def test_single_word_single_doc_multi_position():
    print("test_single_word_single_doc_multi_position:")
    index = PositionalIndex()

    index.addIndex("word", 1, 1)
    index.addIndex("word", 1, 2)
    index.addIndex("word", 1, 3)
    index.addIndex("word", 1, 4)
    index.addIndex("word", 1, 5)

    index.printIndexList()

# add the same word with different documents and different positions
def test_single_word_multi_doc_multi_position():
    print("test_single_word_multi_doc_multi_position:")
    index = PositionalIndex()

    index.addIndex("word", 1, 2)
    index.addIndex("word", 2, 4)
    index.addIndex("word", 3, 6)
    index.addIndex("word", 4, 8)
    index.addIndex("word", 5, 10)

    index.printIndexList()

'''
Function for preprocessing the text
'''
def preprocess_text(text):
   # convert all text to lowercase
   text = text.lower()

   # tokenization of text
   tokens = word_tokenize(text)
   
   # removing stopwords
   stop_words = set(stopwords.words('english'))
   tokens = [token for token in tokens if token not in stop_words]

   # excluding special characters
   tokens = [re.sub('[^a-zA-Z]', ' ', token) for token in tokens]

   # remove whitespace in tokens
   tokens = [token.strip() for token in tokens]

   # eliminating single character words
   tokens = [token for token in tokens if len(token) > 1]
   
   return tokens

if __name__ == "__main__":
    #print("Main for Q1")
    test_single_word_single_doc_single_position()
    test_single_word_single_doc_multi_position()
    test_single_word_multi_doc_multi_position()