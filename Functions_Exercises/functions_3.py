# Exercise 3: Return multiple values from a function
# Write a function calculation() that accepts two variables and calculates both their
# addition and subtraction. The function should then return both the sum and the difference
# in a single return statement.

def calculation(a,b):
    sm=a+b
    minus=a-b
    return sm,minus
res = calculation(40, 10)
print(res)

