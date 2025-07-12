#Exercise 11: Print all prime numbers within a range
start = int(input("enter the Start value"))
end = int(input("enter the end value"))
print(f"Prime numbers between {start} and {end} are:")
for i in range(start,end):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

