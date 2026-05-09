import nltk # natural language toolkit

nltk.download("punkt_tab") # metni kelime ve cümle bazında token'lara ayırır

text = "Hello, World! How are you Hello, hi, ..."

# kelime tokenizasyonu: word_tokenize : metni kelimelere ayırır
# noktalama isaretleri ve bosluklar ayrı birer token olarak elde edilir
word_tokens = nltk.word_tokenize(text)

# cumle tokenizasyonu: sent_tokenize : metni cumlelere ayırır.
# her bir cumle birer token olur
sentence_tokens = nltk.sent_tokenize(text)
