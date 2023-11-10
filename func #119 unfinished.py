import random
r = random

def func():
    hn = int(input('choose a high number '))
    ln = int(input('choose a low number '))
    return r.randint(ln,hn)
    
num = func()

def think():
    print('i am thinking of a number...')
    guess = int(input('guess the number i\'m thinking of '))
    return guess

guess = think()


print(guess)

#comp_num = r.randint(num)
#print(comp_num)


