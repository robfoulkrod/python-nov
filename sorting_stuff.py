
def clean_up(pet):
    return pet.lower()


def special_sort(pet):
    return len(pet), pet.lower()


def pets_sort(pet_info):
    return pet_info[1], pet_info[0].lower()


pets = [("grace", 5), ("Matthew", 7),
        ("floyd", 3), ("sammy", 5), ("louis", 3), ("oso", 2), ("butthead", 2)]


sorted_pets = sorted(pets, key=pets_sort)

# the lowcased version. but this time as a lambda
# sorted_pets = sorted(pets, key=lambda pet: pet.lower())


print(sorted_pets)

# A -> 65
# B -> 66
# ...
# a -> 97
# b -> 98


def mary(a, b): return a + b


mary(12, 13)
