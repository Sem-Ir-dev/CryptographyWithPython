# дешифратор

numbers0 = input('Введите значение: ') # юзер введет сюда значение (например - 1001 или 0110)
numbers = list(numbers0) # создаем из список из переменной numbers0
run = True

# После проверим есть ли другие цифры
for number in numbers:
    if int(number) > 1 or int(number) < 0:
        print('Error!')
        run = False
        break

# Теперь начинаем расшифрование
if run == True:
    numbers.reverse() # переворачиваем список
    length = len(numbers) # длина списка
    n = 0 
    nums = [] # здесь будут значения из следующего цикла
    # Здесь уже начинается расшифрование по школьной формуле
    for number in numbers:
        if n != length:
            nums.append(int(number) * 2**n)
            n +=1

    answer = sum(nums) # присваиваем сумму чисел из прошлого цикла
    print(answer) 
