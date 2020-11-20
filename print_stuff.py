from collections import namedtuple
from pprint import pprint

pets_list = [
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
    ("a", "pet1", 2),
]

data = [
    ["red", "blue", "green"],
    [88, 42, 7],
    ["OK", "OH", "MA", "MN", "MI"]
]

populations = {}

populations["MI"] = 10000000
populations["OH"] = 11689100

my_data = [pets_list, data, populations]

pprint(my_data)

pprint(my_data, depth=2)
