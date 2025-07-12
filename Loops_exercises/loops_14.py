# Exercise 14: Reverse a integer number
# Given:
# 76542
# Expected output:
# 24567
n=int(input("Enter a number"))
def rev_num(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return(rev)
print(rev_num(n))

