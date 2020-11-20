import pytest
from cart import calculate_discount


def test_no_discount_100():
    cart = [('item', 50)]
    applied, _ = calculate_discount(cart)
    assert not applied


def test_discount_at_100():
    cart = [('item', 50), ('item', 50)]
    applied, _ = calculate_discount(cart)
    assert applied


def test_empty_carts_raise_valueError():

    with pytest.raises(ValueError):
        cart = []
        calculate_discount(cart)
