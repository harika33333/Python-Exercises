# Exercise 5: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
#
# Given:
numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
# [1, 4, 9, 16, 25, 36, 49]
def squares(numbers):
    if numbers==[]:
        return []
    return [numbers[0]**2]+squares(numbers[1:])
print(squares(numbers))
