# Exercise 14: Remove empty strings from a list of strings
# Given:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

print("Original list of sting")
print(str_list)
def rem_empty(str_list):
    lis=[]
    for i in str_list:
        if i:
            lis.append(i)
    s="After removing empty strings\n"+str(lis)
    return(s)
print(rem_empty(str_list))

