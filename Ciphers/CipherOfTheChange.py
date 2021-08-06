# Cipher of the Change
alphabet = {
    'a': '-',   't': '2', ' ': ' ',
    'b': '[',   'u': '5',
    'c': '=',   'v': '6',
    'd': '+',   'w': '?',
    'e': '_',   'x': '/',
    'f': ']',   'y': '>',
    'g': '!',   'z': '<',
    'h': '@',   '1': '|',
    'i': '#',   '2': '3',
    'j': '$',   '3': '1',
    'k': '%',   '4': ';',
    'l': '^',   '5': ':',
    'm': '&',   '6': '"',
    'n': '*',   '7': '{',
    'o': '(',   '8': '}',
    'p': ')',   '9': '`',
    'q': '9',   '0': '~',
    'r': '0',   's': 'q'
}

crypt = ''

text = input('Enter text: ').lower()

for i in text:
    if i in alphabet:
        crypt += alphabet[i]

print(crypt)
