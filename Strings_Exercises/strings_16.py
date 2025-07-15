# Exercise 16: Removal all characters from a string except integers
# Given:
#
str1 = 'I am 25 years and 10 months old'
# Expected Output:
#
# 2510
def rem_chars(str1):

    s1=""
    for i in str1:
        if i.isdigit():
            s1=s1+i
    return(s1)
print(rem_chars(str1))
