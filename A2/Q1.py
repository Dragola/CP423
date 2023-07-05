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
        print("Printing inverted Index:", end="\n")
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
- TODO- Positions don't seen accurate for some words (could be before or after the actual position), need to look into.
'''
def preprocess_text(text) -> list[dict]:
   # convert all text to lowercase
   text = text.lower()

   # tokenization of text
   tokens = word_tokenize(text)

   token_with_position: dict = {}
   position = 1
   # determine the positions of each token
   for token in tokens:
       token_with_position[token] = position
       position += 1
   
   # removing stopwords
   stop_words = set(stopwords.words('english'))
   tokens = [token for token in tokens if token not in stop_words]

   # excluding special characters
   tokens = [re.sub('[^a-zA-Z]', ' ', token) for token in tokens]

   # remove whitespace in tokens
   tokens = [token.strip() for token in tokens]

   # eliminating single character words
   tokens = [token for token in tokens if len(token) > 1]

   # check what tokens where removed and return a new dict containing only the valid tokens with their positions
   result: dict = {}
   for token in token_with_position:
       if token in tokens:
           result[token] = token_with_position[token]
   return result

'''
Function for searching phrase queries
'''
def search_phrase(index_list, processed_text: list):
    query_words = processed_text
    query_length = len(query_words)

    # Check if the phrase length is greater than 5
    if query_length > 5:
        raise ValueError("Query length should be equal to or less than 5.")

    # Find the documents containing the first word in the phrase
    first_word = query_words[0]
    if first_word not in index_list:
        return []
    first_word_docs = index_list[first_word][1]

    # Initialize the result list with the document IDs from the first word
    result = list(first_word_docs.keys())

    # Iterate over the remaining words in the phrase
    for i in range(1, query_length):
        word = query_words[i]
        if word not in index_list:
            return []
        word_docs = index_list[word][1]

        # Merge the document IDs with the previous result
        result = merge(result, list(word_docs.keys()))

        # If the result becomes empty, no need to continue
        if not result:
            return []

        # Check for positional proximity within the same document
        result = check_positional_proximity(result, first_word_docs, word_docs, i)

        # If the result becomes empty, no need to continue
        if not result:
            return []

    return result

def merge(list1, list2):
    # Merge algorithm to combine document IDs
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            merged.append(list1[i])
            i += 1
            j += 1
    return merged

def check_positional_proximity(result, first_word_docs, word_docs, proximity):
    # Check positional proximity within the same document
    updated_result = []
    for doc_id in result:
        first_word_positions = first_word_docs[doc_id]
        word_positions = word_docs[doc_id]

        for position1 in first_word_positions:
            for position2 in word_positions:
                if abs(position1 - position2) == proximity:
                    updated_result.append(doc_id)
                    break
            if doc_id in updated_result:
                break
    return updated_result

''''
Run tests for Q1 functions (DEBUG)
'''
if __name__ == "__main__":
    '''
    Tests for Positional Index
    '''
    test_single_word_single_doc_single_position()
    test_single_word_single_doc_multi_position()
    test_single_word_multi_doc_multi_position()

    '''
    Tests for the Phrase queries function
    '''
    print("Testing phrase queries...\n")
    index = PositionalIndex()

    # Add some sample data
    index.addIndex("apple", 1, 2)
    index.addIndex("apple", 2, 1)
    index.addIndex("with", 2, 2)
    index.addIndex("apple", 3, 9)
    index.addIndex("banana", 1, 3)
    index.addIndex("banana", 2, 2)
    index.addIndex("banana", 2, 3)
    index.addIndex("orange", 2, 4)
    index.addIndex("orange", 3, 8)

    index.printIndexList()

    # Test the search_phrase function
    query = "apple with banana"
    result = search_phrase(index.indexList, query)
    print(f"Search Query: '{query}'")
    print(f"Result: {result}")

    query = "banana orange"
    result = search_phrase(index.indexList, query)
    print(f"Search Query: '{query}'")
    print(f"Result: {result}")

    query = "apple banana"
    result = search_phrase(index.indexList, query)
    print(f"Search Query: '{query}'")
    print(f"Result: {result}")