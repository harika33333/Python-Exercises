#Exercise 4: Print multiplication table of a given number

num=int(input("enter a number"))
def mul_table(num):
    s=""
    for i in range(1,11):
        prod=num*i
        s=s+str(prod)+"\n"
    return(s)
print(mul_table(num))
