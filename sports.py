import streamlit as st
import pandas as pd
from translate import Translator
from gtts import gTTS
import os

def generate_audio(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = 'temp_audio.mp3'
    tts.save(audio_file)
    return audio_file

def split_text(text, chunk_size=500):
    chunks = []
    words = text.split(' ')
    current_chunk = ''
    for word in words:
        if len(current_chunk) + len(word) + 1 <= chunk_size:
            current_chunk += word + ' '
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + ' '
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

url = 'https://raw.githubusercontent.com/Yash-Bari/dataset/main/Sports.csv'
df = pd.read_csv(url)
st.set_page_config(page_title='Sports Information App', page_icon=':sports_medal:')
st.image("https://th.bing.com/th/id/OIP.W8FzzgXIKTGjKmHFYkdYnAAAAA?w=176&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", caption="MyOlympia", width=100)
st.title('Sports Information App')
st.subheader("Translate sports information in any language.")
st.write('---')

selected_sport = st.selectbox('Select a sport', df['Sport'].unique())

sport_data = df[df['Sport'] == selected_sport].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.image(sport_data['Images_url'], caption=selected_sport, use_column_width=True)

with col2:
    st.subheader(selected_sport + ' History')
    st.write(sport_data['History'])

st.write('---') 
st.subheader('Voice Translator')
text_to_translate = sport_data['History']

languages = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Chinese': 'zh',
    'Hindi': 'hi',
    'Marathi': 'mr',
}

language_names = list(languages.keys())
selected_language = st.selectbox('Select a language', language_names)

translate_button = st.button('Translate')

if translate_button:
    with st.spinner('Translating...'):
        lang_code = languages[selected_language]
        chunks = split_text(text_to_translate)
        translated_chunks = []
        for chunk in chunks:
            translator = Translator(from_lang='en', to_lang=lang_code)
            translated_text = translator.translate(chunk)
            translated_chunks.append(translated_text)

        translated_text = ' '.join(translated_chunks)
        st.success('Translated History:')
        st.write(translated_text)

        translated_audio = generate_audio(translated_text, lang=lang_code)
        st.audio(translated_audio, format='audio/mp3')
        os.remove(translated_audio)
