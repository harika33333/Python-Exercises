#Exercise 3: Calculate sum of all numbers from 1 to a given number
#Expected Output
#Enter number 10
#Sum is:  55
sm=0
n=int(input("Enter number "))
for i in range(1,n+1):
    sm=sm+i
print("Sum is: ",sm)
