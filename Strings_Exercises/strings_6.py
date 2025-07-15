# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string
# s3 made of the first char of s1, then the last char of s2, Next,
# the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.
#
# Given:
#
s1 = "A"
s2 = "Xyz"

#s3=s1[0]+s2[-1]+s1[1]+s2[-2]+s1[2]
# Expected Output:
# AzbycX
def my_patt(s1,s2):

    s3=""
    if len(s1)>=len(s2):
        c=len(s2)-1
        for i in range(len(s2)):
            s3=s3+s1[i]+s2[c]
            c=c-1
        s3=s3+s1[len(s2):]+s2[len(s1):]
    else:
        c=len(s1)-1
        for i in range(len(s1)):
            s3=s3+s1[i]+s2[c]
            c=c-1
        s3=s3+s2[len(s1):]
    return(s3)
print(my_patt(s1,s2))

