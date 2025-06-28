#Exercise 17: Generate Fibonacci series up to 15 terms
'''It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 
The next number in this series is 13 + 21 = 34.
'''
'''expected output
Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
'''

n1=0
n2=1
print("Fibonacci sequence:")
n=int(input())
while(n>0):
    print(n1,end=" ")
    sm=n1+n2
    n1=n2
    n2=sm
    n=n-1
