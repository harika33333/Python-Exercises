# Exercise 7: Print the following pattern
# Write a Python program to print the reverse number pattern using a for loop.
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

s=""
for i in range(5,0,-1):
    s=s+str(i)+" "
for i in range(0,len(s),2):
    print(s[i::])

############with functions#########
def rev_patt():
    s=""
    res=""
    for i in range(5,0,-1):
        s=s+str(i)+" "
    for i in range(0,len(s),2):
        res=res+(s[i::])+"\n"
    return(res)
print(rev_patt())

