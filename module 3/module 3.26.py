"""
Write a Python script to concatenate following dictionaries to create a 
new one.
"""
dic_1={1:3,2:4}
dic_2={3:5,4:6}
dic_3={5:7,6:9}
dic4={}
for d in (dic_1,dic_2,dic_3):dic4.update(d)#dic4.update(d) function used to put d in dic4
print("dic4",dic4)