# Morse Code
alphabet = {
    'a': '. _',       't': '_',
    'b': '_ . . .',   'u': '. . _',
    'c': '_ . _ .',   'v': '. . . _',
    'd': '_ . .',     'w': '. _ _',
    'e': '.',         'x': '_ . . _',
    'f': '. . _ .',   'y': '_ . _ _',
    'g': '_ _ .',     'z': '_ _ . .',
    'h': '. . . .',   '1': '. _ _ _ _',
    'i': '. .',       '2': '. . _ _ _',
    'j': '. _ _ _',   '3': '. . . _ _',
    'k': '_ . _',    ' 4': '. . . . _',
    'l': '. _ . .',   '5': '. . . . .',
    'm': '_ _',       '6': '_ . . . .',
    'n': '_ .',       '7': '_ _ . . .',
    'o': '_ _ _',     '8': '_ _ _ . .',
    'p': '. _ _ .',   '9': '_ _ _ _ .',
    'q': '_ _ . _',   '0': '_ _ _ _ _',
    'r': '. _ .',     's': '. . .'
}

alphabet1 = {
    '. _': 'a',       '_': 't',
    '_ . . .': 'b',   '. . _': 'u',
    '_ . _ .': 'c',   '. . . _': 'v',
    '_ . .': 'd',     '. _ _': 'w',
    '.': 'e',         '_ . . _': 'x',
    '. . _ .': 'f',   '_ . _ _': 'y',
    '_ _ .': 'g',     '_ _ . .': 'z',
    '. . . .': 'h',   '. _ _ _ _': '1',
    '. .': 'i',       '. . _ _ _': '2',
    '. _ _ _': 'j',   '. . . _ _': '3',
    '_ . _': 'k',     '. . . . _': '4',
    '. _ . .': 'l',   '. . . . .': '5',
    '_ _': 'm',       '_ . . . .': '6',
    '_ .': 'n',       '_ _ . . .': '7',
    '_ _ _': 'o',     '_ _ _ . .': '8',
    '. _ _ .': 'p',   '_ _ _ _ .': '9',
    '_ _ . _': 'q',   '_ _ _ _ _': '0',
    '. _ .': 'r',     '. . .': 's'
}

print('1) Decrypt\n2) Protect')
options = input('>')

text_list = []
text_list1 = []
result = []
crypt = ''
num_list = []

if options == '1':
    text = input('Enter text: ').lower()

    if text.count('   ') > 0:
        text = text.replace('   ', ',')
        text = text.replace(' ', '')
        text = text.replace(',', ' ')

    for i in text:
        if i == '_' or i == '.':
            text_list.append(i)
        elif i == ' ':
            text_list1.append(''.join(text_list))
            text_list.clear()

    text_list.clear()

    for i in text_list1:
        text = i.replace('', ' ')
        text = text.strip()
        text_list.append(text)

    for i in text_list:
        if i in alphabet1:
            crypt += alphabet1[i]

    print(crypt)

elif options == '2':
    text = input('Enter text: ').lower()
    text = text.replace(' ', '')

    for i in text:
        if i in alphabet:
            crypt += alphabet[i]
            crypt += '   '

    print(crypt)

else:
    print('You can only enter: 1 or 2')
