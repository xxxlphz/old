dir = input("do you want to count up or down? ")

if dir == "up":
    n = int(input("choose your final number "))
    for i in range(n):
        print(i+1)
        
elif dir == "down":
    n = int(input("choose a number below 20 "))
    for i in range(n):
        print(n-i)
else:
    print("i dont understand")