"""
Write a Python program to remove an empty tuple(s) from a list of tuples. 
"""

list = [(), (), ('',), ('p', 'r'), ('p', 'r', 'i'), ('y')]
list = [t for t in list if t]
print(list)