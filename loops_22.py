# Exercise 22: Find largest and smallest digit in a number
# Largest digit in 9876543210: 9
# Smallest digit in 987654321: 1
#
# Largest digit in -5082: 8
# Smallest digit in -5082: 0

n=int(input("Enter a number:"))
num=abs(n)
max=0
min=9
while(num)>0:
    rem=num%10
    if rem>max:
        max=rem
    if rem<min:
        min=rem
    num=num//10
print(f"Largest digit in n: {max} \nSmallest digit in n: {min}")


