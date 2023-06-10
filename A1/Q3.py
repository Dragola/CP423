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
    # counter for AND operator ()
    total_comparisons = 0
    
    # break down query and process
    query = query.strip().split()

    # check if all words in the query exist in the inverted index
    for word in query:
        if word not in inverted_index.indexList and word not in ["AND", "OR", "NOT"]:
            print(f"Error: Word '{word}' does not exist in the inverted index.")
            return None
        
    # grab the posting list for the first word in the query
    firstPostingList = set(inverted_index.indexList[query[0]]) 
    
    # operator index in the query list
    i = 1

    # list of all the documentID's (used for NOT operator)
    totalPostingList = []
    for j in range(totalDocumentID):
        totalPostingList.append(j)

    # create empty set for the resulting posting list
    result = list()

    # Split the query into operators and operands
    while i < len(query):

        # grab previous posting list if this isn't the first operation in query
        if (len(result) > 0):
            print("Another operator, grabbing previous result") #DEBUG
            firstPostingList = result

        # get the operator
        operator = query[i]
        
        # if NOT is used 
        if query[i + 1] == "NOT":
            # flip the posting list for the second word
            secondPostingList = set(totalPostingList) - set(inverted_index.indexList[query[i + 2]])
            
            # skip over the word for next operator (if there is)
            i += 3 
        # if NOT isn't used
        else:
            # get the posting list for the second word
            secondPostingList = set(inverted_index.indexList[query[i + 1]])

            # skip over the word for next operator (if there is)
            i += 2 

        # sort the lists before doing the operation
        firstPostingList = sorted(firstPostingList)
        secondPostingList = sorted(secondPostingList)

        # clear result for the operation
        result = list()

        # varaibles for the operation
        p1 = 0
        p2 = 0

        # Apply the AND operation
        if operator == "AND":  
            # while pointers haven't reaches the ends of the lists
            while p1 < len(firstPostingList) and p2 < len(secondPostingList):
                
                # if id's match
                if firstPostingList[p1] == secondPostingList[p2]:
                    # append to list and move both pointer
                    result.append(firstPostingList[p1])
                    p1 += 1
                    p2 += 1
                # if the first posting list's value is lower
                elif firstPostingList[p1] < secondPostingList[p2]:
                    # move first pointer
                    p1 += 1
                # if the second posting list's value is lower
                else:
                    # move second pointer
                    p2 += 1
                
                # increment counter
                total_comparisons += 1
        
        # apply the OR operator
        elif operator == "OR":
            # go through the id's in the first posting list
            while p1 < len(firstPostingList):
                
                # check if second pointer is still valid index
                if (p2 < len(secondPostingList)):
                    print("p2 valid")
                    # if the first posting list's value is lower
                    if firstPostingList[p1] < secondPostingList[p2]:
                        # append to list and move first pointer
                        result.append(firstPostingList[p1])
                        p1 += 1
                    # if the second posting list's value is lower 
                    else:
                        # append to list and move second pointer
                        result.append(secondPostingList[p2])
                        p2 += 1

                    # increment counter
                    total_comparisons += 1
                # if second pointer is invalid then just add from first list
                else:
                    print("p2 bad")
                    # append to list and move first pointer
                    result.append(firstPostingList[p1])
                    p1 += 1

            # add the remaining id's from the second posting list
            while p2 < len(secondPostingList):
                result.append(secondPostingList[p2])
                p2 +=1
                
    return result, total_comparisons


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

    # print the inverted index
    invertedIndex.printIndexList()

    # get query
    user_input = input("Enter the query: ")

    # process query
    result, total_comparisons = process_query(user_input, invertedIndex, 3)

    # print result
    print(f"Result: {result}")
    print("Total comparisons= " + str(total_comparisons))
