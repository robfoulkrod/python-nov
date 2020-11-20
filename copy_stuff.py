import copy

data = [
    ["red", "blue", "green"],
    [88, 42, 7],
    ["OK", "OH", "MA", "MN", "MI"]
]


# copy_of_data = data[::] # shallow copy
copy_of_data = copy.deepcopy(data)

copy_of_data[0].append("magenta")

print(data)
