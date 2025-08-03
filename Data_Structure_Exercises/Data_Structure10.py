# Exercise 10: remove duplicates from a list
# Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number

# Given:

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:

# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

l1=[]
count={}
for i in sample_list:
    if i in count:
        pass
    else:
        count[i]=1
        l1.append(i)
print("unique items",l1)
print("tuple",tuple(l1))
print(max(l1))
print(min(l1))
        






