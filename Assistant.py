import wikipediaapi
from deep_translator import GoogleTranslator
import streamlit as st
from gtts import gTTS
import os
import random
import time

def split_text_by_length(text, length, max_sentences=5):
    sentences = text.split('.')
    splits = []
    current_length = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if current_length + len(sentence) + 1 > length:
            if len(splits) >= max_sentences:
                break
            splits.append(sentence)
            current_length = 0
        else:
            splits.append(sentence)
            current_length += len(sentence) + 1
    return splits

def translate_text(text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    translation = translator.translate(text)
    return translation

def get_language_name(code):
    language_mapping = {
        "en": "English",
        "hi": "Hindi",
        "mr": "Marathi",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "ja": "Japanese",
        "ko": "Korean",
        "pt": "Portuguese",
        "zh": "Chinese",
        "ru": "Russian"
    }
    return language_mapping.get(code, "Unknown Language")
def show_animation():
    st.success("Thinking...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    st.success("Done!")

def virtual_assistant():
    st.title("InfoAssistant")
    st.markdown('---')

    st.sidebar.header("Instructions:")
    st.sidebar.write("1. Type your query in the 'You:' text box.")
    st.sidebar.write("**Example Query: ML, Football, India, ISRO, chandrayaan 3 and etc**")
    st.sidebar.write("2. Choose the language you want to translate the information to from the below.")
    st.sidebar.write("3. Click on the 'Translate and Assist' button to get assistance.")

    # Get user input
    user_input = st.text_input("You:", "")

    # Remove punctuation and symbols from the user input
    user_input_clean = ''.join(e for e in user_input if e.isalnum() or e.isspace())

    # Choose the target language
    language_mapping = {
        "en": "English",
        "hi": "Hindi",
        "mr": "Marathi",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "ja": "Japanese",
        "ko": "Korean",
        "pt": "Portuguese",
        "zh": "Chinese",
        "ru": "Russian"
    }
    st.sidebar.markdown("Choose language:")
    target_language_name = st.sidebar.selectbox("", list(language_mapping.values()))

    # Get the target language code based on the selected language name
    target_language_code = next(key for key, value in language_mapping.items() if value == target_language_name)
    wiki_wiki = wikipediaapi.Wikipedia('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    wiki_page = wiki_wiki.page(user_input_clean)

        if wiki_page.exists() and wiki_page.text:
            info = wiki_page.text
        else:
            # If the page doesn't exist or the summary is too short (ambiguous), show available options
            info = f"Sorry, I couldn't find any relevant information for '{user_input_clean}'."
            if wiki_page.exists() and wiki_page.is_disambiguation_page():
                info += "\n\nPlease select one of the following options:\n\n"
                for option in wiki_page.links.values():
                    info += f"- {option.title}\n"

        # Split the information into sentences, up to a maximum of five sentences
        max_sentences = 5
        sentence_splits = split_text_by_length(info, 400, max_sentences=max_sentences)
        info = ". ".join(sentence_splits)

        # Translate the information using deep_translator
        translated_info = translate_text(info, target_language_code)

        # Display the translated information as regular text
        with st.expander("Translation", expanded=True):
            st.write(f"{get_language_name(target_language_code)} Translation:")
            st.success(translated_info)


        # Inform the user that the audio file is being generated
        with st.spinner("Generating audio. Please wait for a moment..."):
            # Save the translated information as an audio file
            tts = gTTS(text=translated_info, lang=target_language_code, slow=False)
            audio_path = "translated_info.mp3"
            tts.save(audio_path)

        # Hide the info message once the audio is generated
        st.info("")

        with st.expander("Listen to Translation", expanded=True):
            audio_file = open(audio_path, "rb").read()
            st.audio(audio_file, format="audio/mp3")

        # Delete the temporary audio file
        os.remove(audio_path)

if __name__ == "__main__":
    virtual_assistant()
