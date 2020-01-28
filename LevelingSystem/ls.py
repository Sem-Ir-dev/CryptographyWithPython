# LevelingSystem v 1.0
import os # Для создании директории, может быть и другие функции поюзаю :)
import time

# Сначало проверим существует ли папка saves
if os.path.exists('/home/sem/Документы/LevelingSystem/saves'):
    print('Директория "saves" существует...')
else:
    print('Директория "saves" не найдена...')
    print('Создание директории "saves"...')
    create_dir = os.mkdir('saves')
    time.sleep(3)
    print('Директория создана!')

# Теперь проверим существет ли файл data.txt
if os.path.exists('/home/sem/Документы/LevelingSystem/saves/data.txt'):
    print('Файл "data.txt" существует...')
else:
    print('Файл "data.txt" не найден...')
    print('Создание файла "data.txt"...')
    names = input('Введите ваше имя: ')
    create_file = open('/home/sem/Документы/LevelingSystem/saves/data.txt', 'w')
    data = create_file.write(names)
    create_file.close()
    time.sleep(3)
    print('Файл создан!')

# Теперь проверим существует ли файл XP.txt
if os.path.exists('/home/sem/Документы/LevelingSystem/saves/XP.txt'):
    print('Файл "XP.txt" существует...')
else:
    print('Файл "XP.txt" не найден...')
    print('Создание файла "XP.txt"...')
    create_file1 = open('/home/sem/Документы/LevelingSystem/saves/XP.txt', 'w')
    xp_file = create_file1.write('0')
    create_file1.close()
    time.sleep(3)
    print('Файл создан!')

print('-------------------------------------------------------->')
print('                     [Система поднятия уровня]')
file_name = open('/home/sem/Документы/LevelingSystem/saves/data.txt', 'r') # читаем файл с именем
name = file_name.read()
print('                       [Приветствую тебя ' + str(name) + ']')
file_name.close()

print('-------------------------------------------------------->')
file_xp = open('/home/sem/Документы/LevelingSystem/saves/XP.txt', 'r') # читаем файл с кол-вом очков
sxp = file_xp.read()
print('Твое количество очков - ' + str(sxp))
file_xp.close()

xp = int(sxp)

def level():    # функция определяющая уровень
    if xp <= 2000:
        print('Твой уровень - 1')
    elif xp >= 2001 and xp <= 5000:
        print('Твой уровень - 2')
    elif xp >= 5001 and xp <= 9000:
        print('Твой уровень - 3')
    elif xp >= 9001 and xp <= 14000:
        print('Твой уровень - 4')
    elif xp >= 14001 and xp <= 20000:
        print('Твой уровень - 5')
    elif xp >= 20001 and xp <= 27000:
        print('Твой уровень - 6')
    elif xp >= 27001 and xp <= 35000:
        print('Твой уровень - 7')
    elif xp >= 35001 and xp <= 44000:
        print('Твой уровень - 8')
    elif xp >= 44001 and xp <= 54000:
        print('Твой уровень - 9')
    elif xp >= 54001 and xp <= 65000:
        print('Твой уровень - 10')

level()
run = True
print('-------------------------------------------------------->')
print('Вы можете ввести help, чтобы узнать команды.')
print('Или можете ввести dock, чтобы посмотреть документацию')
print('-------------------------------------------------------->')

while run:
    print('Что вы хотите?: ')
    command = input('/')
    print('-------------------------------------------------------->')
    if command == 'help':
        print('level - показыват ваш уровень')
        print('input - ввести завершенные задания для получения опыта')
        print('dock - посмотреть документацию')
        print('exit - выход из программы')
    if command == 'level':
        level()
    if command == 'dock': # Ещё не сделал
        pass
    if command == 'input':
        print('1)--- Тренировка')
        print('2)--- Уроки')
        print('3)--- Программирование')
        print('4)--- Чтение')
        print('5)--- Изучение языков')
        print('6)--- Уборка')
        print('7)--- Рисование')
        print('8)--- Тренировка игры на каком то инструменте')
        print('9)--- Готовка еды')
        print('10)--- Тренировка дикции')
        print('11)--- Тренировка вокала')
        print('12)--- Гигиена')
        print('13)--- Вязание')
        print('14)--- Шитьё')
        print('15)--- Ведение дневника')
        print('16)--- Учиться печатать')
        print('17)--- Учиться битбоксу')
        put = input('Какое задание вы выполнили?: ')
        if put == '1':
            xp += 200
        elif put == '2':
            xp += 200
        elif put == '3':
            xp += 150
        elif put == '4':
            xp += 100
        elif put == '5':
            xp += 100
        elif put == '6':
            xp += 100
        elif put == '7':
            xp += 90
        elif put == '8':
            xp += 90
        elif put == '9':
            xp += 60
        elif put == '10':
            xp += 60
        elif put == '11':
            xp += 60
        elif put == '12':
            xp += 70
        elif put == '13':
            xp += 50
        elif put == '14':
            xp += 50
        elif put == '15':
            xp += 50
        elif put == '16':
            xp += 60
        elif put == '17':
            xp += 40
        elif put == '18':
            xp += 60
        else:
            print('Нет такого числа!')
    if command == 'exit':
        save = open('/home/sem/Документы/LevelingSystem/saves/XP.txt', 'w')
        save_xp = save.write(str(xp))
        save.close()
        run = False
