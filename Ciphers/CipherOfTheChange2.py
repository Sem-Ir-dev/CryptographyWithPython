from random import randint

text = input('Enter text: ')

keys = {
    'q':['$', '№', 'Ь'],
    'w':[':', 'ь'],
    'e':['R', '2', '=', '+', '-', 'S'],
    'r':[';', 'ы', 'н'],
    't':['s', '~', 'D'],
    'y':['d', 'M'],
    'u':['!', 'm', 'v'],
    'i':['l', '@'],
    'o':['i', '3', 'Ы'],
    'p':['^', 'V', 'E'],
    'a':['e', '1', '_', ')', 'r'],
    's':['Q', '&'],
    'd':['Y', '5', 'Н'],
    'f':['4', 'y', 'N', 'T'],
    'g':['I', 'В'],
    'h':['6', 'n', 't', 'G', 'F'],
    'j':['T'],
    'k':['8', '/'],
    'l':['g', 'f', 'Z'],
    'z':['z'],
    'x':['{', 'У'],
    'c':['9', '('],
    'v':['7', 'в'],
    'b':['w', 'o', 'X', 'B'],
    'n':['h', 'H'],
    'm':['x', 'b', 'W', 'O'],
    ' ':['}'],
    '.':['Х']
}

crypt = ''

for i in text:
    if i in keys:
        length = len(keys[i])
        crypt += keys[i][randint(0, length - 1)]

print(crypt)

# decription

'''
decrypt = ''
for i in crypt:
    for j in keys:
        if i in keys[j]:
            decrypt += j

print(decrypt)
'''