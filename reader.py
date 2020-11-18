


db = []

with open('pets.txt', 'r') as pets_file:
    for line in pets_file:
        owner, pet = line.split(',')
        
        #clean off the space and newline
        pet = pet.strip()

        db.append((owner, pet))

# pets_file is closed when we lose the indentation
print(db)

# copy to output.txt
with open('output.txt', 'w') as output_file:
    for owner, pet in db:
        output_file.write(f"{owner}, {pet}\n")

print("file written")