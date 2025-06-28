#Exercise 11: Percentage Display
#Ask the user for a numerator and a denominator. Calculate the percentage and 
#display it with two decimal places followed by a percent sign (e.g., 75.50%).


num=int(input("Enter Numerator"))
den=int(input("Enter denominator"))
if(den==0):
    print("denominator cannot be zero")
else:
    per=(num/den)*100
    print("%.2f" % per+"%")
