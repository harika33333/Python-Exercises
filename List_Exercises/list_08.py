# Exercise 8: Sort a list of numbers
# Sort a given list of numbers in ascending order and print it.
#
# Given:
numbers = [5, 2, 8, 1, 9]
#
# Expected Output:
#
# Original list: [5, 2, 8, 1, 9]
# Sorted list: [1, 2, 5, 8, 9]

def sorting(numbers):
    numbers.sort()
    return numbers
print(sorting(numbers))
