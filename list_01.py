# Exercise 1: Perform Basic List Operations
# Given:

my_list = [10, 20, 30, 40, 50]
# Perform following operations on given list

# Access Elements: Print the third element.
# List Length: Print the number of elements in the list
# Check if Empty: Write a code to check is list empty.
# Expected Output:

# Initial list: [10, 20, 30, 40, 50]

# Third item:  30
# Length of the list: 5
# list is not empty
def basic_op(my_list):
    s=f"Initial list: {my_list}\n"
    if(len(my_list)>=3):
        s=s+(f"Third item: {my_list[2]}\n")
    else:
        s=s+("list index is out of range\n")

    s=s+f"Length of the list: {len(my_list)}\n"
    if my_list:
        s=s+("list is not empty\n")
    else:
        s=s+("list is empty\n")
    return s

print(basic_op(my_list))
    



