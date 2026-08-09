import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Gemini API key was not found.")
    st.stop()

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Medical Complaint Normalizer",
    layout="centered"
)
st.title("Medical Complaint Normalizer")
st.write(
    "Enter a patient's complaint in Arabic or English. "
    "The complaint will be rewritten using formal medical terminology."
)

complaint = st.text_area(
    "Patient Complaint",
    placeholder="Example: My back is killing me and the pain is really bad.",
    height=150
)


if st.button("Normalize Complaint"):
    if not complaint.strip():
        st.warning("Please enter a patient complaint.")

    else:
        prompt = f"""
You are a medical language normalization assistant.

Your task is to rewrite a patient's complaint into
clear, professional medical language while preserving
the language of the original complaint.

Language rules:
- If the patient's complaint is in Arabic, respond in Arabic.
- If the patient's complaint is in English, respond in English.
- If the complaint is mainly Arabic with some English words,
  respond in Arabic.
- If the complaint is mainly English with some Arabic words,
  respond in English.
- Do NOT translate the complaint into another language.

Medical normalization rules:
- Preserve the exact meaning of the patient's complaint.
- Convert informal or colloquial expressions into appropriate
  medical terminology.
- Do NOT diagnose the patient.
- Do NOT infer a disease or medical condition.
- Do NOT add symptoms or information that the patient did not mention.
- Preserve details such as duration, severity, location, triggers,
  and associated symptoms when provided.
- Keep the result concise.
- Write the result as a professional clinical statement.

Patient complaint:
{complaint}
"""
        with st.spinner("Processing complaint..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )
                result = response.text

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.stop()

        st.subheader("Formal Medical Version")
        st.write(result)