# Exercise 17: Find the sum of a series of a number up to n terms
# Write a program to calculate the sum of this series up to n terms.
# For example, if the number is 2 and the number of terms is 5,
# then the series will be 2+22+222+2222+22222=2469
num=int(input("enter a number: "))
num_terms=int(input("Enter no.of terms:"))
sm=0
for i in range(1,num_terms+1):
    sm=sm+int(str(num)*i)
print(sm)
