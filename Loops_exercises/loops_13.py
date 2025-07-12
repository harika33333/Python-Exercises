#Exercise 13: Find the factorial of a given number
# Write a Python program to use for loop to find the factorial of a given number.
# The factorial (symbol: !) means multiplying all numbers
# from the chosen number down to 1.
#
# For example, a factorial of 5! is 5 × 4 × 3 × 2 × 1 = 120
n=int(input("enter a number"))
def factorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return(fact)
print(factorial(n))

