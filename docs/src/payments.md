```markdown
### `cancel_payment`

```python
def cancel_payment(transaction_id: str, reason: str = "customer_request", notify_customer: bool = True, idempotency_key: str | None = None) -> dict
```

Cancels a pending payment before it is captured.

Only payments in `'pending'` or `'authorized'` state can be cancelled. Captured payments must use `refund_payment` instead.

**Parameters:**

-   `transaction_id` (str): The ID of the transaction to cancel.
-   `reason` (str, optional): The reason for the cancellation. Defaults to `"customer_request"`.
-   `notify_customer` (bool, optional): Whether to notify the customer about the cancellation. Defaults to `True`.
-   `idempotency_key` (str | None, optional):  An idempotency key to prevent accidental duplicate cancellations. Defaults to `None`.

**Returns:**

`dict`: A dictionary containing the cancellation details, including the transaction ID, status (`"cancelled"`), reason, and customer notification status.

**Example:**

```python
result = cancel_payment(
    transaction_id="transaction123", reason="incorrect_amount", notify_customer=False
)
print(result)
# Expected output: {'transaction_id': 'transaction123', 'status': 'cancelled', 'reason': 'incorrect_amount', 'customer_notified': False}
```
```
