#Create a simple interactive menu with options like “1. Say Hello”,
# “2. Calculate Square”, “3. Exit”. Based on the user’s input,
# perform the corresponding action
print("Haari MENU")
print(" 1. say Haari is Bestttoooo \n 2. Calculate Square \n 3. Exit")
n=int(input("please choose a number between 1-3"))

if(n==1):
    print("haari is besttooooo")
elif(n==2):
    a=int(input("please enter the number you want calculate the square for:"))
    print(a**2)
elif(n==3):
    pass
else:
    print("arey yedhava Cheppa ga 1-3 lopala ae choose chesko ani,malli run kotti correct num eyyi")
