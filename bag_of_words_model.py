# ------------------------------------------------------------------
# BLOK 1: Kütüphanelerin import edilmesi
# ------------------------------------------------------------------
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# ------------------------------------------------------------------
# BLOK 2: Stopwords listesinin hazırlanması
# ------------------------------------------------------------------
# stopwords leri nltk kütüphanesinden indirelim
nltk.download('stopwords')

# "stop_words_eng" isimli bir değişkene ingilizce stopwordsleri atayalım
stop_words_eng = set(stopwords.words("english"))

# ------------------------------------------------------------------
# BLOK 3: Veri setinin içeriye aktarılması
# ------------------------------------------------------------------
# Not: "IMDB_Dataset.csv" dosyasının kodla aynı dizinde olduğundan emin olun.
# Eğer dosya yoksa, şu satırı kullanabilirsiniz:
# !pip install opendatasets
# import opendatasets as od
# od.download("https" + "://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")
# df = pd.read_csv("imdb-dataset-of-50k-movie-reviews/IMDB Dataset.csv")

try:
    df = pd.read_csv("IMDB_Dataset_part1.csv")
except FileNotFoundError:
    print("UYARI: 'IMDB_Dataset.csv' dosyası bulunamadı.")
    print("Test için örnek bir DataFrame oluşturuluyor.")
    # Örnek veri (eğer dosya bulunamazsa)
    data = {
        "review": [
            "This is a great movie! I loved it 100%.",
            "What a terrible film... waste of time and money $$$",
            "Absolutely fantastic, 10/10. The best acting.",
            "I don't know, it was just... bad. Very bad."
        ],
        "sentiment": ["positive", "negative", "positive", "negative"]
    }
    df = pd.DataFrame(data)
    # Eğer örnek veri kullanılıyorsa, 100 satır kısıtlamasını kaldıralım
    df = df[:4] 
else:
    # veri seti çok büyük, ilk 100 tanesiyle çalışacağız
    df = df[:100]


# veri setini "yorumlar" ve "duygu" olarak ikiye ayırıyoruz.
# "duygu" yorumların etiketidir.
documents = df["review"]
labels = df["sentiment"] # positive or negative

# ------------------------------------------------------------------
# BLOK 4: Metin temizleme fonksiyonu
# ------------------------------------------------------------------
def cleaned_text(text):
    # buyuk-kucuk harf cevir
    text = text.lower()
    
    # rakamları temizle
    text = re.sub(r"\d+", "", text) # \d+ bir veya daha fazla rakamı bulur
    
    # ozel karakterleri kaldır (sadece harfleri ve boşlukları tut)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    # kısa kelimeleri temizle
    # metni kelimelere bölün (splitting)
    words = text.split()
    # ardından kelime uzunluğu 2'den büyük olanları tek boşluk ile yeniden birleştirin
    words = [word for word in words if len(word) > 2]
    text = " ".join(words)
    
    # stopwords temizleme
    # stop words listesinde olmayan kelimeleri filtrele
    # Not: Metin zaten .split() ile 'words' listesine bölünmüştü, tekrar bölebiliriz.
    words = text.split()
    words = [word for word in words if word not in stop_words_eng]
    text = " ".join(words)
    
    return text # temizlenen metnin return edilmesi

# ------------------------------------------------------------------
# BLOK 5: Temizleme ve BoW Uygulaması
# ------------------------------------------------------------------
# documents isimli dataframe'in her bir satırını fonksiyona gönderip metni temizleyelim
# "cleaned_doc" isimli listeye temizlenmiş veriyi tekrar ekleyelim
cleaned_doc = []
for doc in documents:
    cleaned_doc.append(cleaned_text(doc))

# Temizlenmiş metinlerin ilk 5'ini görelim
print("--- TEMİZLENMİŞ METİNLER (İLK 5) ---")
for i, doc in enumerate(cleaned_doc[:5]):
    print(f"Metin {i+1}: {doc[:100]}...") # Çok uzun olmaması için ilk 100 karakter
print("-" * 30)

# BoW Kısmı
# vectorizer tanımla
vectorizer = CountVectorizer()

# metinleri sayısallaştır
X = vectorizer.fit_transform(cleaned_doc)

# kelime kümesi olustur
feature_names = vectorizer.get_feature_names_out()

# vector temsili oluştur ve göster
vector_temsili = X.toarray()

print("\n--- KELİME DAĞARCIĞI (FEATURE İSİMLERİ) (İLK 20) ---")
print(list(feature_names[:20]))
print("\n--- VEKTÖR TEMSİLİ (BoW Matrisi) (İLK 5 SATIR) ---")
print(vector_temsili[:5])
print("-" * 30)

# ------------------------------------------------------------------
# BLOK 6: Kelime Frekanslarının Analizi
# ------------------------------------------------------------------
# metinlerin sayısal temsilleri ile kelime kümesinden gelen kelimeleri birleştirir
df_bow = pd.DataFrame(vector_temsili, columns=feature_names)

# kelime frekanslarını göster
# axis=0--> sütunlar boyunca toplama yap: her bir kelimenin frekansını bulur
# A1--> elde edilen matrisi 1 boyutlu vektöre cevir
word_count = X.sum(axis=0).A1

# yukarıdaki kod çıktısında
# örnegin 34.satırdaki kelimeden 18 adet bulunuyor şeklinde gösterir
# kelimelerin ne olduğunu da görmek için dict kullanırız
word_freq = dict(zip(feature_names, word_count))

# böylece hangi kelimenin hangi sıklıkta kullanıldığını öğreniriz
# en sık kullanılan ilk 5 kelimeyi print edelim
most_common_5_words = Counter(word_freq).most_common(5)
print(f"\n--- EN SIK KULLANILAN 5 KELİME ---")
print(f"Most_common_5_words: {most_common_5_words}")

