# 💬 Controlled Semantic Chatbot

A fast, lightweight, and hallucination-free chatbot powered by **SentenceTransformers** and **Streamlit**, built to demonstrate how **smart architecture can outperform heavyweight models** in specific business use cases.

📍 Live Demo-ready · ⚡ No Training Needed · 🧠 GPT-Alternative for Controlled Contexts

---

## 🔍 Project Overview

This chatbot replicates the **intent-matching capabilities** of large models like T5 or GPT—but without the resource cost, training, or unpredictability.

Instead of training a deep learning model, we:

- Used a **pre-trained sentence embedding model**: `all-mpnet-base-v2`
- Embedded all questions and answers from a real dataset of 3.7K+ conversations
- Matched user input to known intents using **cosine similarity**
- Returned precise and contextually relevant answers with **zero hallucination**

> 💡 Ideal for business use cases where control, consistency, and reliability are more important than generative flexibility.

---

## 🚀 Why This Approach?

| Challenge             | Traditional GPT/T5 Models | Our Approach                  |
| --------------------- | ------------------------- | ----------------------------- |
| Training time         | Hours to days             | None                          |
| Cost                  | High GPU compute          | CPU-friendly                  |
| Risk of hallucination | High                      | None                          |
| Speed                 | Slower                    | Instant (ms latency)          |
| Control               | Low (creative but risky)  | High (pre-approved responses) |

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** – UI and chat interface
- **[SentenceTransformers](https://www.sbert.net/)** – For embedding inputs
- **`all-mpnet-base-v2`** – Pre-trained transformer model
- **Scikit-learn** – For cosine similarity
- **Pandas & NumPy** – Data management and performance

---

## 📦 Installation

```bash
git clone https://github.com/OldAlexhub/chatbot.git
cd chatbot
pip install -r requirements.txt
```

---

## ▶️ Live Demo

**_Streamlit link below:_**

```link
https://chatbot-6maxwigaaogbzbpraztajf.streamlit.app/
```

## 📊 Dataset

The chatbot uses a cleaned version of the Conversation.csv dataset (3,700+ rows). Each entry contains a question and answer, which are embedded using SentenceTransformers.

---

## ✅ Ideal Use Cases

- Customer support bots with pre-defined answers
- HR or legal assistants where consistency matters
- Educational bots that should not hallucinate
- Any chatbot use case where speed and control > open generation

---

## 📌 Future Improvements

- Load pre-saved .npy embeddings for faster cold start
- Add user feedback and response logging
- Top-3 similarity fallback or diversity sampling
- Add REST API using FastAPI for external integration

---

## 👤 Author

**_Mohamed Gad_**
**_Data Scientist · AI Strategist · Founder @ Old Alex Hub_**
🌐 mohamedgad.com | 🧠 LinkedIn: https://www.linkedin.com/in/mohamed-gad-6b286b1b6/

---

## 📄 License

**_MIT License — feel free to use and adapt!_**
