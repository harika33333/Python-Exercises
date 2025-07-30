# Exercise 6: Find Maximum and Minimum
# Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].
#
# Given:
#
data = [8, 2, 15, 1, 9]
# Expected Output:
#
# Largest number: 15
# Smallest number: 1
def max_min(data):
    res=f"Largest number: {max(data)}\n"
    res=res+f"Smallest number: {min(data)}"
    return res
print(max_min(data))
