#Exercise 2: Print the Sum of a Current Number and a Previous number
'''
expected output
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
'''
#Method 1
'''
num=int(input("enter the range"))
print(f"Printing current and previous number sum in a range({num})")
prev_num=0
for i in range(0,num+1):
    summ =prev_num+i
    print("Current Number ",i,"Previous Number ",prev_num,"Sum:",summ)
    prev_num=i
'''

#method 2
#range function iterates in the given range of integers.
for i in range(0,10):
    prev_num= i-1
    summ = prev_num+i
    if(prev_num<0):
        prev_num=0
        summ=0
    print("Current Number ",i,"Previous Number ",prev_num,"Sum:",summ)


