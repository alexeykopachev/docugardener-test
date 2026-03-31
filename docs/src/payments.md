### `c9(method: str, card_last4: str, amount: float) -> dict`

**Description:**
Authorises a card-based payment after validating the payment method. The function checks if the provided payment method is among the supported types and if the payment amount is positive. If these conditions are met, it returns a successful authorisation record. Otherwise, it indicates an error, either by returning an error object for unsupported methods or raising an exception for invalid amounts.

**Parameters:**
*   `method` (`str`): The payment method to be used (e.g., "visa", "mastercard", "amex", "discover", "unionpay"). Case-insensitive.
*   `card_last4` (`str`): The last four digits of the card associated with the payment.
*   `amount` (`float`): The payment amount. Must be a positive value.

**Returns:**
*   `dict`: A dictionary containing the authorisation result.
    *   If the payment is successfully authorised:
        ```json
        {
            "authorised": true,
            "method": "visa",
            "card_last4": "1234",
            "masked": "****1234",
            "amount": 100.00,
            "currency": "USD"
        }
        ```
    *   If the `method` is not supported:
        ```json
        {
            "authorised": false,
            "error": "unsupported_method",
            "method": "jcb"
        }
        ```

**Raises:**
*   `ValueError`: If `amount` is less than or equal to 0.

**Example:**
```python
# Successful authorisation
result = c9("visa", "1234", 100.00)
print(result)
# Expected: {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

# Unsupported payment method
result = c9("jcb", "5678", 50.00)
print(result)
# Expected: {'authorised': False, 'error': 'unsupported_method', 'method': 'jcb'}

# Invalid amount
try:
    c9("mastercard", "9012", 0.00)
except ValueError as e:
    print(e)
# Expected: amount must be positive, got 0.0
```