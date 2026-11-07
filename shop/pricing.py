def apply_discount(price: float, pct: float) -> float:
    """Price after a percentage discount.

    pct is a percentage (10 means 10% off). The result is never below zero,
    so a discount of 100% or more makes the item free, not negative.
    """
    return max(0.0, price * (1 - pct / 100))


def bulk_price(prices: list[float], pct: float) -> float:
    """Total of apply_discount over every price, rounded to cents."""
    return round(sum(apply_discount(p, pct) for p in prices), 2)
