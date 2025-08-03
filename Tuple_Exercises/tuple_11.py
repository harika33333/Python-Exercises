# Exercise 11: Function Returning Tuple
# Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.
#
# Given:
#
def get_min_max(numbers):
        # Write your code here
    mini=min(numbers)
    maxi=max(numbers)
    tuple1=(mini,maxi)
    return tuple1
# # Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")

# Expected Output:
#
# Original numbers: [10, 5, 20, 2, 15]
# Minimum and maximum values: (2, 20)
