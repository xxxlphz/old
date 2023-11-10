bottles = 10

while bottles != 0:
    print(f'\"There are {bottles} green bottles hanging on the wall, {bottles} green bottles hanging on the wall, and if 1 green bottle should accidentally fall\"')
    bottles -= 1
    que = int(input('how many green bottles will be hanging on the wall? '))
    while que != bottles:
        print("wrong try again")
        que = int(input('how many green bottles will be hanging on the wall? '))
            
print('WOOOOOOOOOOOOOOOOHOOOOOOOOO')
        
