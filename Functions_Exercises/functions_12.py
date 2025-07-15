# Exercise 12: Modifies global variable
# Define a global variable global_var = 10. Write a function that modifies a global variable value.

global_var=10

def variable():
    global global_var
    global_var=20
    return global_var

print(global_var)# before changing the global Variable value
print(variable())#after changing the global Variable Value


