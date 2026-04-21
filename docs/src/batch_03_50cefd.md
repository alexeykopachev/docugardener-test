```markdown
### `process_batch_payment_03_50cefd`
```python
def process_batch_payment_03_50cefd(order_ids: list, unit_amount: float) -> dict:
    """Process a batch of payment orders for slot 03.

    Iterates over the supplied order IDs, applies a 3% batch discount to
    each, and returns an aggregated settlement record for the batch along
    with per-order breakdowns.

    Args:
        order_ids:    List of order identifier strings to process.
        unit_amount:  Base amount per order before discount (must be > 0).

    Returns:
        A dictionary containing the settlement record for the batch, including
        the slot number, number of orders, total net amount, and a list of
        per-order breakdowns. Each order breakdown includes the order ID,
        gross amount, discount, and net amount.

    Raises:
        ValueError: If unit_amount is not positive.

    Examples:
        >>> process_batch_payment_03_50cefd(["ord-123", "ord-456"], 100.0)
        {'slot': 3, 'count': 2, 'total_net': 194.0, 'orders': [{'order_id': 'ord-123', 'gross': 100.0, 'discount': 3.0, 'net': 97.0}, {'order_id': 'ord-456', 'gross': 100.0, 'discount': 3.0, 'net': 97.0}]}
    """
```

Processes a batch of payment orders for slot 03.

This function iterates over the supplied order IDs, applies a 3% batch discount to each order, and returns an aggregated settlement record for the batch along with per-order breakdowns.

**Parameters:**

*   **`order_ids`** (`list`): A list of order identifier strings to process.
*   **`unit_amount`** (`float`): The base amount per order before the discount is applied. This value must be positive.

**Returns:**

*   **`dict`**: A dictionary containing the aggregated settlement record and individual order details.
    *   `slot` (`int`): The slot number (always 3).
    *   `count` (`int`): The total number of orders processed in the batch.
    *   `total_net` (`float`): The sum of net amounts for all orders after discounts.
    *   `orders` (`list`): A list of dictionaries, each representing an individual order's breakdown:
        *   `order_id` (`str`): The identifier of the order.
        *   `gross` (`float`): The original amount of the order before discount.
        *   `discount` (`float`): The calculated discount amount for the order.
        *   `net` (`float`): The final net amount after the discount.

**Raises:**

*   **`ValueError`**: If `unit_amount` is not positive.

**Examples:**

```python
>>> process_batch_payment_03_50cefd(["ord-123", "ord-456"], 100.0)
{'slot': 3, 'count': 2, 'total_net': 194.0, 'orders': [{'order_id': 'ord-123', 'gross': 100.0, 'discount': 3.0, 'net': 97.0}, {'order_id': 'ord-456', 'gross': 100.0, 'discount': 3.0, 'net': 97.0}]}
```
```