# Exercise 10: Combine two lists
# Combine given two lists into a single list and print it.
#
# Given:
list_a = [1, 2]
list_b = [3, 4]
# Expected Output:
# [1, 2, 3, 4]

def combine(list_a,list_b):
    list_a+=list_b
    return list_a
print(combine(list_a,list_b))
