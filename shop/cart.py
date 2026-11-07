def cart_count(items: list[tuple[str, int]]) -> int:
    """Number of units in the cart (sum of quantities)."""
    n = 0
    for _, qty in items:
        n += qty
    return n
