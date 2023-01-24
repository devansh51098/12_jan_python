#collect value from users and convert years into days and months

years=int(input("Enter years= "))
print("Months: ",years*12)
print("Days: ",((years*365)+years//4))