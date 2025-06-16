# Write a Python code to check if the given number is a palindrome.
# A palindrome number reads the same forwards and backward. For example,
# 545 is a palindrome number.
num=545
n=num
rev=0
while(n>0):
    rem=n%10#5 4 5
    rev=(rev*10)+rem #5 54 545
    n=n//10 #54 5
if(rev==num):
    print(True)
else:
    print(False)

n=1221
number=str(n)
number=number[::-1]
b=int(number)
print(b)
if(n==b):
    print(True)
else:
    print(False)

