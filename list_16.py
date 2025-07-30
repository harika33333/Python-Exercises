# Exercise 16: Flatten Nested List
# Write a function to flatten a list of lists into a single,
# non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).
#
# Given:
list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
# Expected Output:
# [1, 2, 3, 4, 5, 6, 7]

def flatten(list1):
    return [j for i in list1 for j in i]
print(flatten(list_of_lists))




