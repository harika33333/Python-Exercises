# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() with the following specifications:
#
# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000

def showEmployee(emp_name,emp_sal=9000):
    return (emp_name+" "+str(emp_sal))
print(showEmployee("Ben",12000))
print(showEmployee("Jessa"))







showEmployee("Ben", 12000)
showEmployee("Jessa")
