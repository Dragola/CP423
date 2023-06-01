from Q2 import InvertedIndex

def evaluate_query(x, y):
    # Convert x to boolean based on the number
    if x != 0:
        x = True
    else:
        x = False

    # Convert y to boolean based on the number
    if y != 0:
        y = True
    else:
        y = False

    # Evaluate x OR y
    query_or = x or y

    # Evaluate x AND y
    query_and = x and y

    # Evaluate x AND NOT y
    query_and_not = x and not y

    # Evaluate x OR NOT y
    query_or_not = x or not y

    # Return the results
    return query_or, query_and, query_and_not, query_or_not


# Inverted index mapping words to numbers
invertedIndex = InvertedIndex() 
invertedIndex.addIndex("apple", 1)
invertedIndex.addIndex("banana", 2)
invertedIndex.addIndex("cat", 3)
invertedIndex.addIndex("dog", 4)

indexList = invertedIndex.indexList
invertedIndex.printIndexList()

# Test the function
word_x = input("Enter the value of x (word): ")
word_y = input("Enter the value of y (word): ")

# Get the corresponding numbers from the inverted index
x = indexList[word_x]
y = indexList[word_y]

result_or, result_and, result_and_not, result_or_not = evaluate_query(x, y)

print(f"x OR y: {result_or}")
print(f"x AND y: {result_and}")
print(f"x AND NOT y: {result_and_not}")
print(f"x OR NOT y: {result_or_not}")
