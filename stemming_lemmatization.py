import nltk

#wordnet : lemmatization islemi icin gerekli veri tabani
nltk.download("wordnet")

from nltk.stem import PorterStemmer

#stemming: kök bulma
#porter stemmer nesnesini olustur
stemmer = PorterStemmer()
words = ["running", "runner", "ran", "runs", "better", "go", "went"]

#kelimelerin stem lerini buluyoruz
#bunu yaparken PorterStemmer'in stem() fonk kullanıyoruz
stems = [stemmer.stem(w,to_lowercase=True) for w in words]
print(f"Stems: {stems}")




#lemmatization: anlamlı kök bulma

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words = ["running", "runner", "ran", "runs", "better", "go", "went"]
lemmas = [lemmatizer.lemmatize(w,pos='v') for w in words]
print(f"Lemmas: {lemmas}")
