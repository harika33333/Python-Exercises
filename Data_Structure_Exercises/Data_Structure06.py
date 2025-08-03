# Exercise 6: Set Intersection and Removal
# Write a code to find the intersection (common) of two sets and remove those elements from the first set.

# See: Python Set

# Given:
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
# Expectecd Output:

# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}
int_res=first_set.intersection(second_set)
print("Intersection is", int_res)
diff= first_set.difference(second_set)
print("First Set after removing common element",diff)
