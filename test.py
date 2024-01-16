import streamlit as st
from llama_cpp import Llama

# Load the LLM model
LLM = Llama(model_path="llama-2-7b-chat.Q5_K_M.gguf", n_ctx=2048)

# Define the main app function
def main():
    st.title("Health Information Summary")

    # Collect user information
    name = st.text_input("Enter your name:")
    symptoms = st.text_area("Enter any symptoms you're experiencing (if any):")
    medications = st.text_area("Enter any medications you're currently taking (if any):")
    medical_history = st.text_area("Enter any medical history (if any):")

    if st.button("Generate Summary"):
        # Construct a comprehensive prompt for the LLM
        #prompt = f"Summarize the following health information in a concise and factual manner:\n" \
        #         f"- Name: {name}\n" \
        #         f"- Symptoms: {symptoms}\n" \
        #         f"- Medications: {medications}" \
        #         f"\nFocus only on the information provided and nothing else. Do not add any speculation, personal opinions, or new information."
        prompt = f"**Concisely summarize the key medical information from the following, ensuring factual accuracy and objectivity:**\n" \
                 f"- **Patient Name:** {name}\n" \
                 f"- **Reported Symptoms:** {symptoms} (if any)\n" \
                 f"- **Current Medications:** {medications} (if any)\n" \
                 f"- **Medical History:** {medical_history} (if any)\n" \
                 f"\n**Prioritize:**\n" \
                 f"- Current health concerns\n" \
                 f"- Notable symptoms\n" \
                 f"- Medications and potential interactions\n" \
                 f"\n**Strictly adhere to the provided information. Avoid:**\n" \
                 f"- Speculation or opinions\n" \
                 f"- Introduction of new information not explicitly stated\n" \
                 f"- Subjective language or personal biases"



        try:
            # Generate summary with LLM
            output = LLM(prompt, temperature=0, max_tokens=0)
            summary = output["choices"][0]["text"]

            # Display the summary
            st.write("Summary:", summary)
        except Exception as e:
            st.error("Error generating summary:", e)

if __name__ == "__main__":
    main()