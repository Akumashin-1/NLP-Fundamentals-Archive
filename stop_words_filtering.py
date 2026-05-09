import nltk

from nltk.corpus import stopwords

nltk.download("stopwords") # en cok kullanilan stopwords veriseti

#ingilizcedeki stopwords listesi
stop_words_eng = set(stopwords.words("english"))

#ornek ingilizce metin
text = "There are some examples of handling stop words from some texts."

# 1. adim -> tokenlastirma
text_list = text.split()

# stop words listesinde olmayan kelimeleri filtrelemis listeye ekle
filtered_words = []
for word in text_list:
    if word.lower() not in stop_words_eng:
        filtered_words.append(word)
# filtered_words = [word for word in text_list if word.lower() not in stop_words_eng]
print(f"filtered_words: {filtered_words}")



'''-----'''

# turkce stop words inceleme
stop_words_tr = set(stopwords.words("turkish"))
metin = "Merhaba arkadaşlar çok güzel bu ders."
metin_list = metin.split()

filtered_words_tr = []
for word in metin_list:
    if word.lower() not in stop_words_tr:
        filtered_words_tr.append(word)
# filtered_words_tr = [word for word in metin_list if word.lower() not in stop_words_tr]
print(f"filtered_words_tr: {filtered_words_tr}")

'''--------'''


# stop words kutuphanesi kendimiz olusturalim
tr_stopwords = ["için", "bu", "ile", "mu"]
metin2 = "bu bir denemedir. Amacımız bu metindeki özel kelimeler ile çalışmak"

filtered_words_tr2 = []
for word in metin2.split():
    if word.lower() not in tr_stopwords:
        filtered_words_tr2.append(word)

# filtered_words_tr2 = [word for word in metin2.split() if word.lower() not in tr_stopwords]
print(f"filtered_words_tr2: {filtered_words_tr2}")