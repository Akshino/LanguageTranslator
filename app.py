import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize Google Translator
translator = Translator()

# Function to get language code from language name
def get_language_code(language_name):
    for lang_code, lang_name in LANGUAGES.items():
        if lang_name.lower() == language_name.lower():
            return lang_code
    return None

# Streamlit layout and styling
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="wide",
)

# Sidebar
st.sidebar.title("Language Translator 🌍")
st.sidebar.write("Translate text between languages using a modern, sleek interface.")

# Sidebar language selection
source_lang = st.sidebar.selectbox(
    "Select Source Language", ["English", "French", "Spanish", "German", "Italian"]
)

target_language_search = st.sidebar.text_input("Enter Target Language (e.g., French, Spanish)")

# Main Content Area
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #4B0082;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 16px !important;
    }
    h1, h2, h3, p {
        color: #4B0082;
    }
            
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border: none;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
    .main-container {
        padding: 20px;
        background-color: #f0f0f5;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title
st.markdown("<h1 class='main-header'>🌍 Language Translator using Seq2Seq Model</h1>", unsafe_allow_html=True)
st.write("Translate text between different languages in real time.")

# Input Area
st.markdown("## 📝 Enter Text to Translate:")
source_text = st.text_area("", "")

# Translate Button
if st.button("🌍 Translate"):
    target_lang_code = get_language_code(target_language_search)

    if target_lang_code is None:
        st.error(f"⚠ Error: '{target_language_search}' is not a valid language name. Please try again.")
    else:
        try:
            translated_text = translator.translate(source_text, src=source_lang[:2].lower(), dest=target_lang_code).text
            st.success(f"**Translated Text**: {translated_text}")
        except AttributeError:
            st.error("Translation failed due to a token acquisition issue. Please try again later.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

# Supported Languages Section
st.markdown("### 🔄 Supported Languages")
with st.expander("Click to view supported languages"):
    st.write(", ".join([lang_name.capitalize() for lang_name in LANGUAGES.values()]))

# Footer Section
st.markdown("""
    <footer style='text-align: center; padding: 10px;'>
    Made by Akshino using Streamlit.
    </footer>
    """, unsafe_allow_html=True)
