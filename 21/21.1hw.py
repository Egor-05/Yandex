<<<<<<< HEAD
translated_text = None


=======
>>>>>>> 11899a3a4ee2933fa1f2436947f6ff5a2580bce0
def translate(text):
    global translated_text
    for i in text:
        if i.lower() in 'аеёиоуыэюяaeyuo' or (not i.isalpha() and i != ' '):
            text = text.replace(i, '')
    while '  ' in text:
        text = text.replace('  ', ' ')
<<<<<<< HEAD
    translated_text = text.strip()
=======
    translated_text = text
>>>>>>> 11899a3a4ee2933fa1f2436947f6ff5a2580bce0
