# Exercise 18: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# Expected output:
#
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
def conc_lists(list1,list2):
    return [i+j for i,j in zip(list1,list2)]
print(conc_lists(list1, list2))
