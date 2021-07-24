# The program converts from the binary number system to decimal

numbers0 = input('Введите значение: ')
numbers = list(numbers0) 
run = True

for number in numbers:
    if int(number) > 1 or int(number) < 0:
        print('Error!')
        run = False
        break

if run == True:
    numbers.reverse() 
    length = len(numbers) 
    n = 0 
    nums = [] 
    for number in numbers:
        if n != length:
            nums.append(int(number) * 2**n)
            n +=1

    answer = sum(nums) 
    print(answer) 
