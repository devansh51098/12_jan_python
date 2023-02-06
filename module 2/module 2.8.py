integer_1 = int(input("Enter integer 1 "))
integer_2 = int(input("Enter integer 2 "))

status = True 
if integer_1 + integer_2 == 5 or integer_1 - integer_2 ==5 or integer_1==integer_2:
    print("true")
else:
    print('false')