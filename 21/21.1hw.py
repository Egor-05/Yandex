translated_text = None


def translate(text):
    global translated_text
    for i in text:
        if i.lower() in 'аеёиоуыэюяaeyuo' or (not i.isalpha() and i != ' '):
            text = text.replace(i, '')
    while '  ' in text:
        text = text.replace('  ', ' ')
    translated_text = text.strip()
