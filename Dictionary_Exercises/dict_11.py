# Exercise 11: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
#
# Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# # Keys to extract
# keys = ["name", "salary"]
# Expected output:
#
# {'name': 'Kelly', 'salary': 8000}
lis=[i for i in sample_dict.keys() if i in ["name","salary"]]
print(lis)
my_dict={}
for i,k in sample_dict.items():
    for j in lis:
        if i==j:
            my_dict[i]=k
print(my_dict)

