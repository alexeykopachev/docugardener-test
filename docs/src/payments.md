```markdown
### `estimate_fees`

```python
def estimate_fees(
    amount: float,
    currency: str = "USD",
    payment_method: str = "card",
) -> dict:
```

Estimate processing fees for a given payment amount and method.

Returns a breakdown of platform fee, network fee, and total charge.
Supported `payment_method` values: `card`, `bank_transfer`, `wallet`.

**Parameters:**

*   `amount` (float): The payment amount.
*   `currency` (str, optional): The currency code (e.g., "USD"). Defaults to "USD".
*   `payment_method` (str, optional): The payment method. Defaults to "card".

**Returns:**

*   dict: A dictionary containing the amount, currency, payment method, platform fee, network fee, and total fee.

**Example:**

```python
>>> estimate_fees(amount=100.00, currency="USD", payment_method="card")
{'amount': 100.0, 'currency': 'USD', 'payment_method': 'card', 'platform_fee': 1.4, 'network_fee': 0.6, 'total_fee': 2.0}
```
```