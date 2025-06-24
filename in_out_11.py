num=int(input("Enter Numerator"))
den=int(input("Enter denominator"))
if(den==0):
    print("denominator cannot be zero")
else:
    per=(num/den)*100
    print("%.2f" % per+"%")
