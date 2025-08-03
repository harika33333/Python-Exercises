# Exercise 1: Perform Basic Set Operations
# Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.
# Add Element: Add “grape” to the fruits set.
# Remove Element: Remove “banana” from the fruits set.
# Discard Element: Try to discard “mango” from the fruits set.
# Expected Output:

# 1. After creating the set: {'apple', 'orange', 'mango', 'banana'}
# 2. After adding 'grape': {'orange', 'banana', 'grape', 'apple', 'mango'}
# 3. After removing 'banana': {'orange', 'grape', 'apple', 'mango'}
# 4. After discarding 'mango': {'orange', 'grape', 'apple'}

set1={"apple", "banana", "mango","orange"}
set1.add("grape")
print(set1)
set1.remove("banana")
print(set1)
set1.discard("mango")
print(set1)



