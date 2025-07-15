
'''Exercise 18: Replace each special symbol with # in the following string
Given:

str1 = '/*Jon is @developer & musician!!'
Expected Output:

##Jon is #developer # musician##
'''

str1 = '/*Jon is @developer & musician!!'
def disp(str1):

    s1=""
    for i in str1:
        if (i.lower()>="a") and (i.lower()<="z"):
            s1=s1+i
        elif i.isdigit():
            s1=s1+i
        elif i==" ":
            s1=s1+i
        else:
            s1=s1+"#"
    return(s1)
print(disp(str1))
