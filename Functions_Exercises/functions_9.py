# Exercise 9: Find the largest item from list
# Given:
# x = [4, 6, 8, 24, 12, 2]
# Expected Output:
# 24


x = [4, 6, 8, 24, 12, 2]
def my_max(x):
    mx=0
    for i in x:
        if i>mx:
            mx=i
    return mx
print(my_max(x))
