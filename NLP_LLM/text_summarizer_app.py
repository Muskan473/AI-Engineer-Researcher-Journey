import streamlit as st
from transformers import pipeline

st.title("Text Summarizer App")
st.write("Enter text below to summarize:")

@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

summarizer = load_summarizer()

user_input = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if len(user_input) > 0:
        summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
