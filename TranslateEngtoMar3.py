from deep_translator import GoogleTranslator

def english_to_marathi(text):
    translator = GoogleTranslator(source='en', target='mr')
    return translator.translate(text)

if __name__ == "__main__":
    english_text = "create a photorealistic image."
    marathi_translation = english_to_marathi(english_text)
    print("English:", english_text)
    print("Marathi:", marathi_translation)
