def cart_count(items: list[tuple[str, int]]) -> int:
    """Number of units in the cart (sum of quantities)."""
    n = 0
    for _, qty in items:
        n += qty
    return n


def cart_weight(items: list[tuple[str, int]], grams: dict[str, int]) -> int:
    """Total weight of the cart in grams: quantity times the item's weight, summed.

    Items missing from `grams` raise KeyError.
    """
    return sum(qty * grams[sku] for sku, qty in items)
