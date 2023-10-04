import time
n = int(input('Guess a number '))

while n < 10 or n > 20: 
    while n > 20:
        print('whoa thats too high')
        time.sleep(0.50)
        n = int(input('try again '))
    while n < 10:
        print('damn thats too low')
        time.sleep(0.50)
        n = int(input('try again '))

    
    
print('Thank you cuh')