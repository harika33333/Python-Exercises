# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Expected Outcome:
# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]

def lis_rev(l1,i):

    ch=l1[i:i+3]
    rev_lis=ch[::-1]
    return ch,rev_lis
c=1   
for i in range(0,len(sample_list),3):
    
    ch,rev_lis=lis_rev(sample_list,i) 
    print(f"chunk {c} {ch}")
    print("After reversing it",rev_lis)
    c=c+1
    






