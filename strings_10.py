# Exercise 10: Write a program to count occurrences of all characters within a string
# Given:
#
str1 = "Apple"
# Expected Outcome:
#
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}
def count_occurences(str1):

    count={}
    for i in str1:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    return(count)
print(count_occurences(str1))
