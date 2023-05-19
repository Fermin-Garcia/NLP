import pandas as pd
import numpy as np
import re
import unicodedata
import nltk

def basic_clean(text):
    # Lowercase everything
    text = text.lower()
    
    # Normalize unicode characters
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    # Replace anything that is not a letter, number, whitespace or a single quote.
    text = re.sub(r"[^a-z0-9'\s]", '', text)

    return text

def tokenize(text):
    # Clean the text first
    clean_text = basic_clean(text)
    
    # Then tokenize it
    tokens = nltk.word_tokenize(clean_text)

    return tokens

def stem(text):
    # Instantiate the stemmer
    stemmer = PorterStemmer()
    
    # Tokenize the input text
    tokens = nltk.word_tokenize(text)
    
    # Apply stemming to each token
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    # Join the stemmed tokens back into a single string
    stemmed_text = ' '.join(stemmed_tokens)
    
    
    
import nltk
from nltk.stem import WordNetLemmatizer

def lemmatize(text):
    # Instantiate the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize the input text
    tokens = nltk.word_tokenize(text)
    
    # Apply lemmatization to each token
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the lemmatized tokens back into a single string
    lemmatized_text = ' '.join(lemmatized_tokens)

    return lemmatized_text

import nltk
from nltk.corpus import stopwords

def remove_stopwords(text, extra_words=None, exclude_words=None):
    # Get the list of English stopwords
    stopword_list = stopwords.words('english')

    # Add extra_words to the stopword list, if provided
    if extra_words:
        stopword_list.extend(extra_words)

    # Remove exclude_words from the stopword list, if provided
    if exclude_words:
        stopword_list = [word for word in stopword_list if word not in exclude_words]

    # Tokenize the input text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords from the tokens
    filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]

    # Join the filtered tokens back into a single string
    filtered_text = ' '.join(filtered_tokens)

    return filtered_text