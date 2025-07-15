# Exercise 10: Call Function using both positional and keyword arguments
# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet.
# Call this function using both positional and keyword arguments.

def describe_pet(animal_type,pet_name):
    s=f"My name is {pet_name} and i am a {animal_type}"
    return s
#Using Positional args
print(describe_pet("cat","Billi"))

#Using Keyword args
print(describe_pet(pet_name="Romeo",animal_type="dog"))

