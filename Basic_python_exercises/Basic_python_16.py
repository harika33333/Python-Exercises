#Exercise 16: Check Palindrome Number

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

