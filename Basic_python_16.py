#Exercise 16: Check Palindrome Number
n=int(input("Enter a number: "))
num=n
rev=0
while(n>0):
     rem=n%10
     rev=rev*10+rem
     n=n//10
# print(rev)
if(rev==num):
    print(True)
else:
    print(False)
