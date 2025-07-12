# Exercise 8: patterns
#expected output
#1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
def my_pattern():
    s=""
    for i in range(1,6):
        s=s+((str(i)+" ")*i)+"\n"
    return(s)
print(my_pattern())




