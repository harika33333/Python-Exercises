#Exercise 21: Check if a user-entered string contains any digits using a for loop

# Enter a string: Pynative123Python
# The string contains at least one digit.

# Enter a string: PYnative
# The string does not contain any digits.
    
str_in=str(input("Enter a String: "))
c=0
for i in str_in:
    if i.isdigit():
        c=c+1
# print(c)
if c>0:
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")
