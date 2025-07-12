#Exercise 1: Print first 10 natural numbers using while loop
def while_loop(i):
    s=""
    n=1
    while(n<(i+1)):
        s=s+str(n)+"\n"
        n=n+1
    return(s)
print(while_loop(10))


