
# print number 1 thru 10
# for i = 1 to 10
# for( int i = 1; 1 <= 10; i++){ ... }

# n = 1
# while n <= 10:
#     print(n)
#     n += 1

for n in range(1,11):
    print(n)

print("-" * 10)

pets = ["grace", "matthew", "floyd", "sammy", "louis", "oso"]
for index, name in enumerate(pets, 1):
    print(index, name)


cookies = ["chocolate chip"] * 12
more_cookies = cookies + ["oatmeal raisin"]

print(more_cookies)