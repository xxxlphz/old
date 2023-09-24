#loops 18

def func():
    num = int(input("Enter a number: "))
    
    if num < 10:
        print("\nToo low\n")
        
        print("Try again:")
        
        func()
    
    elif num <= 20 and num >= 10:
        print("\nCorrect")
    
    else:
        print("\nToo high\n")
        
        print("Try again:")
        
        func()
    
func()