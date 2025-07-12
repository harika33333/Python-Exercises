#Exercise 1: Given two integer numbers, write a Python program to return their product 
#if the product is equal to or lower than 1000. Otherwise, return their sum.

#Expected Output
#number1 = 20
#number2 = 30
#The result is 600


num1= int(input("enter number 1: "))
num2= int(input("enter number 2: "))

def mull(num1,num2):
    prod=(num1 * num2)
    if(prod <=1000):
        return prod
    else:
     return(num1+num2)
print("The result is",mull(num1,num2))

