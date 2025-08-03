# Exercise 16: Count Unique Words
# Write a code to count the number of unique words in the given a sentence.

# Given:

sentence = "dog is a simple animal dogs is selfless animal"
# Expected Output:

# Number of unique words: 7
l1=sentence.split(" ")
#print(l1)
print("Number of unique words:",len(set(l1)))
