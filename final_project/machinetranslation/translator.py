import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['API_KEY']
url = os.environ['API_URL']

# Initialize Language Translator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    if english_text is None:
        return None
    
    # Translate text from English to French
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract and return the translated text
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    if french_text is None:
        return None
    
    # Translate text from French to English
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    # Extract and return the translated text
    english_text = translation['translations'][0]['translation']
    return english_text
