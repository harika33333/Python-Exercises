# Exercise 9: Write a Python code to check if the given number is a palindrome.
# A palindrome number reads the same forwards and backward. For example,
# 545 is a palindrome number.
num=int(input("Enter a number: "))
n=num

def pal_check(n):
    rev=0
    while(n>0):
        rem=n%10#5 4 5
        rev=(rev*10)+rem #5 54 545
        n=n//10 #54 5
    if(rev==num):
        return(True)
    else:
        return(False)
print(pal_check(n))


