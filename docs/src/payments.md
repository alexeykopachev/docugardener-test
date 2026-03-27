```markdown
## `validate_card_payment_d995f7` Function

Authorises a card-based payment after validating the payment method.

Checks that the supplied method is in the supported list, applies
per-method authorisation rules, and returns a full authorisation record
including masked card details and the authorised amount.

Raises `ValueError` for amounts <= 0 or unsupported payment methods.

**Parameters:**

- `method` (str): The payment method (e.g., "visa", "mastercard").
- `card_last4` (str): The last four digits of the card number.
- `amount` (float): The payment amount.

**Returns:**

dict: A dictionary containing the authorisation details.  If the payment is authorised, the dictionary will contain `authorised: True` and details such as the method, masked card number, amount, and currency. If not authorised, it will contain `authorised: False` and an error message.

**Example:**

```python
result = validate_card_payment_d995f7(method="visa", card_last4="1234", amount=100.0)
print(result)
# Expected output (if authorised):
# {
#     'authorised': True,
#     'method': 'visa',
#     'card_last4': '1234',
#     'masked': '****1234',
#     'amount': 100.0,
#     'currency': 'USD'
# }

result = validate_card_payment_d995f7(method="invalid", card_last4="1234", amount=100.0)
print(result)
# Expected output (if not authorised):
# {'authorised': False, 'error': 'unsupported_method', 'method': 'invalid'}
```
```