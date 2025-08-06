# 📚 Kindle Review Sentiment Analysis

A Natural Language Processing (NLP) project that performs **sentiment classification** on Amazon Kindle book reviews using both traditional and embedding-based techniques.

---

## 📦 Dataset
- Source: Amazon Kindle Store 5-core dataset (1996–2014)
- Total: ~982,000 reviews (subset used in this project)
- Used Columns:
  - `reviewText` (the actual text of the review)
  - `overall` rating (mapped to sentiment: positive or negative)

---

## 🧹 Preprocessing
All reviews were passed through a custom `clean_text()` function which:
- Removed HTML tags, punctuation, emails, and URLs
- Lowercased all words
- Removed stopwords
- Lemmatized each word

---

## 🧠 Feature Engineering

### 1. TF-IDF
- Created unigram and bigram features using `TfidfVectorizer`
- Limited to top 3000 features

### 2. Word2Vec
- Trained a custom Word2Vec model using Gensim
- Represented each review as the **average of word vectors**

---

## 🤖 Models & Results

### 1. TF-IDF + Logistic Regression:
```
Accuracy: 83.5%
F1 Score: 88.1%
Precision: 84.9%
Recall: 91.6%
```

### 2. Word2Vec + Logistic Regression:
```
Accuracy: 77.1%
F1 Score: 83.8%
Precision: 79.1%
Recall: 89.2%
```

> Word2Vec gave slightly lower accuracy but strong generalization with semantic similarity.

---

## 🔍 How to Run

### Requirements:
- Python 3.8+
- Install packages:
```bash
pip install pandas numpy nltk gensim scikit-learn tqdm
```

### Run the notebook:
```bash
jupyter notebook "Kindle Review Sentiment Analyis.ipynb"
```

---


## 📬 Contact
**Author**: Gad Amr  
**LinkedIn**: [(https://www.linkedin.com/in/gaadamr/)]  
**License**: MIT
