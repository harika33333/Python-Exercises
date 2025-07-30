# Exercise 15: Access Nested Lists
# Given a nested list, print the element '55'.
#
# Given:

nested_list =[[10, 20, 30], [44, 55, 66], [77, 87, 99]]

def nested_access(list1):
    return nested_list[1][1]
print(nested_access(nested_list))

