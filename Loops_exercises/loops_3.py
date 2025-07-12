#Exercise 3: Calculate sum of all numbers from 1 to a given number
#Expected Output
#Enter number 10
#Sum is:  55
def cal_sum(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+i
    return(sm)
n=int(input("Enter number "))
sm=cal_sum(n)
print("The result is",sm)
