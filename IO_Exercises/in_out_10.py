#exercise 10: Read Line Number 4 from File
with open("test.txt",'r') as file:
    content=file.readlines()
    print(content[3])

