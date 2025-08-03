# Exercise 12: Set Symmetric Difference Update
# Write a program to update set1 by adding items from set2 that are not common to both sets.

# Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:

# {70, 10, 20, 60}
no_comm=set2.difference(set1)
set1=set1.difference(set2)
set1.update(no_comm)
print(set1)
