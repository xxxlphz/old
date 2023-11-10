import random
r = random
colors = ['green', 'red', 'blue', 'pink', 'white']
c = r.choice(colors)

print('choose one of these colors:')
print(*colors)
userc = input('')

if c == 'green':
    clue = 'clue- \"i bet youre GREEN with envy\"'
elif c == 'blue':
    clue = 'clue- \"youre probably feeling very BLUE rn\"'
elif c == 'red':
    clue = 'clue- \"when im angry all i see is RED\"'
elif c == 'pink':
    clue = 'clue- \"have you ever turned PINK from embarrassment?\"'
else:
    clue = 'clue- \"frank ocean\'s \(second\) best song is pink+____\"'

while userc != c:
    print(clue)
    userc = input('try again: ')

if c == userc:
    print ('Well done!')