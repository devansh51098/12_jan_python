import operator
d={'a':2,'b':4,'c':8,'d':10,'e':11,'f':90,'g':3,'h':11,'i':9}
print("original dictionary",d)
ascending_d=sorted(d.items(),key=operator.itemgetter(1))
print(ascending_d)
descending_d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print(descending_d)
