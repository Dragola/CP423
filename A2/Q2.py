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
def tf_idf(word: str, docID: int, pos_ind:PositionalIndex, document_count:int, weight_scheme: int):
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
    #none of the above options returns an error (no need if we prevent before calling)
    else: 
        print("Error: that is not a valid weight scheme.")
        return -1

    idf = float(document_count)/float(pos_ind.indexList[word][0]) + 1
    result = tf*(math.log(idf,10))
    #print(result)
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
def query_vector(query: list, term_count, pos_ind:PositionalIndex):
    query_vector = np.array([0]*(term_count))
    col = 0
    for word in pos_ind.indexList:
        if word in query:
            query_vector[col] = 1
        col += 1
    return query_vector

#calculate tfidf score by multiplying query vector with the tfidf values
def calculate_tf_idf (query_vector, word, docID, pos_ind:PositionalIndex, document_count:int, weight_scheme: int):
    value = tf_idf(word, docID, pos_ind, document_count, weight_scheme)
    result = value * query_vector
    return (result)

#return top 5 relevent documents by returning top 5 tf-idf scores
def relevant_doc(query_vector, tf_idf_matrix): 
    #calculate tfidf scores at each matrix position and append them to a list then sort the list in descending scores
    scores = np.dot(query_vector, tf_idf_matrix)

    print("\nScores:")
    print(scores)

    # determine the order of the scores (sorts lowest to highest)
    sorted_indecies = np.argsort(scores)

    # reverse the index's from the sorted list and grab the first 5 (aka 5 highest relevant docID's)
    top_5_doc = sorted_indecies[::-1][-5:]

    return top_5_doc

#returns top 5 relevant documents based on cosine similarity scores
#TODO- Need to run for all 5 TF weight calculations
def cosine_sim(query_vector, tfidf_matrix):

    # get the dot product
    cosine_scores = np.dot(query_vector, tfidf_matrix)/(norm(query_vector)*norm(tfidf_matrix))
    
    print("\nCosine Scores:")
    print(cosine_scores)

    # determine the order of the scores (sorts lowest to highest)
    sorted_indecies = np.argsort(cosine_scores)

    # reverse the index's from the sorted list and grab the first 5 (aka 5 highest relevant docID's)
    top_5_doc = sorted_indecies[::-1][-5:]

    return top_5_doc
    

if __name__ == "__main__":
    
    #Testing
    print("Main for Q2")
    
    print("Testing phrase queries...\n")
    index = PositionalIndex()

    # Add some sample data
    index.addIndex("apple", 1, 2)
    index.addIndex("apple", 2, 1)
    index.addIndex("apple", 3, 9)
    index.addIndex("with", 2, 2)
    index.addIndex("banana", 1, 3)
    index.addIndex("banana", 2, 2)
    index.addIndex("banana", 2, 3)
    index.addIndex("orange", 2, 4)
    index.addIndex("orange", 3, 8)

    # print positional index structure
    index.printIndexList()

    # generate TF-IDF matrix
    matrix = generate_tfidf_matrix(index, 4, 1)
    print("\nTF-IDF Matrix:")
    print(index.indexList.keys())
    print(matrix)
    
    # create query vector
    query_vec = query_vector(["apple"], 4, index)
    print("\nQuery vector:")
    print(query_vec)

    # test TD-IDF
    top = relevant_doc(query_vec, matrix)
    print("\nTF-IDF Result:")
    print("Top 5 dopcumets are:")
    for doc in top:
        print("Document " + str(doc + 1) + " (index " + str(doc) + ")")

    # test cosine similarity
    top_cosine = cosine_sim(query_vec, matrix)
    print("\nCosine Similarity Result:")
    print("Top 5 dopcumets are:")
    for doc in top:
        print("Document " + str(doc + 1) + " (index " + str(doc) + ")")
