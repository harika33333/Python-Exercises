#Exercise 6: Display numbers divisible by 5
'''Expected output
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55'''

num=[10, 20, 33, 46, 55]

def div_5():
    global num
    num=[28,24,635,89,20]
    lis=[]
    for i in num:
        if (i%5==0):
            lis.append(i)
    return(lis)
#print(num)
a=div_5()
print(f"Given list is {num}")
print("Divisible by 5",a)


