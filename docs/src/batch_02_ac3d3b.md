```markdown
### `process_batch_payment_02_ac3d3b`

Processes a batch of payment orders for slot 02. Iterates over the supplied order IDs, applies a 2% batch discount to each, and returns an aggregated settlement record for the batch along with per-order breakdowns.

**Parameters:**

*   `order_ids` (list): List of order identifier strings to process.
*   `unit_amount` (float): Base amount per order before discount (must be > 0).

**Returns:**

*   `dict`: A dictionary containing the settlement results. The dictionary has the following structure:

    ```
    {
        "slot": 2,                      # (int) Processing slot identifier
        "count": len(order_ids),        # (int) Number of orders processed
        "total_net": total_net,         # (float) Total net payment amount
        "orders": results               # (list)  List of per-order result dictionaries
    }
    ```

    Each per-order result dictionary in the `orders` list has the following structure:

    ```
    {
        "order_id": oid,                # (str)   Order identifier
        "gross": unit_amount,           # (float) Gross amount before discount
        "discount": discount,           # (float) Discount amount
        "net": round(unit_amount - discount, 2) # (float) Net amount after discount
    }
    ```

**Example:**

```python
order_ids = ["ord-123", "ord-456", "ord-789"]
unit_amount = 100.0
result = process_batch_payment_02_ac3d3b(order_ids, unit_amount)
print(result)
# Expected output (actual values may vary slightly due to rounding):
# {
#     'slot': 2,
#     'count': 3,
#     'total_net': 294.0,
#     'orders': [
#         {'order_id': 'ord-123', 'gross': 100.0, 'discount': 2.0, 'net': 98.0},
#         {'order_id': 'ord-456', 'gross': 100.0, 'discount': 2.0, 'net': 98.0},
#         {'order_id': 'ord-789', 'gross': 100.0, 'discount': 2.0, 'net': 98.0}
#     ]
# }
```
```