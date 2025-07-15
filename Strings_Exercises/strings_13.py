# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
# Given:
str1 = "Emma-is-a-data-scientist"
# Expected Output:
# Displaying each substring
# Emma
# is
# a
# data
# scientist
def display(str1):

    str1=str1.split("-")
    s="Displaying each substring\n"
    for i in str1:
        s=s+i+"\n"
    return(s)
print(display(str1))


