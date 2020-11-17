animal = input("what kind of pet do you want? ")
name = input("what would you name this pet? ")

print("POOF!")
# the f tells python this is a FORMATING string
# auto add {variables} into the string
print(f"and now {name} is your new {animal}.")

# alternate
print("and now " + name + " is your new " + animal +".")
