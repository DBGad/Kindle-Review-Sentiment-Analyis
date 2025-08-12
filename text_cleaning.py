import re
import os
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import nltk
from nltk_downloader import download_nltk_data
download_nltk_data()


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # حذف التاجات
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\d+', '', text)

    # توكن + حذف التوقف + Lemmatize
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w, pos='v') for w in tokens if w not in stop_words and len(w) > 2]

    return ' '.join(tokens)
