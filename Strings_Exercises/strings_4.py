# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters
# should come first.
#
# Given:
#
str1 = "PyNaTive"
# Expected Output:
#
# yaivePNT
def low_up(str1):
    small=""
    caps=""
    for i in str1:
        if i==i.lower():
            small=small+i
        else:
            caps=caps+i
    return(small+caps)


