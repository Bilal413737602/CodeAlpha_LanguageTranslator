import streamlit as st
from deep_translator import GoogleTranslator

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌍 AI Language Translator")
st.write("Translate text between different languages using Google Translator.")

# -----------------------------
# Language Dictionary
# -----------------------------
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Turkish": "tr",
    "Portuguese": "pt"
}

# -----------------------------
# Input Text
# -----------------------------
text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type your text here..."
)

# -----------------------------
# Language Selection
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=0
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

# -----------------------------
# Translate Button
# -----------------------------
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        try:
            translator = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            )

            translated_text = translator.translate(text)

            st.success("Translation Completed!")

            st.subheader("Translated Text")

            st.text_area(
                "",
                translated_text,
                height=180
            )

        except Exception as e:
            st.error(f"Error: {e}")