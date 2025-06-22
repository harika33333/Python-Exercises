# Write a program to use the string.format() method to format the following three variables
# according to the expected output.
totalMoney = 1000
quantity = 3
price = 450

# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

print(f"I have {totalMoney} dollars so I can buy {quantity} football for {"%.2f"% price} dollars.")
