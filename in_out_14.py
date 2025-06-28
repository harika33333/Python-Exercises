#exercise 14: 
# You have two lists: names = ["Alice", "Bob", "Charlie"] and s
# scores = [85, 92, 78]. Print these lists as a simple table with columns “Name” and “Score”.
# Name       Score
# ---------------
# Alice      85   
# Bob        92   
# Charlie    78
names = ["Alice", "Bob", "Charlie"] 
a=max(names, key=len) 
scores = [85, 92, 78]
print(f"Names {"scores":>10}")
print("-"*18)
c=0
char_len=len(a)
for i in names:
    if len(i)<=char_len:
        diff=char_len-len(i)
        print(i+(" "*diff)+"    "+str(scores[c]))
        c=c+1
