# exercise 7:Write a program to take three names as input from the user in a single call
# to the input() function.
a=input("Enter three strings")
c=0
for i in a.split(" "):
    c=c+1
    print("Name",c,i)
