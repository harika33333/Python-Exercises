# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

# Given:

list1 = [34, 54, 44, 27, 79, 91, 41]
# Expected Output:

# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
rem_lis=[]
rem=[]

for i in range(len(list1)):
    if i!=4:
        rem_lis.append(list1[i])
    else:
        rem.append(list1[i])
add_lis=rem_lis[:2]+rem+rem_lis[3:]
add_end=add_lis+rem
print("List After removing element at index 4",rem_lis)
print("List after Adding element at index 2",add_lis)
print("List after Adding element at last ",add_end)        

    
        
        
