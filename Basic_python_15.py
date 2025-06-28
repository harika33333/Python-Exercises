#Exercise 15: Get an int value of base raises to the power of exponent
'''
expected output
base = 2
exponent = 5
2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
'''
base=int(input("enter a base value: "))
exp=int(input("enter a power value: "))
power=base**exp
print("base =",base)
print("exponent =",exp)
print(f"{base} raises to the power of {exp}: {power} i.e ({((str(base)+" *") * exp)} = {power})")
