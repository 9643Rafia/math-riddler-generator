# 🧩 MathRiddleAI: Fine-Tuned AI Model for Math Riddle Generation

A fun and creative NLP project that uses a fine-tuned language model to generate engaging math riddles. Deployed using Streamlit, the app allows users to explore AI-generated logic puzzles, math questions, and brain teasers — all created in real time.

---

## 📖 Overview

- 🤖 Fine-tuned a language model specifically on **math riddle-style datasets**
- 🧠 Generates creative and challenging **math riddles** on demand
- 🖥️ Deployed with a simple **Streamlit frontend** for interactive use
- ✍️ Full blog post explaining dataset, model, and deployment [here](https://medium.com/@f219643/building-a-streamlit-web-app-for-a-fine-tuned-math-riddle-ai-model-ee881f7de009)

---

## 📁 Folder Structure

MathRiddleAI/
│
├── app/
│ └── app.py # Streamlit frontend
│
├── model/
│ └── fine_tuned_model/ # Model checkpoint or HuggingFace link
│
├── data/
│ └── riddles_dataset.csv # Math riddle text data (if available)
│
├── requirements.txt
├── README.md
└── LICENSE

---

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/MathRiddleAI.git
cd MathRiddleAI

2. **Install dependencies**

```bash
pip install -r requirements.txt

3. **Run the app**

```bash
streamlit run app/app.py

## 🧠 How It Works
Dataset: Curated collection of math riddles and logic problems
Model: Fine-tuned transformer (e.g., GPT-2) on riddle-style questions
Backend: Uses Hugging Face Transformers or custom fine-tuned model
Frontend: Streamlit interface with input prompt + real-time response

## ✍️ Blog
📰 Building a Streamlit Web App for a Fine-Tuned Math Riddle AI Model

Covers:
Data preprocessing
Model fine-tuning steps
Riddle formatting
Streamlit deployment

## 👩‍💻 Author
Rafia Zubair
🔗 LinkedIn
📬 Blog on Medium

## 📜 License
This project is licensed under the MIT License.
