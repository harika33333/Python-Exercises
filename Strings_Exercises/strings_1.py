# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
#
# Given:
#
str1 = "James"
# Expected Output:
#
# Jms
def display(str1):
    return(str1[0]+str1[int(len(str1)/2)]+str1[-1])
print(display(str1))
