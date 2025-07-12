#Exercise 2: Print the following pattern
#Write a Python code to print the following number pattern using a loop.

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5


n = 5

num_list = ""

for i in range(1,6):
    num_list+=str(i)+" "
    print(num_list)

