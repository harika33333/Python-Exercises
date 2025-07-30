# Exercise 15: Map Tuples
# Given a tuple of numbers, create a new tuple where each number is squared.
#
# Given:
#
t = (1, 2, 3, 4)
# Expected Output:
#
# Original tuple: (1, 2, 3, 4)
# Squared tuple:  (1, 4, 9, 16)

print(f"Original tuple: {t}")

squares= []
for i in t:
  squares.append(i ** 2)
squares=tuple(squares)
print(squares)

