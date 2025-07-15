# Exercise 5: Count all letters, digits, and special symbols from a given string
# Given:
#
str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
#
# Total counts of chars, digits, and symbols
#
# Chars = 8
# Digits = 3
# Symbol = 4
def count(str1):
    chars=0
    digits=0
    symbols=0
    for i in str1:
        if i.isdigit():
            digits=digits+1
        elif (i.lower()>="a") and (i.lower()<="z"):
            chars=chars+1
        else:
            symbols=symbols+1
    s=f"Total counts of chars, digits, and symbols \nChars = {chars}\nDigits = {digits}\nSymbol = {symbols}"
    return(s)
print(count(str1))
