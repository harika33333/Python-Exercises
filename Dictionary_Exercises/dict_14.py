# Exercise 14: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
#
# Given:
#
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# Expected output:
#
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

sample_dict.popitem()
sample_dict["location"]="New york"

print(sample_dict)
