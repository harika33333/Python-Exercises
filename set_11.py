# Exercise 11: Set Intersection Check
# Write a code to check if two sets have any elements in common. If yes, display the common elements

# Given:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
# Expected output:

# Two sets have items in common
# {10}
if set1.intersection(set2):
    print("two sets have items in common")
    print(set1.intersection(set2))
