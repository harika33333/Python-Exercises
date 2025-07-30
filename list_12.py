# Exercise 12: Remove Duplicates from list
# Write a function that takes a list with duplicate elements and
# returns a new list with only unique elements.
#
# Given:
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
#
# Expected Output:
# [1, 2, 3, 4, 5]
def rem_dup(list1):
    list1=list(set(list1))
    return list1
print(rem_dup(list_with_duplicates))

