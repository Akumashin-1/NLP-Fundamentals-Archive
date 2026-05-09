import pandas as pd
import numpy as np
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from nltk.corpus import stopwords

df = pd.read_csv("BURAYA_TEST_VERISI", encoding ="latin-1")
df = df.loc[:,["v1","v2"]]

documents = df["v2"]
labels = df["v1"]

def cleaned_text(text):
    
    text = text.lower()
    
    
    text = re.sub(r"\d+", "", text) 
    

    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
 
    words = text.split()
    words = [word for word in words if len(word) > 2]
    text = " ".join(words)
    

    '''words = text.split()
    words = [word for word in words if word not in stop_words_eng]
    text = " ".join(words)'''
    
    return text 

cleaned_doc = [cleaned_text(row) for row in documents]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_doc)

feature_names = vectorizer.get_feature_names_out()

vector_temsili = X.toarray()
tfidf_score = X.mean(axis=0).A1

df_tfidf = pd.DataFrame({"word":feature_names,"scores":tfidf_score})

df_tfidf_sorted = df_tfidf.sort_values(by="scores",ascending=False)
print(df_tfidf_sorted.head(10))





