```markdown
```

### `validate_card_payment_3b9563`

Authorise a card-based payment after validating the payment method.

Checks that the supplied method is in the supported list and returns a full authorisation record including masked card details and the authorised amount.

Raises `ValueError` for amounts less than or equal to 0. Returns a dictionary with `authorised: False` for unsupported payment methods.

**Parameters:**

*   `method` (str): The payment method (e.g., "visa", "mastercard").
*   `card_last4` (str): The last four digits of the card number.
*   `amount` (float): The payment amount.

**Returns:**

dict: A dictionary containing the authorisation details.  If the payment is authorised, it includes `authorised: True`, the payment `method`, masked card details (`masked`), the `amount`, and `currency`. If not authorised, it includes `authorised: False` and an `error` message.

**Raises:**

*   `ValueError`: if `amount` is less than or equal to 0.

**Examples:**

*   **Successful authorisation:**

    ```python
    result = validate_card_payment_3b9563(method="visa", card_last4="1234", amount=100.0)
    print(result)
    # Expected output:
    # {
    #     'authorised': True,
    #     'method': 'visa',
    #     'card_last4': '1234',
    #     'masked': '****1234',
    #     'amount': 100.0,
    #     'currency': 'USD'
    # }
    ```

*   **Unsuccessful authorisation (unsupported method):**

    ```python
    result = validate_card_payment_3b9563(method="paypal", card_last4="1234", amount=100.0)
    print(result)
    # Expected output:
    # {'authorised': False, 'error': 'unsupported_method', 'method': 'paypal'}
    ```
```