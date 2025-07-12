#Exercise 4: Remove first n characters from a string

my_str = str(input("Enter a String: "))
num=int(input("enter a number to remove char: "))
def remove_char(num,my_str):
    new_str=""
    for i in range(len(my_str)):
        if i>=num:
            new_str=new_str+ (my_str[i])
    return(new_str)

print(remove_char(num,my_str))

#print(my_str[num:])
