from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set a seed for reproducibility
DetectorFactory.seed = 0

# Language code to name mapping
language_names = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'ru': 'Russian',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'pa': 'Punjabi',
    'mr': 'Marathi',
    'te': 'Telugu',
    'ta': 'Tamil',
    'ur': 'Urdu',
    'tr': 'Turkish',
    'nl': 'Dutch',
    'sv': 'Swedish',
    'fi': 'Finnish',
    'no': 'Norwegian',
    'da': 'Danish',
    'el': 'Greek',
    'he': 'Hebrew',
    'vi': 'Vietnamese',
    'th': 'Thai',
    'cs': 'Czech',
    'pl': 'Polish',
    'hu': 'Hungarian',
    'uk': 'Ukrainian'
}

def identify_language(text):
    try:
        language_code = detect(text)
        return language_names.get(language_code, language_code)  # Return full name if available, otherwise code
    except LangDetectException as e:
        return f"Language detection error: {str(e)}"

# Get input from the user
text = input("Enter the text you want to identify the language of: ")
language = identify_language(text)
print(f"The language of the given text is: {language}")
