# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
#
# Given:
# Case 1
str1 = "JaSonAy"
# Output
# Dip
mid=int(len(str1)/2)
print(mid)
print(str1[mid-1]+str1[mid]+str1[mid+1])
