import hashlib
import os

# hash table -------------------------------------------------------------------

class hash_table_class():
    def __init__(self):
        self.hash_table = [None, None, None, None, None, None, None, None, None, None, None]
    def add(self, x):
        pos = x % (len(self.hash_table))
        self.hash_table[pos] = x

    def delete_hash(self, x):
        pos = x % (len(self.hash_table))
        self.hash_table[pos] = None

    def print_hash(self):
        print self.hash_table

h = hash_table_class()
h.add(54)
h.add(26)
h.print_hash()
h.delete_hash(54)
h.print_hash()
# dictionary comprehension -----------------------------------------------------
'''
# zip two lists into a dictionary

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
hash_values = {k:v for k, v in zip(keys, values)}

for k, v in hash_values.items():
    print k, ':', v

# square each value in the list
squared_hash = {k:v**2 for (k,v) in hash_values.items()}
print (squared_hash)

# this can be done to the keys as well
hash_keys = {k*2:v for (k,v) in hash_values.items()}
print(hash_keys)

# create a dictionary with all keys divisible by 2 and the values the square
# alternate to a for loop
dict = {n:n**2 for n in range(0, 10) if n%2 == 0}
print(dict)

# if conditions
dict_1 = {k:v for k, v in zip(keys, values)}
dict_1_if = {k:v for (k, v) in dict_1.items() if v%2 == 0}
print(dict_1_if)



# https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
'''
