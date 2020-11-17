
age_str = input("What is your age? ")
age = int(age_str)

LOTTO_PURCHASER = 18
KNOW_BETTER = 50

if age >= KNOW_BETTER:
    print("You know the odds must be bad to make money")
elif age >= LOTTO_PURCHASER:
    print("You are old enough to buy into the lottery")
    print("Remember a lottery is a tax on the mathamatically challenged")
else:
    print("you are not old enough to collect on lott winnings")
    print("Better have an older friend that you trust, if you win")

print("All done")

pages_str = input("number of pages read")
pages = int(pages_str)

plural = "page" if pages == 1 else "pages"


message = f"You read {pages} {plural}."
print(message)


