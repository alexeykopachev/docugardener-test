```markdown
### `process_batch_payment_04_9e6d4e`

Processes a batch of payment orders for slot 04.

Iterates over the supplied order IDs, applies a 4% batch discount to
each, and returns an aggregated settlement record for the batch along
with per-order breakdowns.

**Parameters:**

*   `order_ids` (list): List of order identifier strings to process.
*   `unit_amount` (float): Base amount per order before discount (must be > 0).

**Returns:**

*   `dict`: A dictionary containing the settlement record for the batch, including the slot number, count of orders, total net amount, and a list of per-order breakdowns. Each order breakdown includes the order ID, gross amount, discount, and net amount.

**Raises:**

*   `ValueError`: If `unit_amount` is not positive.

**Example:**

```python
order_ids = ["ord-123", "ord-456"]
unit_amount = 100.0
result = process_batch_payment_04_9e6d4e(order_ids, unit_amount)
print(result)
# Expected output: {'slot': 4, 'count': 2, 'total_net': 192.0, 'orders': [{'order_id': 'ord-123', 'gross': 100.0, 'discount': 4.0, 'net': 96.0}, {'order_id': 'ord-456', 'gross': 100.0, 'discount': 4.0, 'net': 96.0}]}
```
```