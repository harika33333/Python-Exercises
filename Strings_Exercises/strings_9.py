# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits
# that appear in the string, ignoring all other characters.
# Given:
#
str1 = "PYnative29@#8496"
# Expected Outcome:
#
# Sum is: 38 Average is  6.333333333333333
def sum_avg(str1):
    summ=0
    count=0
    for i in str1:
        if i.isdigit():
            summ=summ+int(i)
            count=count+1
    res=f"Sum is: {summ} Average is  {summ/count}"
    return(res)
print(sum_avg(str1))





