# https://raw.githubusercontent.com/mohitgupta-omg/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv

"""
spam veri seti -> spam ve ham -> binary classification with Decision Tree
"""

# import libraries
import pandas as pd

# veri setini yukle
data = pd.read_csv("Folder/Spam.csv", encoding = "latin-1")
data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace = True)
data.columns = ["etiket", "metin"]

# EDA: Kesifsel veri analizi: missing value (kayip deger)
print(data.isna().sum())

# %% text cleaning and preprocessing: ozel karakterler, lowercase, tokenization, stopwords, lemmatize

import nltk 

nltk.download("stopwords") # cok kullanilan ve anlam tasimayan sozcukleri metin icerisinden cikartalim
nltk.download("wordnet") # lemma bulmak icin gerekli olan veriseti
nltk.download("omw-1.4") # wordnete ait farkli dillerin kelime anlamlarini iceren bir veri seti

import re 
from nltk.corpus import stopwords  # stopwords lerden kurtulmak icin
from nltk.stem import WordNetLemmatizer # lemmatization

metin = list(data.metin)
lemmatizer = WordNetLemmatizer()

corpus = []


for i in range(len(metin)):
    
    r = re.sub("[^a-zA-Z]", " ", metin[i]) # metin icerisinde harf olmayan tum karakterlerden kurtul
    
    r = r.lower() # buyuk harfi kucuk harf yap
    
    r = r.split() # kelimeleri ayir
    
    r = [word for word in r if word not in stopwords.words("english")] # stopwords lerden kurtul
    
    r = [lemmatizer.lemmatize(word) for word in r]
    
    r = " ".join(r)
    
    corpus.append(r)

data["metin2"] = corpus


# %% model training and evaluation

X = data["metin2"] 
y = data["etiket"] # target variable

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20, random_state = 42)

# feature extraction: bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X_train_cv = cv.fit_transform(X_train)

# classifier training: model training and evaluation
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(X_train_cv, y_train) # egitim

X_test_cv = cv.transform(X_test)

# prediction 
prediction = dt.predict(X_test_cv)

from sklearn.metrics import confusion_matrix
c_matrix = confusion_matrix(y_test, prediction)

accuracy = 100*(sum(sum(c_matrix)) - c_matrix[1,0] - c_matrix[0,1])/sum(sum(c_matrix))

print(f"Basarim: {accuracy}")













