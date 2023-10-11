import random
r = random

score = 0
    
for x in range(5):
    print(f'-QUESTION',x+1,'-')
    n1 =r.randint(0,10)
    n2 =r.randint(0,10)
    ch = int(input(f'What is {n1} + {n2}?\n'))
    a = n1+n2
    if ch == a:
        print('well done!\n')
        score += 1
    if ch != a:
        print('wrong but we move\n')
    
p = score * 20
print(f'you got {score} point(s), or {p}%!!!')