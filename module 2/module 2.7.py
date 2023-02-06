x = int(input("Enter your first integer : "))
y = int(input("Enter your second integer : "))
z = int(input("Enter your third integer : "))
sum = x+y+z 

if x==y or y==z or z==x:
    print("0")
else:
    print(sum)
