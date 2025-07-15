# Exercise 14: Create a lambda function that squares a given number
# A lambda function in Python is a small anonymous function defined using the lambda keyword.
# The syntax is lambda arguments: expression. The expression is evaluated and returned.
n=2
squares=(lambda n: n*n)
print(squares(n))


def square(n):
    return (n*n)
print(square(n))
