import random
r = random
mynum =r.randint(1,10)

choice = int(input('choose a number '))

while choice != mynum:
    
    print('Try again')
    choice = int(input('choose a number '))

print('correct')