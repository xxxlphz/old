n1 = input("Name someone you wanna invite to a party: ")
n2 = input("ANOTHER ONE (DJ KHALED!): ")
n3 = input("A third person: ")

list = [n1, n2, n3 ]

ans = input("do you wanna invite someone else? " )

def func():
    
    
    if ans == "yes" or "Yes":
        n4 = input("whats their name: ")
        ans2 = input("do you wanna invite another person? " )
        list.append(n4)
        if ans2 == "yes":
            func()
        
        else:
            print ( "\n\nyouve invited", len(list), "people to the party")
            print("the people you invited are", *list)
            
    else:
        print ( "\n\nyouve invited", len(list), "people to the party")
        print("the people you invited are", *list)

func()