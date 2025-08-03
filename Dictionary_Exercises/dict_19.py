# Exercise 19: Sort Dictionary by Values
# Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
#
# Given:
#
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
# Expected Output:
#
# Original dictionary: {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
#
# Sorted by values (as OrderedDict):
# OrderedDict([('Jessa', 3), ('Kelly', 1), ('Jon', 2), ('Kerry', 4), ('Joy', 1)])
new_dict={}
lis=sorted(my_dict.values())
for k in lis:
    for i,j in my_dict.items():
        if j==k:
            new_dict[i]=j
print(new_dict)

