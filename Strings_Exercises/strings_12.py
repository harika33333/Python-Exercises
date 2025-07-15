# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
#
# Given:
#
str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Expected Output:
#
# Last occurrence of Emma starts at index 43
def final_position(str1):

    str2="Emma"
    words=""
    wordlist=[]
    position={}
    for i in range(len(str1)):
        if str1[i] not in [" ","."]:
            words=words+str1[i]
        if str1[i]==" ":
            wordlist.append(words)
            position[words]=(i-(len(words)))
            words=""
    res=f"Last occurrence of Emma starts at index {position['Emma']}"
    return(res)
print(final_position(str1))













