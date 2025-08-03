# Exercise 20: Check if All Values are Unique
# Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.
#
# Given:
#
dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {} # Empty dictionary (all values are vacuously unique)
# Expected Output:
#
# Dictionary: {'a': 1, 'b': 2, 'c': 3} -> All values unique? True
# Dictionary: {'x': 10, 'y': 20, 'z': 10} -> All values unique? False
# Dictionary: {} -> All values unique? True
new=(set(list(dict3.values())))
if len(dict3)==len(new):
    print(True)
elif dict1=={}:
    print(True)
else:
    print(False)
