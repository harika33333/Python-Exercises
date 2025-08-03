# Exercise 9: Create a copy of a list
# Create a copy of a list [10, 20, 30] and modify the copy.
# Print both the original and the copied list to demonstrate they are independent.
list1=[1,2,3]



def copy_list(list1):
    list2=list1
    list2=list1+[345]
    #print(list1,list2)
    #print(id(list1),id(list2))
    return(list1,list2)
original,copied=copy_list(list1)
print("original list",original)
print("copied list", copied)



