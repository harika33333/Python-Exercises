# Exercise 15: Print elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
c=0
for i in my_list:
    if c %2!=0:
        print(i,end=" ")
    c=c+1
