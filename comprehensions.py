
pets = ["grace", "matthew", "floyd", "sammy", "louis", "oso"]

# cased = []
# for pet in pets:
#     cased.append(pet.title())

# we can do the same as above in a comprehension
# title case EVERY pet
cased = [p.title() for p in pets]

# now display
# print(cased)

# title case the 5 character pets
five_letter_pets = [
    p.title()       # select
    for p in pets   # from
    if len(p) == 5  # where 
]

# print(five_letter_pets)


suits = 'Clubs', 'Diamonds', 'Hearts', 'Spades'
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


full_deck = []
for suit in suits:
    for rank in ranks:
        full_deck.append((rank, suit))


print()
# deck = [(rank, suit) for suit in suits for rank in ranks]
# print(deck)


dynamic_deck = ((rank, suit) for suit in suits for rank in ranks)
print(dynamic_deck)

# print()
for c in dynamic_deck:
    print(c)
    if index >= 10: break

# processing the generator a second time
for c in dynamic_deck:
    print(c)
    if index >= 10: break