# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
#
# Given:
#
str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output:
#
# Emma25
# scientist50
def alpha_num(str1):
    str1=str1.split(" ")
    res=""
    for i in str1:
        charr=0
        digit=0
        for j in i:
            if (j.lower()>="a" and j.lower()<="z"):
                charr=charr+1
            if(j.isdigit()):
                digit=digit+1
            if (charr and digit)>=1:
                res=res+(i)+"\n"
                break
    return(res)
print(alpha_num(str1))







