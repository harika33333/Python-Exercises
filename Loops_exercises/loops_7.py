# Exercise 7: Print the following pattern
# Write a Python program to print the reverse number pattern using a for loop.
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5,0,-1):
    c=i
    for j in range(i):
        print(c,end=" ")
        c=c-1
    print()
