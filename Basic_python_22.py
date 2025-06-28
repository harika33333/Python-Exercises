#Exercise 22: Capitalize the first letter of each word in a string


str1 = str(input("enter a string: "))

str1=str1.split(" ")
for i in str1:
    print(i.capitalize(),end=" ")
