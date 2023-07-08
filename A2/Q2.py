# imports
import numpy as np #required to generate matrix
import math as math #required to perform log functions

from numpy.linalg import norm

from Q1 import *
# Properties

#generate matrix, fill with zeros
def generate_matrix(document_count:int, positional_index:PositionalIndex):
    row = document_count
    col = len(positional_index.indexList)
    return (np.array([0]*row*col, dtype = "float").reshape(row,col))

#calculate tfidf using the different weighting schemes for term frequency
def tf_idf(word, docID, pos_ind:PositionalIndex, document_count:int, weight_scheme):
    #binary 
    if weight_scheme == 1:
        if word in pos_ind.indexList:
            tf = float(1)
        else: 
            tf = float(0)
    #raw count
    elif weight_scheme == 2:
        tf = float(len(pos_ind.indexList[word][1][docID]))
    #term frequency
    elif weight_scheme == 3:
        tf = float(len(pos_ind.indexList[word][1][docID]))
        value = 0
        for word in pos_ind.indexList:
            tf = tf/(value + pos_ind.indexList[word][1][docID])
    #log Normalization
    elif weight_scheme == 4:
        tf = math.log((1+len(pos_ind.indexList[word][1][docID])), 10)
    #double normalization
    elif weight_scheme == 5:
        tf = float(len(pos_ind.indexList[word][1][docID]))
        max = float(len(pos_ind.indexList[word][1][docID]))
        for word in pos_ind.indexList[word][1][docID]:
            if pos_ind.indexList[word][1][docID] > max:
                max = pos_ind.indexList[word][1][docID]
            tf = tf/max   
        tf = 0.5+0.5 *tf       
    #none of the above options returns an error
    else: 
        print("Error: that is not a valid weight scheme.")
        return -1

    idf = float(document_count)/float(pos_ind.indexList[word][0]) + 1
    result = tf*(math.log(idf,10))
    print(result)
    return result

#populate matrix with tfidf generated values
def generate_tfidf_matrix(pos_ind:PositionalIndex, document_count:int, weight_scheme: int):
    col = 0

    #generate the matrix
    matrix = generate_matrix(document_count, pos_ind)

    #calculate the tf-idf for each word and put value in the matrix
    for word in pos_ind.indexList:
        for doc in pos_ind.indexList[word][1]:
            tfidf = tf_idf(word, doc, pos_ind, document_count, weight_scheme)
            matrix[doc -1][col]= tfidf
        col += 1 
    return matrix

#create query vector
def query_vector(query,term_count, pos_ind:PositionalIndex):
    query_vector = np.array([0]*(term_count))
    col = 0
    for word in pos_ind.indexList:
        if word in query:
            query_vector[col] = 1
        col += 1
    return query_vector

#calculate tfidf score by multiplying query vector with the tfidf values
def calculate_tf_idf (query_vector, word, docID, pos_ind:PositionalIndex, document_count:int, weight_scheme):
    value = tf_idf(word, docID, pos_ind, document_count, weight_scheme)
    result = value * query_vector
    return (result)

#return top 5 relevent documents by returning top 5 tfidf scores
def relevant_doc (result): 
    score = 0
    list = []
    #calculate tfidf scores at each matrix position and append them to a list then sort the list in descending scores
    for i in matrix:
        for j in matrix:
            score = calculate_tf_idf(query_value, word, docID, pos_ind, document_count, weight_scheme)
            list.append(score)
    list.sort(reverse=True)
    return list[:5]

#returns top 5 relevant documents based on cosine similarity scores
def cosine_sim(query_tfidf_scores, tfidf_matrix):

    cosine_scores = np.dot(query_tfidf_scores, tfidf_matrix)/(norm(query_tfidf_scores)*norm(tfidf_matrix))

    top_5 = np.argsort(cosine_scores, axis=1)[0][::-1][:5]

    return top_5
    

if __name__ == "__main__":
    
    #Testing
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
    matrix = generate_tfidf_matrix("apple", 1, index, 4, 1)
    print(matrix)
    queryvector = query_vector("apple", 4, index)
    print(queryvector)
    ##tf_idf_score = calculate_tf_idf (query_vector, "apple", 1, index, 4, 1)
    ##print(tf_idf_score)
    
