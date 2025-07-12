#Exercise 11: Print all prime numbers within a range
start = int(input("enter the Start value"))
end = int(input("enter the end value"))
print(f"Prime numbers between {start} and {end} are:")

def prime_num(start,end):
    res=""
    for i in range(start,end):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            res=res+str(i)+"\n"
    return(res)
print(prime_num(start,end))


