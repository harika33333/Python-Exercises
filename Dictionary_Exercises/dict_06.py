# Exercise 6: Count Character Frequencies
# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
#
# Given:
string1 = 'Jessa'
# Expected Output:
# Frequencies for 'Jessa': {'J': 1, 'e': 1, 's': 2, 'a': 1}
count={}
for i in string1:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)
