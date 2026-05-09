NLP-Fundamentals-Archive/
│
├── 01_Metin_On_Isleme/
│   ├── stemming_lemmatization.py       (Eski ad: kök_bulma.py)
│   ├── morphological_analysis_spacy.py (Eski ad: morfoloji.py)
│   ├── pos_tagging_spacy.py            (Eski ad: pos.py)
│   ├── stop_words_filtering.py         (Eski ad: stop_words.py)
│   ├── text_cleaning_basics.py         (Eski ad: veritemizleme.py)
│   └── tokenization_nltk.py            (Eski ad: tokenization.py)
│
├── 02_Vektorel_Temsil/
│   ├── bag_of_words_model.py           (Eski ad: bag_of_words.py)
│   ├── ngram_analysis_wordcloud.py     (Eski ad: ngram.py)
│   ├── spam_detection_tfidf.py         (Eski ad: spam_tfidf.py)
│   ├── count_vectorizer_intro.py       (Eski ad: vectorizer.py)
│   └── tfidf_vectorizer_intro.py       (Eski ad: Tfid.py)
│
├── 03_Geleneksel_NLP_Modelleri/
│   ├── pos_tagging_hmm.py              (Eski ad: hidden_markov.py)
│   ├── max_entropy_classifier.py       (Eski ad: max_entropy.py)
│   ├── wsd_lesk_nltk.py                (Eski ad: kelime_anlami_belirsizligi_giderme1.py)
│   └── wsd_lesk_pywsd.py               (Eski ad: kelime_anlami_belirsizligi_giderme2.py)
│
├── 04_Makine_Ogrenmesi/
│   └── sentiment_analysis_vader.py      (Eski ad: duygu_analizi.py)
│
├── 05_Modern_NLP_ve_LLM/
│   ├── text_summarization_bart.py      (Eski ad: metin_ozetleme.py)
│   ├── machine_translation_marianmt.py (Eski ad: metin_cevirisi.py)
│   ├── text_generation_transformers.py (Eski ad: gpt_llama.py)
│   └── openai_chatbot.py               (Eski ad: chatbot.py)
│
├── README.md
└── requirements.txt

# Doğal Dil İşleme Temelleri (NLP Fundamentals)

Bu depo, Doğal Dil İşleme (NLP) alanındaki temel kavramlardan modern Büyük Dil Modellerine (LLM) kadar uzanan kapsamlı bir Python uygulama arşividir. Metin temizleme, istatistiksel modeller, duygu analizi ve Transformer mimarileri gibi temel NLP aşamalarını içerir.

## 📂 Proje Yapısı

Repo, öğrenme sürecini kolaylaştırmak için beş ana kategoriye ayrılmıştır:

### 1. Metin Ön İşleme (Text Preprocessing)
Metnin analiz öncesi temizlenmesi ve yapılandırılması.
- Temel metin temizleme (HTML, URL, Özel Karakterler)
- Tokenizasyon (Kelime ve Cümle Parçalama)
- Kök Bulma (Stemming & Lemmatization)
- Morfolojik Analiz ve POS Etiketleme

### 2. Vektörel Temsil ve Özellik Çıkarımı
Metinlerin sayısal vektörlere dönüştürülme yöntemleri.
- Bag of Words (BoW) ve Count Vectorizer
- TF-IDF Ağırlıklandırma
- N-Gram Analizi ve Kelime Bulutu (WordCloud) Görselleştirme

### 3. İstatistiksel ve Geleneksel Modeller
NLP'nin temelini oluşturan klasik algoritmalar.
- Hidden Markov Models (HMM) ile POS Etiketleme
- Maksimum Entropi Sınıflandırıcısı
- Kelime Anlamı Belirginleştirme (WSD - Lesk Algoritması)

### 4. Makine Öğrenmesi Uygulamaları
- VADER ve NLTK kütüphaneleri ile duygu analizi (Sentiment Analysis).

### 5. Modern NLP ve LLM Uygulamaları
Derin öğrenme ve Transformer tabanlı güncel teknolojiler.
- BART modeli ile otomatik özetleme
- Helsinki-NLP (MarianMT) ile diller arası çeviri
- GPT-2 ve LLaMA modelleri ile metin üretimi
- OpenAI API entegrasyonlu akıllı sohbet robotu

## 🚀 Kurulum ve Çalıştırma

1. Repoyu klonlayın:
```bash
git clone [https://github.com/Akumashin-1/NLP-Fundamentals-Archive.git](https://github.com/Akumashin-1/NLP-Fundamentals-Archive.git)
cd NLP-Fundamentals-Archive
```

2. Bağımlılıkları Yükleyin:
Gerekli tüm kütüphaneleri tek seferde kurmak için terminalinizde projenin bulunduğu dizine gidip şu komutu çalıştırın:
```bash
pip install -r requirements.txt
```

3.spaCy Dil Modelini İndirin:
```bash
python -m spacy download en_core_web_sm
```

🛠️ Teknolojiler
-Kütüphaneler: NLTK, spaCy, Scikit-learn, Transformers, PyWSD, TextBlob, BeautifulSoup4.

-Modeller: GPT-2, LLaMA-7B, BART, MarianMT.

📝 Önemli Notlar
-openai_chatbot.py dosyasını kullanmak için kendi OpenAI API anahtarınızı tanımlamanız gerekir.

-LLaMA gibi büyük modelleri yerel makinede çalıştırırken yüksek bellek (RAM/VRAM) ihtiyacı olduğunu unutmayın.

Hazırlayan: Melih Karabacak
