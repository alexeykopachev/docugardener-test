```markdown
### `calculate_fx_conversion_572f33`
Calculate the result of a foreign-exchange conversion for a payment.

Applies the provided exchange rate to the source amount, deducts a
0.5% conversion fee, and returns a full settlement breakdown including
gross converted amount, fee, and net amount.

**Parameters:**

*   `from_currency` (str): ISO 4217 source currency (e.g. "GBP").
*   `to_currency` (str): ISO 4217 target currency (e.g. "USD").
*   `amount` (float): Amount in source currency (must be > 0).
*   `rate` (float): Exchange rate from_currency → to_currency (must be > 0).

**Returns:**

*   `dict`: A dictionary containing the FX conversion breakdown.
    *   `from` (str): The source currency.
    *   `to` (str): The target currency.
    *   `original` (float): The original amount in the source currency.
    *   `rate` (float): The exchange rate used.
    *   `gross` (float): The converted amount before fees.
    *   `fee` (float): The calculated 0.5% conversion fee.
    *   `net` (float): The final amount after deducting the fee.

**Example:**

```python
from_currency = "GBP"
to_currency = "USD"
amount = 100.0
rate = 1.25
result = calculate_fx_conversion_572f33(from_currency, to_currency, amount, rate)
print(result)
# Expected output: {'from': 'GBP', 'to': 'USD', 'original': 100.0, 'rate': 1.25, 'gross': 125.0, 'fee': 0.62, 'net': 124.38}
```
```