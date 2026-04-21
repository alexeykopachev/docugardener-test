```markdown
### `apply_surcharge_3ffe5f`
Applies a percentage-based surcharge to a payment transaction.

Calculates the surcharge value, validates inputs, and returns a breakdown
including the original amount, surcharge, total charged, and applied currency.
Surcharge percentage must be between 0 and 50 (exclusive).

Args:
    amount (float): Base transaction amount (must be > 0).
    surcharge_pct (float): Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
    currency (str, optional): ISO 4217 currency code. Defaults to "USD".

Returns:
    dict: A dictionary containing the original amount, surcharge amount,
          total amount charged, and the currency.

Raises:
    ValueError: If amount is not positive or if surcharge_pct is not
                between 0 and 50.

Example:
    >>> apply_surcharge_3ffe5f(100.0, 2.5)
    {'original': 100.0, 'surcharge': 2.5, 'total': 102.5, 'currency': 'USD', 'rate_applied': 2.5}

    >>> apply_surcharge_3ffe5f(50.0, 10.0, "EUR")
    {'original': 50.0, 'surcharge': 5.0, 'total': 55.0, 'currency': 'EUR', 'rate_applied': 10.0}
```