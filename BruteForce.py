# Взлом пароля методом BruteForce. Сделал Sem_Ir
import random

correctPassword = '1234'  # Здесь стоит верный пароль
wrongPasswords = []     # Сюда будут складываться неправильные пароли
password = ''       # Сюда будет складываться сгенерированный пароль
length = 4      # Длинна пароля
chars = '1234567890'        # Список генерируемых чисел
run = True

while run:
    password = ''       # Обнуление переменной
    for i in range(length):
        password += random.choice(chars)    # Генерация паролей и добавление их в переменную password
    if password not in wrongPasswords:      # Если пароля нет в переменной wrongPasswords то выводим на экран
        print(password)
        if password != correctPassword:
            wrongPasswords.append(password)     # Если пароль неправильный добавляем в переменную wrongPasswords
        else:
            print(password + ' is correct')
            run = False
            break       # Если пароль правильный то выводится на экран и цикл прерывается
