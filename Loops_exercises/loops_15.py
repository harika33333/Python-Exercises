# Exercise 15: Print elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def odd_list(my_list):
    c=0
    res=""
    for i in my_list:
        if c%2!=0:
            res=res+str(i)+" "
        c=c+1
    return(res)
print(odd_list(my_list))

