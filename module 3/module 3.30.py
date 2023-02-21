#Write a Python script to merge two Python dictionaries

d1={1:2,2:3,3:4,4:5}
d2={5:6,6:7,7:8,8:9}
d3=d1.copy()
d3.update(d2)
print(d3)
print(d1|d2)
