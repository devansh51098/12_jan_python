#accept principle amount , term and rate of interest from user

P = int(input("enter amount:"))
R = int(input("rate of interest:"))
N = int(input("no. of years:"))

ROI = P*R*N/100
print(int(ROI))
 