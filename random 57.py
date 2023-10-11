import random
r = random
mynum =r.randint(1,10)

choice = int(input('choose a number '))

while choice != mynum:
    
    if choice > mynum:
        print('Too high')
        choice = int(input('choose a number '))
        
    elif choice < mynum:
        print('Too low')
        choice = int(input('choose a number '))
        
if choice == mynum:
    print('correct')