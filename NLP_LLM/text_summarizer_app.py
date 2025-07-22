import streamlit as st
from transformers import pipeline

st.title("Text Summarizer App")
st.write("Enter text below to summarize:")

summarizer = pipeline("summarization")

user_input = st.text_area("Enter text to summarize:", height=300)

def summarize_long_text(text):
    # Break long text into smaller chunks (500 words per chunk approx)
    max_chunk = 500
    sentences = text.split('. ')
    current_chunk = ""
    chunks = []
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence.split()) <= max_chunk:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    summary = ""
    for chunk in chunks:
        res = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summary += res[0]['summary_text'] + " "
    
    return summary

if st.button("Summarize"):
    if len(user_input.strip()) > 0:
        try:
            summary = summarize_long_text(user_input)
            st.subheader("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to summarize.")
