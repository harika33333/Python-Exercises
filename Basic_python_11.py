#For example, If the given integer number is 7536, the output shall be
# “6 3 5 7“, with a space separating the digits.
n=7536
rev=0
while(n>0):
    rem=n%10
    n=n//10
    print(rem,end=" ")
