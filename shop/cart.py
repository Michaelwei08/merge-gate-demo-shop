def cart_count(items: list[tuple[str, int]]) -> int:
    """Number of units in the cart (sum of quantities)."""
    return sum(qty for _, qty in items)
