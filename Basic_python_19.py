#Exercise: 19: Print Alternate Prime Numbers till 20
'''expected output
All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19

Alternate prime numbers from 1 to 20:
2, 5, 11, 17
'''

prime_num= []

for i in range(2,21):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_num.append(i)
print(prime_num)
prime_num=prime_num[::2]
print(prime_num)
d=""
for i in prime_num:
    d=d+str(i)+","
print(d[0:len(d)-1])
