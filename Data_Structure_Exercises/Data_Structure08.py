# Exercise 8: Filter List Against Dictionary Values
# Write a program to iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

# Given:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Expected Outcome:

# After removing unwanted elements from list [47, 69, 76, 97]
l1=[]
for i in roll_number:
    for j in sample_dict:
        #print(i,sample_dict[j])
        if(i==sample_dict[j]):
            l1.append(i)
print(l1)

