# Exercise 11: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:
#
# # ["Mike", "Emma", "Kelly", "Brad"]
def rem_emp(list1):
    if "" not in list1:
        return list1
    list1.remove("")
    return (rem_emp(list1))
print(rem_emp(list1))

