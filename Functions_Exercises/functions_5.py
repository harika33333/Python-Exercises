# Exercise 5: Create an inner function
# Create a program with nested functions to perform an addition calculation as follows:
#
# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”

def out_fun():
    a=5
    b=3
    def in_fun():
        nonlocal a, b
        return(a+b)
    return (a+b+5)
print(out_fun())



