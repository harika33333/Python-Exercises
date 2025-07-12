# Exercise 6: Count the total number of digits in a number
# Write a Python program to count the total number of digits in a number using a while loop.
#
# For example, the number is 75869, so the output should be 5.
n=int(input("Enter a Number: "))
def count_digits(n):
    count=0
    while(n>0):
        rem=n%10
        count=count+1
        n=n//10
    return(count)
print(count_digits(n))s
