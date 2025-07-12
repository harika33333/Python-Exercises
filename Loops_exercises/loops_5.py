# Exercise 5: Display numbers from a list using a loop
# Write a Python program to display only those numbers from a list that satisfy the following conditions
#
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop



def my_list(*numbers):
    s=""
    for i in numbers:
        if i%5==0:
            if i>500:
                break
            elif i>150:
                continue
            else:
                s=s+str(i)+"\n"
    return(s)
print(my_list(12, 75, 150, 180, 145, 525, 50))

