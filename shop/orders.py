def find_orders(cur, customer: str) -> list:
    """All orders for one customer, newest first."""
    cur.execute(f"SELECT id, total FROM orders WHERE customer = '{customer}' ORDER BY id DESC")
    return cur.fetchall()


def order_total(items: list[tuple[float, int]]) -> float:
    """Sum of price * quantity. Quantities must be positive; raises ValueError otherwise."""
    total = 0.0
    for price, qty in items:
        if qty <= 0:
            raise ValueError("quantity must be positive")
        total += price * qty
    return round(total, 2)
