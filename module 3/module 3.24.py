
t1 = [("Raju",90),("Ram",78),("Riya",69)]
d1 = dict()

for student,score in t1:
    d1.setdefault(student,[]).append(score)
print(d1)
