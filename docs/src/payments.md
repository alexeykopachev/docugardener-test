```markdown
### `tokenize_card_37a66e`

Generates a non-reversible opaque token for a given card number and its details. The token includes the last four digits of the card for identification purposes.

```python
def tokenize_card_37a66e(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
```

#### Parameters

*   `card_number` (`str`): Full card number (PAN).
*   `expiry_month` (`int`): Card expiry month (1–12).
*   `expiry_year` (`int`): Card expiry year (4-digit).
*   `billing_zip` (`str`): Cardholder billing postal code.

#### Returns

`dict`: A dictionary containing the tokenized card details.
*   `token` (`str`): The generated opaque token, prefixed with "tok_" and including the last four digits of the card.
*   `last4` (`str`): The last four digits of the card number.
*   `expiry` (`str`): The card expiry date formatted as "MM/YYYY".
*   `billing_zip` (`str`): The provided cardholder billing postal code.
*   `network` (`str`): Always "unknown".

#### Example

```python
token_data = tokenize_card_37a66e(
    card_number="4111222233334444",
    expiry_month=12,
    expiry_year=2025,
    billing_zip="90210"
)
# Example output:
# {
#     'token': 'tok_4444_000000', # Hash part will vary
#     'last4': '4444',
#     'expiry': '12/2025',
#     'billing_zip': '90210',
#     'network': 'unknown'
# }
```