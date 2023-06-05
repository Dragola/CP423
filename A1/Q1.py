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

   # remove whitespace in tokens (TODO- not sure if this is working)
   tokens = [token.strip() for token in tokens]

   # excluding special characters (TODO- why is it adding a space?)
   tokens = [re.sub(r'[^a-zA-Z]', ' ', token) for token in tokens if token]

   # eliminating singly occuring characters
   #word_counts = Counter(tokens)
   # tokens = [token for token in tokens if word_counts[token] > 1]

   # eliminating single character words
   tokens = [token for token in tokens if len(token) > 1]

   # ensure that token stats with a character (TODO- words that have space or such before get lost)
   tokens = [token for token in tokens if token[0].isalpha()]

   # creating set of all the words
   #unique_words = list(tokens)
   
   return tokens
