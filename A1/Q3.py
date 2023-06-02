from Q2 import InvertedIndex

def process_query(query, inverted_index):
    query = query.strip().split()

    if len(query) != 3:
        return None

    x = set(inverted_index.indexList.get(query[0], []))
    operator = query[1]
    y = set(inverted_index.indexList.get(query[2], []))

    if operator == "OR":
        result = x.union(y)
    elif operator == "AND":
        result = x.intersection(y)
    elif operator == "AND" and query[2] == "NOT":
        result = x.difference(y)
    elif operator == "OR" and query[2] == "NOT":
        result = x.union(inverted_index.indexList.keys()).difference(y)
    else:
        return None

    return result


# Inverted index mapping words to numbers
invertedIndex = InvertedIndex()
invertedIndex.addIndex("apple", 1)
invertedIndex.addIndex("banana", 2)
invertedIndex.addIndex("cat", 3)
invertedIndex.addIndex("cat", 4)
invertedIndex.addIndex("dog", 4)

indexList = invertedIndex.indexList
invertedIndex.printIndexList()

# testing
user_input = input("Enter the query: ")
result = process_query(user_input, invertedIndex)
print(f"Result: {result}")
