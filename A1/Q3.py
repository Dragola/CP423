from Q2 import InvertedIndex

'''
Verify if the query meets certain requirements
'''
def check_query_format_valid(query: str):
    # break down query and process
    query = query.strip().split()
    
    # check that query is valid (minimum: word | operation | word). Query can have more
    if len(query) < 3:
        print("Error: Query must contain at least two words and one operator.")
        return False
    
    # check if any of the required operators are missing
    if "AND" not in query and "OR" not in query and "NOT" not in query:
        print("Error: Query must contain at least one of the operators AND, OR, or NOT (case sensitive).")
        return False
    
    return True

'''
Process the query and return the resulting posting list
'''
def process_query(query: str, inverted_index: InvertedIndex, totalDocumentID: int):
    # break down query and process
    query = query.strip().split()

    # check if all words in the query exist in the inverted index
    for word in query:
        if word not in inverted_index.indexList and word not in ["AND", "OR", "NOT"]:
            print(f"Error: Word '{word}' does not exist in the inverted index.")
            return None
        
    # grab the posting list for the first word in the query
    firstPostingList = set(inverted_index.indexList[query[0]]) 
    
    # index in the query list
    i = 1

    # list of all the documentID's (used for NOT operator)
    totalPostingList = []
    for j in range(totalDocumentID):
        totalPostingList.append(j)

    # Split the query into operators and operands
    while i < len(query):
        operator = query[i]
        
        # if NOT is used 
        if query[i + 1] == "NOT":
            # flip the posting list for the second word
            secondPostingList = set(totalPostingList) - set(inverted_index.indexList[query[i + 2]])
            
            # skip over the word for next part of query
            i += 3 
        # if NOT isn't used
        else:
            # get the posting list for the second word
            secondPostingList = set(inverted_index.indexList[query[i + 1]])

            # skip over the word for next part of query
            i += 2 
        
        # Apply the operators accordingly
        if operator == "AND":
            result = firstPostingList.intersection(secondPostingList)
        elif operator == "OR":
            result = firstPostingList.union(secondPostingList)

    return list(sorted(result))

# only runs tests if this file is being run
if __name__ == "__main__":
    # Inverted index mapping words to numbers
    invertedIndex = InvertedIndex()
    invertedIndex.addIndex("apple", 1)
    invertedIndex.addIndex("apple", 2)
    invertedIndex.addIndex("banana", 2)
    invertedIndex.addIndex("banana", 3)
    invertedIndex.addIndex("cherry", 3)
    invertedIndex.addIndex("orange", 6)
    invertedIndex.addIndex("orange", 7)
    invertedIndex.addIndex("berry", 2)
    invertedIndex.addIndex("berry", 4)
    invertedIndex.addIndex("grape", 5)

    invertedIndex.printIndexList()

    # get query
    user_input = input("Enter the query: ")

    # process query
    result = process_query(user_input, invertedIndex, 3)

    # print result
    print(f"Result: {result}")
