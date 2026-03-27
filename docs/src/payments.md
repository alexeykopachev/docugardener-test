```markdown
### capture_payment

```python
def capture_payment(
    transaction_id: str,
    amount: float | None = None,
) -> dict:
    """Capture a previously authorized payment.

    If amount is None, captures the full authorized amount.
    Partial capture is supported by passing a lower amount.
    """
    return {
        "transaction_id": transaction_id,
        "status": "captured",
        "captured_amount": amount,
    }
```

Captures a previously authorized payment.

**Parameters:**

*   `transaction_id` (str): The ID of the transaction to capture.
*   `amount` (float | None, optional): The amount to capture. If `None`, the full authorized amount is captured. Defaults to `None`.

**Returns:**

*   `dict`: A dictionary containing the transaction ID, status, and captured amount.

**Example:**

```python
result = capture_payment(transaction_id="123", amount=50.0)
print(result)
# Expected output: {'transaction_id': '123', 'status': 'captured', 'captured_amount': 50.0}
```

```python
result = capture_payment(transaction_id="456")
print(result)
# Expected output: {'transaction_id': '456', 'status': 'captured', 'captured_amount': None}
```
