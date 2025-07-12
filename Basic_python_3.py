#Exercise 3: Print characters present at an even index number

'''Expected Output
Orginal String is  PYnative
Printing only even index chars
P
n
t
v'''


my_str=str(input("Enter a string: "))
#method1
#for i in (my_str[::2]):  
 #   print(i)
 
#method 2
def slicing(p):
    d=""
    for i in range(len(p)):
        if i%2==0:
            d=(d+p[i])+"\n"
    return(d)

a=slicing("pynative")
print(a)

#print(my_str[::2])


