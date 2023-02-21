"""Write a Python program to calculate surface volume and area of a πr2h
cylinder"""
pie = 22/7
r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
volume = pie * r*r *h
area = (2* pie * r * h )+ (2 * pie * r**2)
print("Volume of the cylinder is : ",volume)
print("Surface area of the cylinder is :", area)
