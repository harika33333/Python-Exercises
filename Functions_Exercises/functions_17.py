# Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based
# on the second element
# Given:
#data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
# Expected Output:
# The sorted list of tuples based on the second element is:
# [('date', 1), ('banana', 2), ('apple', 5), ('cherry', 8)]

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

sort_list= []
for i,a in data:
    if str(a).isdigit():
        #if isinstance(a,int):
            sort_list.append(a)

b=sorted(sort_list)
#[1,2,5,8]
res=[]
for c in b:
    for i,d in data:
        #print (d,c)
        if(d==c):
            #print(i,d)
            res.append((i,d))
print(res)











