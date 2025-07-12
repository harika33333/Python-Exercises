#Exercise 22: Capitalize the first letter of each word in a string


str1 = str(input("enter a string: "))
def capital(str1):
    s=""
    str1=str1.split(" ")
    for i in str1:
        s=s+i.capitalize()+" "
    return(s)
print(capital(str1))

