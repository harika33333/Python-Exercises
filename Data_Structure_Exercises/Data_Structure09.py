# Exercise 9: Extract Unique Dictionary Values to List
# Write a code to get all values from the dictionary and add them to a list but don’t add duplicates

# Given:

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# Expected Outcome:

# [47, 52, 44, 53, 54]
# l1=[]
# count={}
# for i in speed:
#     #print(i,speed[i])
#     if(speed[i]  in count):
#         pass
#     else:
#         count[speed[i]]=1
#         l1.append(speed[i])

# print(l1)

l1=list(set(speed.values()))
print(l1)

