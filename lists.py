
names = ['alex', 'anne', 'arul', 'christine', 'gail']

names.append('george')

first_name = names[0]

print(first_name, ' is the first name of ', names)

del names[2]
print("After arul left", names)

# remove method is by value
names.remove('christine')
print("After christine left", names)

names.insert(2, 'glen')

print("adding glen to index 2", names)

# can it also be a stack?
names.append('greg')
names.append('gregory')

print("with the gregs", names)

g1 = names.pop()
g2 = names.pop()
print("after 2 pops", names, g1, g2)

long_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

print(long_list)
print(long_list[3])
print(long_list[3:10])
print(long_list[5:7])
print(long_list[20:])
print('exclude outside', long_list[1:-1])
print('alternate letters', long_list[1::2])
print()
print("alternate letters in upper case")
for letter in long_list[::2]:
    print(letter.upper())