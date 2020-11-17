
# first start by asking for people and pets

db = []

while True:
    name = input('enter your name or "q" for quit ')
    if name == "q": 
        break

    pet_name = input('enter pet name: ')

    age = int(input(f"how old is {pet_name}? "))
    
    row = (name, pet_name, age)
    db.append(row)

# we now have all the data, let's print

for info in db:
    # person_name = pair[0]
    # pets_name = pair[1]

    # _ is uesd as a variable that is needed by the 'compiler', but not by us
    person_name, pets_name, _ = info # unpack the tuple into 3 varaibles

    print(f"{person_name} takes care of {pets_name}")
