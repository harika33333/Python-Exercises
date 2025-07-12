#Exercise 20: Print Reverse Number Pattern

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
def my_pattern(n):
    s=""
    c=5
    for i in range(1,n+1):
        s=s+((str(i)+ " ")*c)+"\n"
        c=c-1
    return(s)
print(my_pattern(5))

