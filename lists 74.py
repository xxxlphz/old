list = ["green","blue","black","red","pink","purple","yellow","orange","marshmallow","white"]
int1 = int(input("choose a number from 0 to 4: "))
int2 = int(input("choose number from 5 to 9"))

print (*list[int1+1:int2])