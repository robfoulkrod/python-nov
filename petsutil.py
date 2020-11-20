
''' petsutil - a collection of utillity fuctions for manipulating
               the pets text file
'''


def get_pets():
    '''
        description
        returns a list of tuples containing owner and pet name
    '''
    pets_path = r"c:\class\pets.txt"
    pets_list = []
    with open(pets_path, "r") as pets_file:
        for line in pets_file:
            owner, pet = line.split(",")
            pet = pet.strip()
            pets_list.append((owner, pet))
    return pets_list


def max():
    return "Best pet name ever!"


def _clear_file():
    '''clears the contents of the pets file'''
    pass  # not actually doing anything


def main():
    # testing code #
    l = get_pets()
    print(l)

    print("*************************")
    print()
    print("__name__", __name__)
    print()
    print("**************************")


if __name__ == "__main__":
    main()