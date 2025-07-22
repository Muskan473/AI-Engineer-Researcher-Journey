import streamlit as st
from transformers import pipeline

st.title("Text Summarizer App")
st.write("Enter text below to summarize:")

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

user_input = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if len(user_input.strip()) > 0:
        # Approximate token count (1 word ~ 1.3 tokens, rough estimate)
        token_length = len(user_input.split()) * 1.3
        token_length = int(token_length)

        # Set max_length dynamically but keep it reasonable
        max_len = min(150, int(token_length * 0.6))  # Take 60% of the input size
        min_len = max(20, int(max_len * 0.5))  # Minimum 50% of summary length

        summary = summarizer(user_input, max_length=max_len, min_length=min_len, do_sample=False)
        
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
