# Exercise 12: Comparing Tuples
# Compare two tuples and find out which one is “greater” and why?
#
# Given:
t1 = (1, 2, 4,5)
t2 = (1, 2, 4,5)
# Expected Output:
# Tuple 1: (1, 2, 3, 8)
# Tuple 2: (1, 2, 4, 5)
# (1, 2, 3, 8) is less than (1, 2, 4, 5)
if t1<t2:
    print("t1 is lesser than t2")
elif t1>t2:
    print("t2 is lesser than t1")
else:
    print("they are equal")
