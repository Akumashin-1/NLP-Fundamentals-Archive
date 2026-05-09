import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

document = ["Köpek çok tatlı bir hayvandır.","Köpek ve kuşlar çok tatlı hayvanlardır.","Inekler süt üretirler."]

tfidf_vectorizer = TfidfVectorizer()

X = tfidf_vectorizer.fit_transform(document)

feature_names = tfidf_vectorizer.get_feature_names_out()


vector_temsili = X.toarray()

print(f"tf-idf: {vector_temsili}")

df_tfidf = pd.DataFrame(vector_temsili, columns=feature_names)

tf_idf  = df_tfidf.mean(axis=0)


         


