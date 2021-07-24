# Morse Code

alphabet = {
    'a' : '._',     't' : '_',
    'b' : '_...',   'u' : '.._',
    'c' : '_._.',   'v' : '..._',
    'd' : '_..',    'w' : '.__',
    'e' : '.',      'x' : '_.._',
    'f' : '.._.',   'y' : '_.__',
    'g' : '__.',    'z' : '__..',
    'h' : '....',   '1' : '.____',
    'i' : '..',     '2' : '..___',
    'j' : '.___',   '3' : '...__',
    'k' : '_._',    '4' : '...._',
    'l' : '._..',   '5' : '.....',
    'm' : '__',     '6' : '_....',
    'n' : '_.',     '7' : '__...',
    'o' : '___',    '8' : '___..',
    'p' : '.__.',   '9' : '____.',
    'q' : '__._',   '0' : '_____',
    'r' : '._.',    's' : '...',
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
    
print(' | '.join(result))
