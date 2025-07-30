# Exercise 3: Sum and average of all numbers in a list
# Calculate and print the sum and average of all numbers in a list.
#
# Given:
#
my_list = [10, 20, 30, 40, 50]
# Expected Output:
#
# Sum: 150
# Average: 30.0

def summ(my_list):

   if my_list==[]:
       return 0
   return(my_list[0]+summ(my_list[1:]))
print("sum: ", summ(my_list))
print("Average: ", summ(my_list)/len(my_list))

