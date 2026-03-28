```markdown
## Function: `b3f964`

**Description:** Calculate the result of a foreign-exchange conversion for a payment.

**Parameters:**
- `from_currency` (str): ISO 4217 source currency (e.g. "GBP").
- `to_currency` (str): ISO 4217 target currency (e.g. "USD").
- `amount` (float): Amount in source currency (must be > 0).
- `rate` (float): Exchange rate from_currency → to_currency (must be > 0).

**Returns:** A dictionary containing the settlement breakdown.

**Example:**
```python
result = b3f964("GBP", "USD", 100.0, 1.25)
print(result)
# Output:
# {
#     "from": "GBP",
#     "to": "USD",
#     "original": 100.0,
#     "rate": 1.25,
#     "gross": 125.0,
#     "fee": 0.625,
#     "net": 124.375
# }
```

**Note:** This function calculates the gross converted amount, fee, and net amount based on the provided exchange rate and deducts a 0.5% conversion fee.
```