msh = {'A': '.-',
       'B': '-...',
       'C': '-.-.',
       'D': '-..',
       'E': '.',
       'F': '..-.',
       'G': '--.',
       'H': '....',
       'I': '..',
       'J': '.---',
       'K': '-.-',
       'L': '.-..',
       'M': '--',
       'N': '-.',
       'O': '---',
       'P': '.--.',
       'Q': '--.-',
       'R': '.-.',
       'S': '...',
       'T': '-',
       'U': '..-',
       'V': '...-',
       'W': '.--',
       'X': '-..-',
       'Y': '-.--',
       'Z': '--..'}

mdsh = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'}


def encode_to_morse(text):
    mc = []
    for i in text:
        if i in msh:
            mc.append(msh[i] + '/')
        else:
            mc.append(i)
    return ''.join(mc)


def decode_from_morse(code):
    rc = []
    code = code.split('/')
    for i in code:
        if i in mdsh:
            rc.append(mdsh[i])
        else:
            rc.append(i)
    return ''.join(rc)


def main():
    if input('вы хотите закодировать или декодировать?') == 'закодировать':
        print(encode_to_morse(input()))
    else:
        print(decode_from_morse(input()))