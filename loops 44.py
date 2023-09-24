n = int(input("how many people do you want to invite to a party? "))
list = []

for i in range(n):
    name = input('who do you want to invite? ')
    list.append(name)
    print(name,"has been invited.")

print("you invited",n,"people")
print('the people you invited are',*list)