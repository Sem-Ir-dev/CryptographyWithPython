# Password guessing with BruteForce
import random

correctPassword = '1234'  
wrongPasswords = []     
password = ''       
length = 4     
chars = '1234567890'        

while run:
    password = ''       
    for i in range(length):
        password += random.choice(chars)    
    if password not in wrongPasswords:      
        print(password)
        if password != correctPassword:
            wrongPasswords.append(password)    
        else:
            print(password + ' is correct')
            run = False
            break       