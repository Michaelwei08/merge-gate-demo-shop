from shop.pricing import apply_discount, bulk_price


def test_basic_discount():
    assert apply_discount(100, 10) == 90


def test_bulk():
    assert bulk_price([10, 20], 50) == 15.0
