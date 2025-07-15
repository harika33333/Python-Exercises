# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
def my_patt():
    res=""
    for i in range(1,6):
        res=res+("* "*i)+"\n"
    for i in range(4,0,-1):
        res=res+("* "*i)+"\n"
    return(res)
print(my_patt())


