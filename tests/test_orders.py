import pytest

from shop.orders import order_total


def test_total():
    assert order_total([(2.5, 2), (1.0, 3)]) == 8.0


def test_rejects_zero_quantity():
    with pytest.raises(ValueError):
        order_total([(1.0, 0)])
