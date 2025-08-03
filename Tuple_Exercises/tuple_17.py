# Exercise 17: Sort a tuple of tuples by 2nd item
# Given:
tuple1 = (('a', 23),('b', 37),('c', 11),('d',29))
# Expected output:
# (Sorted tuple by 2nd item: (('c', 11), ('a', 23), ('d', 29), ('b', 37))
val_lis=[]
for i in tuple1:
    val_lis.append(i[1])
val_lis=sorted(val_lis)
lis=[]
for i in val_lis:
    for j in tuple1:
        if i==j[1]:
            lis.append(j)
print(lis)
