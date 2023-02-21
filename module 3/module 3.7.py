"""Write a Python function that takes a list and returns a new list with unique 
elements of the first list."""

l1 = [12,4,54,2,12,5,2]

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)


s = set(l1)
print(s)