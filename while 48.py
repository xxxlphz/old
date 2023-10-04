#while 48
n = 0

p1 = input('Who do you wanna invite ')
print(f'{p1} has been invited')
n += 1

yn = input('do you want to invite somome else? ')

while yn == 'yes':
    p1 = input('Who do you wanna invite ')
    print(f'{p1} has been invited')
    yn = input('do you want to invite somome else? ')

print(f'\nyou have invited {n} people')