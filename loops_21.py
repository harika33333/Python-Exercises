# Exercise 21: Flatten a nested list using loops
# Write a program to flatten a nested list using loops.
# Given:
nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

# # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
lis=[]
for i in nested_list:
    if type(i)==list:
        for j in i:
            lis.append(j)
    else:
        lis.append(i)

print(lis)
