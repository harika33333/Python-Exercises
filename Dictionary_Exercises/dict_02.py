#
# Exercise 2: Perform dictionary operations
# Given:
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
# Perform following operations on given dictionary
#
# Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
# Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary
# Expected Output:
#
# Original dictionary: {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#
# Updated dictionary after removing 'profession': {'name': 'Alice', 'age': 35, 'city': 'New York'}
#
# Printing all key-value pairs:
# name: Alice
# age: 35
# city: New York
#
# Does 'age' exist? True
del_item=my_dict.popitem()
print(my_dict)
for i,j in my_dict.items():
    print(i+":"+str(j))

if 'age'in my_dict:
    print(True)
else:
    print(False)


