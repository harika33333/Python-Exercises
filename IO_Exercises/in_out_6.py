#Exercise 6: Write all content of a file into a new file by skipping line number 5

with open("test.txt", 'r') as file:
    content = file.readlines()
with open("new_file.txt",'w') as file1:
    for i in content:
        if i!=content[4]:
            #print(i) 
            file1.write(i)



