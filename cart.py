'''
   simple function for our unit testing example
'''


def calculate_discount(shopping_list):

    if len(shopping_list) == 0:
        raise ValueError("Carts cannot be empty wen processing discount")

    discount = 0
    total = 0
    applied_discount = False
    for _, price in shopping_list:
        total += price
    if total >= 100:
        discount = .1
        applied_discount = True
    return applied_discount, discount
