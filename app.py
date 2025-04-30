import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-mpnet-base-v2')

# Load and embed dataset
@st.cache_data(show_spinner=False)
def load_data():
    data = pd.read_csv("Conversation.csv")
    data = data.drop(columns=['Unnamed: 0'], errors='ignore')
    data['question_embedding'] = model.encode(data['question'].tolist(), show_progress_bar=True).tolist()
    data['answer_embedding'] = model.encode(data['answer'].tolist(), show_progress_bar=True).tolist()
    return data

data = load_data()

# Extract top suggested questions (first 15 unique ones)
suggested_questions = data['question'].dropna().unique()[:15]

# App layout
st.set_page_config(page_title="Smart Chatbot", page_icon="💬", layout="centered")
st.title("💬 Controlled Semantic Chatbot")
st.caption("Fast, Reliable, and Hallucination-Free")

# Sidebar with suggestions
with st.sidebar:
    st.header("🧠 Try Asking...")
    for question in suggested_questions:
        st.markdown(f"- {question}")

# Chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Say something like: 'How's it going?'")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Embed user input and compute similarity
    query_vector = model.encode([user_input])
    data_matrix = np.vstack(data['question_embedding'].values)
    similarities = cosine_similarity(query_vector, data_matrix)[0]
    data['similarity'] = similarities

    # Select best match
    best_match = data[data['similarity'] > 0.70].sort_values(by='similarity', ascending=False)
    if not best_match.empty:
        bot_reply = best_match.iloc[0]['answer']
    else:
        bot_reply = "I'm not sure how to respond to that yet. Try rephrasing."

    st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
