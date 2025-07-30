# Exercise 4: Reverse a list
# Given:
list1 = [100, 200, 300, 400, 500]
# Expected output:
# [500, 400, 300, 200, 100]

def rev(list1):
    #list1=list1[::-1]
    list1.reverse()
    return(list1)
print(rev(list1))

