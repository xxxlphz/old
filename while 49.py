compnum = 50
a = 0
n = int(input('Guess a number '))
a += 1
while n != 50:
    if n > 50:
        print('Too high')
        n = int(input('Try again '))
        a += 1
    elif n < 50:
        print('Too low')
        n = int(input('Try again '))
        a += 1

if n == 50:
    print(f'Well done, you took {a} attempts')