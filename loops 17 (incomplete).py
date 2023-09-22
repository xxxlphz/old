#loops 17

age = int(input("What is your age? "))

if age <= 18:
    print("you can vote!")
    
elif age == 17:
    print("you can drive")
    
elif age == 16:
    print("you can buy a lottery ticket")
    
elif age < 16:
    print("you can go trick or treating ")