import json
import bot
with open('russian_language.txt', 'r', encoding='utf-8') as file:
    a = file.read()
    russian_text = json.loads(a)
with open('english_language.txt', 'r', encoding='utf-8') as file:
    a = file.read()
    english_text = json.loads(a)



MORSE_CODE_DICT = ''


def language_choose():
    global MORSE_CODE_DICT
    text_laguage = input('ru/en')
    if text_laguage == 'ru':
        MORSE_CODE_DICT = russian_text
    if text_laguage == 'en':
        MORSE_CODE_DICT = english_text



def russian_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + ' '
    return morse_code.strip()

def morse_to_russian(morse_code):
    russian_text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in MORSE_CODE_DICT.items():
            if morse == code:
                russian_text += char
                break
    return russian_text

def translate_text(text):
    if text.lower() == 'exit' or text.lower() == 'quit':
        return False
    elif text.startswith('.') or text.startswith('-'):
        translated_text = morse_to_russian(text)
        print(f'Translated text: {translated_text}')
    else:
        morse_code = russian_to_morse(text)
        print(f'Morse_code: {morse_code}')
    return True
language_choose()
while True:

    user_input = input('Enter text in Russian or Morse_code (enter "exit" to quit):')
    if not translate_text(user_input):
        break
    language_choose()
