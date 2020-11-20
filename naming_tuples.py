from collections import namedtuple


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

Pet = namedtuple("Pet", "owner name age")

p1 = Pet("bob", "polly", 3)
