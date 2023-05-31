# imports

from collections import Counter
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')


def preprocess_text(text):
    
    '''
    Function for preprocessing the text
    '''
    
    # convert all text to lowercase
    text = text.lower()

    # tokenization of text
    tokens = word_tokenize(text)
    
    # removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # excluding special characters
    tokens = [re.sub(r'[^a-zA-Z0-9]', '', token) for token in tokens if token]

    # eliminating singly occuring characters
    word_counts = Counter(tokens)
    tokens = [token for token in tokens if word_counts[token] > 1]
    
    # creating set of all the words
    unique_words = set(tokens)
    
    return unique_words
