from shop.pricing import apply_discount, bulk_price


def test_basic_discount():
    assert apply_discount(100, 10) == 90


def test_discount_never_negative():
    assert apply_discount(10, 150) == 0.0


def test_bulk():
    assert bulk_price([10, 20], 50) == 15.0


def test_discount_rounding_close():
    assert abs(apply_discount(19.99, 15) - 16.9915) < 1e-9
