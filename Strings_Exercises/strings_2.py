# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3
# by appending s2 in the middle of s1.
# Given:
s1 = "Ault"
s2 = "Kelly"
# Expected Output:
# AuKellylt
def appending(s1,s2):
    mid=int(len(s1)/2)
    s3=""
    c=1
    for i in range(len(s1)):
        s3=s3+s1[i]
        if c==mid:
            s3=s3+s2
        c=c+1
    return(s3)
print(appending(s1,s2))



