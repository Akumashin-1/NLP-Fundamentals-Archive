from sklearn.feature_extraction.text import CountVectorizer

documents=["Bu çalışma Ngram çalışmasıdır.",
           "Bu çalışma doğal dil işleme çalışmasıdır."]

vectorizer_unigram = CountVectorizer(ngram_range = (1,1))
vectorizer_bigram = CountVectorizer(ngram_range=(2,2))
vectorizer_trigram = CountVectorizer(ngram_range=(3,3))

X_unigram = vectorizer_unigram.fit_transform(documents)
unigram_features= vectorizer_unigram.get_feature_names_out()

X_bigram= vectorizer_bigram.fit_transform(documents)
bigram_features= vectorizer_bigram.get_feature_names_out()

X_trigram= vectorizer_trigram.fit_transform(documents)
trigram_features= vectorizer_trigram.get_feature_names_out()

print(f"unigram_features: {unigram_features}")
print(f"bigram_features: {bigram_features}")
print(f"trigram_features: {trigram_features}")


from wordcloud import WordCloud
import matplotlib.pyplot as plt

word_count = X_unigram.sum(axis=0).A1
word_freq = dict(zip(unigram_features,word_count))

wordcloud = WordCloud().generate_from_frequencies(word_freq)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

ngrams = list (word_freq.keys())
counts = list(word_freq.values())

plt.barh(ngrams, counts, color='skyblue')
plt.xlabel("Frekans")
plt.ylabel("N-gram")
plt.title("N-gram Histogram")
plt.show()

word_count2 = X_bigram.sum(axis=0).A1
word_freq2 = dict(zip(bigram_features, word_count2))

ngrams= list(word_freq2.keys())
counts= list(word_freq2.values())

plt.barh(ngrams, counts, color='skyblue')
plt.xlabel("Frekans")
plt.ylabel("N-gram")
plt.title("N-gram Histogram")
plt.show()