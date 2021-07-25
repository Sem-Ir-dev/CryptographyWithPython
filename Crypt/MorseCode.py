# Morse Code

alphabet = {
    'a' : '. _',     't' : '_',
    'b' : '_ . . .',   'u' : '. . _',
    'c' : '_ . _ .',   'v' : '. . . _',
    'd' : '_ . .',    'w' : '. _ _',
    'e' : '.',      'x' : '_ . . _',
    'f' : '. . _ .',   'y' : '_ . _ _',
    'g' : '__ .',    'z' : '_ _ . .',
    'h' : '. . . .',   '1' : '. _ _ _ _',
    'i' : '. .',     '2' : '. . _ _ _',
    'j' : '. _ _ _',   '3' : '. . . _ _',
    'k' : '_ . _',    '4' : '. . . . _',
    'l' : '. _ . .',   '5' : '. . . . .',
    'm' : '_ _',     '6' : '_ . . . .',
    'n' : '_ .',     '7' : '_ _ . . .',
    'o' : '_ _ _',    '8' : '_ _ _ . .',
    'p' : '. _ _ .',   '9' : '_ _ _ _ .',
    'q' : '_ _ . _',   '0' : '_ _ _ _ _',
    'r' : '. _ .',    's' : '. . .',
    ' ' : ' '
}

text = input('Enter text: ').lower()

text_list =[]
result = []

for i in text:
    text_list.append(i)

for key, value in alphabet.items():
    for i in text_list:
        if i == key:
            result.append(value)
    
print('   '.join(result))
