inc=1000
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

