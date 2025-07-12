#Exercise 11: Get each digit from a number in the reverse order.
#For example, If the given integer number is 7536, the output shall be
# “6 3 5 7“, with a space separating the digits.
num=int(input("Enter a number: "))
def rev_order(num):
    s=""
    while(num>0):
        rem=num%10
        num=num//10
        s=(s+str(rem))+" "
    return(s)
print(rev_order(num))

