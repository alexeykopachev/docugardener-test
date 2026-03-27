```markdown
### `convert_currency`

```python
def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
) -> dict:
    """Convert a payment amount between currencies.

    Returns the original amount, the currencies, a converted amount equal to the original, and an exchange rate of 1.0.
    """
    return {
        "original_amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "converted_amount": amount,
        "exchange_rate": 1.0,
    }
```

This function simulates a currency conversion. It takes an amount and two currency codes as input, and returns a dictionary containing the original amount, the input currencies, a converted amount (equal to the original amount), and an exchange rate of 1.0.

**Parameters:**

*   `amount` (float): The amount to convert.
*   `from_currency` (str): The currency to convert from.
*   `to_currency` (str): The currency to convert to.

**Returns:**

*   `dict`: A dictionary containing the original amount, the input currencies, a converted amount (equal to the original amount), and an exchange rate of 1.0.

**Example:**

```python
result = convert_currency(100.0, "USD", "EUR")
print(result)
# Expected output: {'original_amount': 100.0, 'from_currency': 'USD', 'to_currency': 'EUR', 'converted_amount': 100.0, 'exchange_rate': 1.0}
```
