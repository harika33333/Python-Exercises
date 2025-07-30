# Exercise 13: Remove all occurrences of a specific item from a list
# Given a Python list, write a program to remove all occurrences of item 20.
#
# Given:
#
list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
#
# [5, 15, 25, 50]
def rem_occurences(list1):
    if 20 not in list1:
        return(list1)
    list1.remove(20)
    return rem_occurences(list1)
print(rem_occurences(list1))
