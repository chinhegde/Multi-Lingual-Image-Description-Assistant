import streamlit as st
from PIL import Image
import easyocr
import openai
from transformers import pipeline

def image_to_text(image):
    reader = easyocr.Reader(['en'])  
    result = reader.readtext(image)
    extracted_text = ' '.join([entry[1] for entry in result])
    return extracted_text

def translate_text(text, target_language):
    openai.api_key = 'YOUR_API_KEY'  
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following English text to {target_language}: {text}",
        max_tokens=100
    )
    translated_text = response['choices'][0]['text'].strip()
    return translated_text

def text_to_speech(text, language_code):
    text_to_speech_pipeline = pipeline(task="text2speech", model=f"facebook/wav2vec2-base-960h-{language_code}")
    audio = text_to_speech_pipeline(text)[0]["audio"]
    return audio

def main():
    st.title("Multilingual Image Description Assistant")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")

        target_language_code = {"French": "fr", "Spanish": "es", "German": "de", "Hindi": "hi", "Kannada": "kn", "Bengali": "bn"}
        target_language = st.selectbox("Select Target Language:", ["French", "Spanish", "German", "Hindi", "Kannada", "Bengali"])
        
        extracted_text = image_to_text(image)
        
        st.header("Extracted Text:")
        st.write(extracted_text)

        st.write("Translating to", target_language, "...")
        
        translated_text = translate_text(extracted_text, target_language_code)

        st.header("Translated Text:")
        st.write(translated_text)

        st.write("Generating Audio...")
        audio = text_to_speech(translated_text, target_language_code)

        st.audio(audio, format="audio/wav")

if __name__ == "__main__":
    main()
