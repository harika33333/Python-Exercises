#Exercise 11: Get each digit from a number in the reverse order.
#For example, If the given integer number is 7536, the output shall be
# “6 3 5 7“, with a space separating the digits.
num=int(input("Enter a number: "))
rev=0
while(num>0):
    rem=num%10
    num=num//10
    print(rem,end=" ")
