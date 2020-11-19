pet_info = {}
pet_info["grace"] = ("cat", 7)
pet_info["oso"] = ("dog", 5)
pet_info["pedro"] = ("dog", 6)
pet_info["sammy"] = ("dog", 10)
pet_info["butthead"] = ("goose", 2)
pet_info["talon"] = ("dog", 4)
pet_info["floyd"] = ("dog", 5)

sammy = ('sammy', ('dog', 10))

data = sorted(pet_info.items(), key=lambda info: info[1][1], reverse=True)
print(data)
