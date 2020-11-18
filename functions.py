
def create_cart():
    shopping_list = []
    while True:
        item = input('What did you purchase (q to quit) ')
        if item.lower() == 'q':
            break
        price = input('price of ' + item + ' ')
        price = float(price)
        shopping_list.append((item, price))
    return shopping_list


def calculate_discount(shopping_list):
    discount = 0
    total = 0
    applied_discount = False
    for _, price in shopping_list:
        total += price
    if total >= 100:
        discount = .1
        applied_discount = True
    return applied_discount, discount


def print_list(shopping_list, discount_percentage):
    total = 0
    for item, price in shopping_list:
        print(item, price)
        total += price

    print('Before Discount', total)
    discounted_amount = price * discount_percentage
    print('Discount', discounted_amount)
    print('Final', total - discounted_amount)


def main():
    shopping_list = create_cart()
    applied_discount, discount_percent = calculate_discount(shopping_list)
    print_list(shopping_list, discount_percent)


main()
