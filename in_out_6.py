file=open("test.txt", 'r')

file1=open("new_file.txt",'w')

content = file.readlines()

for i in content:
    if i!="line5\n":
       # print(i)
       file1.write(i)

#print(type(content))
#print(content[:2:1])

file.close()
file1.close()

