# Install the library first:
# pip install googletrans==4.0.0-rc1

from googletrans import Translator

def english_to_marathi(text):
    translator = Translator()
    result = translator.translate(text, src='en', dest='mr')
    return result.text

# Example usage
if __name__ == "__main__":
    english_text = "Hello, how are you? I am learning Python."
    marathi_translation = english_to_marathi(english_text)
    print("English:", english_text)
    print("Marathi:", marathi_translation)
