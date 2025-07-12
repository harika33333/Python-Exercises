#Exercise 2: Print the following pattern
#Write a Python code to print the following number pattern using a loop.

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

def my_patt(n):
    num_list = ""
    s=""
    for i in range(1,n+1):
        num_list+=str(i)+" "
        s=s+num_list+"\n"
    return s

print(my_patt(n=5))
