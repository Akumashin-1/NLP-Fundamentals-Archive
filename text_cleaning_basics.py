import string
from textblob import TextBlob
from bs4 import BeautifulSoup
import re

# metinlerde bulunan fazla boşlukları ortadan kaldır
text = "Hello, World!    2025"
cleaned_text1 = " ".join(text.split())
print(f"text: {text} \n cleaned_text1: {cleaned_text1}")


# noktalama işaretlerini kaldır
text = "Hello, World! 2025"
cleaned_text3 = text.translate(str.maketrans("", "", string.punctuation))
print(f"text: {text} \n cleaned_text3: {cleaned_text3}")


# yazım hatalarını düzelt
text = "Hello, Wirld! 2025"
cleaned_text5 = TextBlob(text).correct()
print(f"text: {text} \n cleaned_text5: {cleaned_text5}")


# büyük harflerin küçük harfe çevrilmesi
text = "Hello, World! 2025"
cleaned_text2 = text.lower() # küçük harfe çevir
print(f"text: {text} \n cleaned_text2: {cleaned_text2}")


# html/url etiketlerini kaldır
text = "<div>Hello, World! 2025</div>"
cleaned_text6 = BeautifulSoup(text, "html.parser").get_text()
print(f"text: {text} \n cleaned_text6: {cleaned_text6}")
text2 = "Visit https://www.dataclean.com"
cleaned_text7 = re.sub(r"http\S+", "", text2) # URL'leri kaldır
print(f"text: {text2} \n cleaned_text7: {cleaned_text7}")
text3 = "Contact us at info@dataclean.org"
cleaned_text8 = re.sub(r"\S+@\S+", "", text3) # E-postaları kaldır
print(f"text: {text3} \n cleaned_text8: {cleaned_text8}")


# özel karakterleri kaldır
text = "Hello, World! 2025%"


# text içinden harf ve rakamlar dışındaki tüm karakterleri kaldır
cleaned_text4 = re.sub(r"[^A-Za-z0-9\s]", "", text)
print(f"text: {text} \n cleaned_text4: {cleaned_text4}")