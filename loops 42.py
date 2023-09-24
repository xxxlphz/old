ttl = int(0)

for i in range(5):
    num = int(input("choose a number "))
    inc = input("do you wanna include this  number? ")
    if inc == "yes":
        ttl += num

print(ttl)