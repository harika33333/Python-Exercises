# Exercise 15: Use a lambda with the filter() function to get all even numbers from a list
# Given:
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output:
#
# The even numbers in the list are: [2, 4, 6, 8, 10]


def even_num(num_list):
    s=[]
    for i in num_list:
        if i%2==0:
            s.append(i)
    return(s)
print(" The even numbers in the list are:", even_num(numbers))



