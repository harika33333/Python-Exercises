# Exercise 6: Create a recursive function
# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself repeatedly.
#
# Expected Output:
#
# 55

def plus(n):
    if n == 0:
        return 0
    else:
        return n+plus(n-1)
print(plus(10))

