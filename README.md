# Multilingual Image Description Assistant
The Multilingual Image Description Assistant is a web application that takes an image as input, extracts text content, translates it into multiple languages, and converts the translated text into speech, providing a comprehensive multilingual audio description of the image.

[Motivation and architecture]([url](https://chinmayih.wordpress.com/2023/12/30/multilingual-image-description-assistant/))

## Features
- **Image-to-Text Processing** using Hugging Face's image-to-text model (easyocr) to extract textual information from uploaded images.
- **Language Translation** with OpenAI's LangChain to translate the extracted text into multiple languages, enhancing global accessibility.
- **Text-to-Speech Generation** using Hugging Face's text-to-speech model (transformers) to convert translated text into speech in the user's preferred language.

Allows users to upload images, choose target languages, and customize the voice and speed of the generated speech.

## Configuration
- Replace 'YOUR_API_KEY' with your actual OpenAI GPT-3 API key in the translate_text function.
