import streamlit as st
from llama_cpp import Llama

# Load the LLM model
LLM = Llama(model_path="llama-2-7b-chat.Q5_K_M.gguf", n_ctx=2048)

# Initialize session state
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Define questions
questions = [
    "What is your name?",
    "Do you have symptoms?",
    "Do you take medicines?",
    "Do you have allergies?"
]

# Ask each question and save answers
for question in questions:
    user_answer = st.text_input(question)
    st.session_state.answers[question] = user_answer

# Generate summary using LLM with refined prompt and examples
answers_text = "\n".join(answer for answer in st.session_state.answers.values())

summary_prompt = f"""**Provide a concise and factual summary of the key points from the following answers.**

**Focus only on the information provided. Do not add any speculation, personal opinions, or new information.**

**Here are examples of good summaries:**

* **Prompt:** John is 30 years old, lives in London, and works as a software engineer. He enjoys playing football and reading books. **Good summary:** John is a 30-year-old software engineer who lives in London and enjoys football and reading.
* **Prompt:** The patient reported a fever, cough, and headache. They have no known allergies and are not currently taking any medications. **Good summary:** The patient has a fever, cough, and headache. They have no allergies and are not taking medications.

**Please provide a summary that is similar to the examples above.**
"""

output = LLM(summary_prompt, temperature=0)#, top_p=0.95, frequency_penalty=0.5)
summary = output["choices"][0]["text"]

# Display answers and summary
st.write("**Your answers:**")
for question, answer in st.session_state.answers.items():
    st.write(f"**{question}:** {answer}")

st.write("**Summary of your answers:**")
st.write(summary)