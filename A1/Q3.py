from Q2 import InvertedIndex

def process_query(query, inverted_index):
    # break down query and process
    query = query.strip().split()

    # check input
    if len(query) < 3 or len(query) % 2 != 1:
        return None

    result = set(inverted_index.indexList.get(query[i + 1], []))
    i = 1

    # Split the query into operators and operands
    while i < len(query):
        operator = query[i]
        operand = set(inverted_index.indexList.get(query[i + 1], []))

        # Apply the operators accordingly
        if operator == "AND":
            result = result.intersection(operand)
        elif operator == "OR":
            result = result.union(operand)
        elif operator == "AND" and query[i + 1] == "NOT":
            result = result.difference(operand)
        elif operator == "OR" and query[i + 1] == "NOT":
            result = result.union(inverted_index.indexList.keys()).difference(operand)
        else:
            return None

        i += 2

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
result = process_query(user_input, invertedIndex)
print(f"Result: {result}")
