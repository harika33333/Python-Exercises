#Write a program to check if the given file is empty or not

with open("test1.txt",'r') as file:
    contents=file.read()
    if contents:
        print("file is not empty")
    else:
        print("file is Empty")


