#Exercise 12: Calculate income tax
'''Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20'''

'''
Expected Output:

For example, suppose the income is 45000, and the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000
''' 

inc=int(input("Enter the income of the person: "))
if ( inc > 10000 ):
    income=inc-10000
    #print(inc)
if(inc > 10000) and (inc < 20000):
    tax_pay = income * 0.10
    print(tax_pay)
elif(inc>20000):
    #print(inc)
    slab_1=income-10000
    tax_pay=(slab_1*0.20)+(10000*0.10)
    print(tax_pay)
else:
    print(0)

