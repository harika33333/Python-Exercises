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
for i in range(len(my_str)):
    if i%2==0:
        print(my_str[i])
        
#print(my_str[::2])


