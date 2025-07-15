# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
#
# Given:
#
str1 = "Welcome to USA. usa awesome, isn't it?"
str2="USA"
# Expected Outcome:
#
# The USA count is: 2
def count(str1):

    s1=""
    for i in str1:
        if i!=".":
            s1=s1+i
        else:
            pass
    #print(s1)
    str1=s1.split(" ")
    #print(str1)
    count=0
    for i in str1:
        if str2.lower() in i.lower():
             count=count+1
    res=f"The {str2} count is: {count}"
    return res
print(count(str1))


