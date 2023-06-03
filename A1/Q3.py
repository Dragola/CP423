from Q2 import InvertedIndex

def process_query(query: str, inverted_index: InvertedIndex, totalDocumentID: int):
    # break down query and process
    query = query.strip().split()

    # check that query is valid (minimum: word | operation | word). Query can have more
    if len(query) < 3:
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
        if query[i + 1].upper() == "NOT":
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
        if operator.upper() == "AND":
            result = firstPostingList.intersection(secondPostingList)
        elif operator.upper() == "OR":
            result = firstPostingList.union(secondPostingList)
        else:
            # if word isn't AND/OR then we should print to indicate the error
            return None

    return result


# Inverted index mapping words to numbers
invertedIndex = InvertedIndex()
invertedIndex.addIndex("apple", 1)
invertedIndex.addIndex("apple", 2)
invertedIndex.addIndex("banana", 2)
invertedIndex.addIndex("banana", 3)
invertedIndex.addIndex("cherry", 1)
invertedIndex.addIndex("cherry", 3)
invertedIndex.addIndex("orange", 2)
invertedIndex.addIndex("berry", 1)

invertedIndex.printIndexList()

# testing
user_input = input("Enter the query: ")
result = process_query(user_input, invertedIndex, 3)
print(f"Result: {result}")
