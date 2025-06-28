# Exercise 12: Display Fibonacci series up to 10 terms
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
n1=0
n2=1
n=int(input("enter the no. of terms:"))
for i in range(0,n):
    sm=n1+n2
    print(n1)
    n1=n2
    n2=sm
