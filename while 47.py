n1 = int(input('Enter a number '))
n2 = int(input('Enter another number '))
nsum = n1 + n2
yn = str(input('do you wanna add another number? (y or n) '))
while yn == 'y':
    n3 = int(input('Enter another number '))
    nsum += n3
    yn = str(input('do you wanna add another number? (y or n) '))
print (nsum)