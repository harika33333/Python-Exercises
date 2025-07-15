#Exercise 15: Remove special symbols / punctuation from a string
# Given:
str1 = "/*Jon is @developer & musician"
#Expected Output:  "Jon is developer musician"
def rem_symbols(str1):

    s1=""
    for i in str1:
        if (i.lower()>="a") and (i.lower()<="z"):
            s1=s1+i
        elif i.isdigit():
            s1=s1+i
        elif i==" ":
            s1=s1+i
        else:
            continue
    return(s1)
print(rem_symbols(str1))

