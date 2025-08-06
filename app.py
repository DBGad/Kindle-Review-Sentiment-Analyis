import streamlit as st
import pickle
from text_cleaning import clean_text
from gensim.models import Word2Vec
import numpy as np
import time

# ---------- Load models ----------
model = pickle.load(open("model.pkl", "rb"))
w2v_model = Word2Vec.load("word2vec_model")

# ---------- Utility functions ----------
def avg_word2vec(doc):
    return np.mean([w2v_model.wv[word] for word in doc if word in w2v_model.wv], axis=0)

def set_bg_color():
    st.markdown("""
        <style>
        .main {
            background-color: #f0f8ff;
        }
        </style>
        """, unsafe_allow_html=True)

def add_footer():
    st.markdown("""
        <hr style="border:1px solid #bbb">
        <div style='text-align: center'>
            Made with ❤️ by <strong>Gad Amr</strong> | 📚 Kindle Review Sentiment App
        </div>
        """, unsafe_allow_html=True)

# ---------- UI Starts ----------
set_bg_color()
st.title("📚 Kindle Review Sentiment Predictor")
st.markdown("Enter your **Amazon Kindle review** below to detect its sentiment.")

with st.expander("💡 Example Reviews"):
    st.info("✅ *I loved the story and characters. A must-read!*")
    st.info("❌ *The plot was boring and poorly written.*")

text = st.text_area("✏️ Write your review here", height=200)

if st.button("🔍 Predict Sentiment"):
    if text.strip() == "":
        st.warning("Please enter a review to predict.")
    else:
        # Loading bar simulation
        progress = st.progress(0)
        for percent in range(100):
            time.sleep(0.01)
            progress.progress(percent + 1)

        cleaned = clean_text(text).split()
        vec = avg_word2vec(cleaned).reshape(1, -1)
        pred = model.predict(vec)[0]

        # Result
        if pred == 1:
            st.success("✅ Positive Review")
            st.toast("Thanks for your feedback!", icon="😊")
            st.balloons()
        else:
            st.error("❌ Negative Review")
            st.toast("We're sorry you had a bad experience 😞", icon="⚠️")

add_footer()
