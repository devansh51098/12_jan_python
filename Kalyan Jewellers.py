print("Welcome to Kalyan Jewellers ")

Name = input("Enter customer's name : ")
Gender = input("Enter 'm' for male and 'f' for female : ")
age = int(input("Enter the age : "))
product = input("type of product : ")
grams = int(input("total weight : "))
gold_price = int(input("Enter current gold price : "))

print("Name : ",Name)
print("Gender :",Gender)
print("Age :" ,age)
print("product : ",product )
print("Gram : " ,grams)
print("Gold Price :" ,gold_price)

making_charges = int(input("Enter making charges per gram:"))
print(making_charges,"M_charges")

gross_rate = gold_price * grams
print(gross_rate,"gross rate")

total_rate = gross_rate + (making_charges *grams)
print(total_rate,"Total rate")

discount = 0
if Gender == 'm' and age > 65:
    if total_rate > 200000:
        print("Discount 20%")
        discount = int(total_rate) * 20 / 100
    elif total_rate > 300000:
        print("Discount 30%")
        discount = int(total_rate) * 30 / 100
    elif total_rate > 500000:
        print("Discount 35%")
        discount = int(total_rate) * 35 / 100
    else:
        print("No discount")

        if Gender== 'm' and age< 65: 
            if total_rate>200000:
                print("Discout 10%")
                discount=(total_rate)*10/100
            elif total_rate>300000:
                print("Discount 20%")
                discount=(total_rate)*20/100
            elif total_rate>500000:
                print("Discount 25%")
                discount=(total_rate)*25/100
            else:
                print("No Discount")

if Gender=='f' and age<=65:
    if total_rate>200000:
            print("Discount 20%")
            discount=int(total_rate)*20/100
    elif total_rate>300000:
            print("Discount 30%")
            discount=int(total_rate)*30/100
    elif total_rate>500000:
            print("Discount 35%")
            discount=int(total_rate)*35/100
    else:
            print("No discount")

if Gender=='f' and age>65:
    if total_rate>200000:
                print("Discount 15%")
                discount=(total_rate)*15/100
    elif total_rate>300000:
             print("Discount 25%")        
             discount=(total_rate)*25/100
    elif total_rate>500000:
                print("Discount 30%")
                discount=(total_rate)*30/100
    else:
                print("No Discount")
net_amt=(total_rate-making_charges)-discount
print("Discount Amount :",net_amt)

dis_amount=total_rate-net_amt
print("Total Net Amount :",net_amt)
