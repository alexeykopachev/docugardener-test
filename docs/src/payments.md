```markdown
### `calculate_fx_conversion_fd90bc`
Calculates the result of a foreign-exchange conversion for a payment.

Applies the provided exchange rate to the source amount, deducts a
0.5% conversion fee, and returns a full settlement breakdown including
gross converted amount, fee, and net amount.

**Parameters:**

*   `from_currency` (str): ISO 4217 source currency (e.g. "GBP").
*   `to_currency` (str):   ISO 4217 target currency (e.g. "USD").
*   `amount` (float):        Amount in source currency (must be > 0).
*   `rate` (float):          Exchange rate from_currency → to_currency (must be > 0).

**Returns:**

*   `dict`: A dictionary containing the settlement breakdown, including:
    *   `from`: The source currency.
    *   `to`: The target currency.
    *   `original`: The original amount in the source currency.
    *   `rate`: The exchange rate used.
    *   `gross`: The converted amount before fees.
    *   `fee`: The calculated conversion fee (0.5% of gross).
    *   `net`: The final amount after deducting the fee.

**Raises:**

*   `ValueError`: If `amount` or `rate` are not positive.

**Example:**

```python
from_currency = "GBP"
to_currency = "USD"
amount = 100.0
rate = 1.25
result = calculate_fx_conversion_fd90bc(from_currency, to_currency, amount, rate)
print(result)
# Expected output: {'from': 'GBP', 'to': 'USD', 'original': 100.0, 'rate': 1.25, 'gross': 125.0, 'fee': 0.62, 'net': 124.38}
```
```