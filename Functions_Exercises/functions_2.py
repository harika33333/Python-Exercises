# Exercise 2: Create a function with variable length of arguments
# Write a program to create a function func1() that accepts a variable number
# of arguments and prints each of their values.

# Note: Create this function so that it can receive any number of arguments,
# process them, and display the value of each individual argument.

def func1(*var_num):
    s="Printing values\n"
    for i in var_num:
        s=s+str(i)+"\n"
    return s
# call function with 3 arguments
print(func1(20, 40, 60))

# call function with 2 arguments
print(func1(80, 100))

