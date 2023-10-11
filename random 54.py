import random
r = random

n = r.choice('ht')
choice = input('choose either heads (h) or tails (t) ')

if choice == n:
    print('You win')
    
else:
    print('You lose')
