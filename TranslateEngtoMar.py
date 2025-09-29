from googletrans import Translator

def translate_english_to_marathi(text):
    """
    Translates English text to Marathi using the googletrans library.

    Args:
        text (str): The English text to be translated.

    Returns:
        str: The translated Marathi text, or an error message if translation fails.
    """
    try:
        translator = Translator()
        translation = translator.translate(text, src='en', dest='mr')
        return translation.text
    except Exception as e:
        return f"Error during translation: {e}"

# Example usage:
english_text = "Hello, how are you?"
marathi_translation = translate_english_to_marathi(english_text)
print(f"English: {english_text}")
print(f"Marathi: {marathi_translation}")

english_text_two = "The quick brown fox jumps over the lazy dog."
marathi_translation_two = translate_english_to_marathi(english_text_two)
print(f"English: {english_text_two}")
print(f"Marathi: {marathi_translation_two}")