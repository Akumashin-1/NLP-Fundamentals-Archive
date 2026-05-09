# Metin Temsili Yöntemleri-1 -> Bag of Words
# BoW : Bag of Words -> kelimelerin çantası
# metni kelimelere bölüp, kelimelerin frekansını bulacağız
# ardından metnin vektör temsilini oluşturacağız

#count vectorizer iceriye actar
from sklearn.feature_extraction.text import CountVectorizer

# veri seti olustur
documents = [
    "Kedi bahçede",
    "Kedi evde"]

# vectorizer tanımla
vectorizer = CountVectorizer()

# metni sayısal vektorlere cevir
X= vectorizer.fit_transform(documents)

# kelime kumesini olusturma
feature_names = vectorizer.get_feature_names_out() #kelime kumesini olusturur
print(f"feature isimleri: {feature_names}")

# vektor temsili
vector_temsili = X.toarray()

print(f"Kelime kümesi: {vector_temsili}")