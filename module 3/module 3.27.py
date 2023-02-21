"""
Write a Python script to check if a given key already exists in a 
dictionary.
""" 
d={1:10,2:20,3:30,4:40,5:50,6:60}

def present(x):
    if x in d:
        print("key present")
    else:
        print("key not present")
present(6)
present(10)
