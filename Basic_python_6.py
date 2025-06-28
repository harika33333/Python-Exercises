#Exercise 6: Display numbers divisible by 5
'''Expected output
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55'''

num=[10, 20, 33, 46, 55]
print(f"Given list is {num}")
print("Divisible by 5")
for i in num:
    if (i%5==0):
        print(i)
