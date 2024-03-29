# imports
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

'''
Function for preprocessing the text
'''
def preprocess_text(text):
   # convert all text to lowercase
   text = text.lower()

   # tokenization of text
   tokens = word_tokenize(text)
   
   # removing stopwords
   stop_words = set(stopwords.words('english'))
   tokens = [token for token in tokens if token not in stop_words]

   # excluding special characters
   tokens = [re.sub('[^a-zA-Z]', ' ', token) for token in tokens]

   # remove whitespace in tokens
   tokens = [token.strip() for token in tokens]

   # eliminating single character words
   tokens = [token for token in tokens if len(token) > 1]
   
   return tokens
