import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load fine-tuned model
model_path = "/content/drive/MyDrive/qwen-math-riddles"  # ✅ Corrected Path  # Update path if stored in Google Drive
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Move model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Function to generate riddles
def generate_riddle():
    prompt = "Here is a math riddle:\n"
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

    with torch.no_grad():  # No need to track gradients
        output = model.generate(
            input_ids,
            max_length=150,
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            do_sample=True  # Enables randomness for diverse riddles
        )

    riddle = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    return riddle

# Streamlit UI
st.title("🤖 Math Riddle Generator")
st.write("🔢 **AI-powered tool that generates unique math riddles.** Click below to create one!")

if st.button("🎲 Generate a Math Riddle"):
    riddle = generate_riddle()
    st.success(f"🧩 **Riddle:**\n\n{riddle}")
