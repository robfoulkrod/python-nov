from collections import defaultdict


def default_next_id_factory():
    last_id = 0

    def increment():
        nonlocal last_id
        last_id += 1
        return last_id
    return increment


populations = defaultdict(default_next_id_factory())
populations2 = defaultdict(default_next_id_factory())

populations["MI"] = 10000000
populations["OH"] = 11689100

print(populations["WI"])
print(populations["MT"])
print(populations["MO"])

print(populations2["WI"])
print(populations2["MT"])
print(populations2["MO"])


print(populations)
print(populations2)

