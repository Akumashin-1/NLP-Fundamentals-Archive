import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
from pywsd.lesk import simple_lesk, adapted_lesk, cosine_lesk

# ornek cumle
sentences = [
    "I go to the bank to deposit money",
    "The river bank was flooded after the heavy rain"]

word = "bank"

for s in sentences:
    print(f"Sentence: {s}")

    # Correcting simple_lesk
    sense_simple = simple_lesk(s, word) 
    print(f"Sense simple: {sense_simple.definition()}")

    # Correcting adapted_lesk
    sense_adapted = adapted_lesk(s, word)
    print(f"Sense adapted: {sense_adapted.definition()}")

    # Correcting cosine_lesk
    sense_cosine = cosine_lesk(s, word)
    print(f"Sense cosine: {sense_cosine.definition()}")
    























