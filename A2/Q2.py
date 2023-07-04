# imports
import numpy as np
from Q1 import *
# Properties

#generate matrix
def generate_matrix(document_count:int, positional_index:PositionalIndex):
    row = document_count
    col = len(positional_index.indexList)
    return (np.array([0]*row*col, dtype = "float").reshape(row,col))
    
def tf_idf(word, docID, pos_ind:PositionalIndex, document_count:int):
    tf = float(len(pos_ind.indexList[word][1][docID]))
    idf = float(document_count)/float(pos_ind.indexList[word][0])
    result = tf*idf
    print(result)
    return result

def generate_tfidf_matrix(document_count:int, pos_ind:PositionalIndex):
    row = 0
    col = 0
    matrix = generate_matrix(document_count, pos_ind)
    for word in pos_ind.indexList:
        for doc in pos_ind.indexList[word][1]:
            tfidf = tf_idf(word, doc, pos_ind, document_count)
            matrix[row][col]= tfidf
            row += 1
        col += 1 
        row = 0  
    return matrix
   
def query_vector(query,term_count, pos_ind:PositionalIndex):
    query_vector = np.array([0]*(term_count))
    col = 0
    for word in pos_ind.indexList:
        if word in query:
            query_vector[col] = 1
        col += 1
    return query_vector
    
def calculate_tf_idf ():
    
    
         
            
if __name__ == "__main__":
    print("Main for Q2")
    
    
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

    """matrix = generate_matrix(3, index)
    print(matrix)
    tfidf = tf_idf("apple", 1, index, 3)
    """
    matrix = generate_tfidf_matrix(3, index)
    print(matrix)
    queryvector = query_vector("apple", 4, index)
    print(queryvector)