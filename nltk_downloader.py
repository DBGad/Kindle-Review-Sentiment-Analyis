import nltk
import os

NLTK_DIR = os.path.join(os.getcwd(), "nltk_data")
nltk.data.path.append(NLTK_DIR)

def download_nltk_data():
    if not os.path.exists(NLTK_DIR):
        os.makedirs(NLTK_DIR)

    required_packages = ['stopwords', 'wordnet', 'punkt', 'omw-1.4']
    for pkg in required_packages:
        try:
            nltk.data.find(f"{pkg}")
        except LookupError:
            nltk.download(pkg, download_dir=NLTK_DIR)

download_nltk_data()
