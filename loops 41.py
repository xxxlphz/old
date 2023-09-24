name = str(input("what your name "))
num = int(input("choose a number "))

if num <= 10:
    for i in range(num):
        print(name)
        
else:
    for i in range(3):
        print("Too high")