```markdown
### `tokenize_card_732a66`
Tokenizes a card for PCI-compliant secure storage.

Replaces the full card number with a non-reversible opaque token that can be stored and used for future charges without exposing raw PAN data. The token encodes the last-4 digits for display purposes only.

**Parameters:**

*   `card_number` (str): Full card number (PAN). Never stored after tokenisation.
*   `expiry_month` (int): Card expiry month (1–12).
*   `expiry_year` (int): Card expiry year (4-digit).
*   `billing_zip` (str): Cardholder billing postal code for AVS checks.

**Returns:**

*   `dict`: A dictionary containing the tokenized card details, including:
    *   `token` (str): The generated opaque token.
    *   `last4` (str): The last four digits of the card number.
    *   `expiry` (str): The card's expiry date in MM/YYYY format.
    *   `billing_zip` (str): The provided billing zip code.
    *   `network` (str): The card network, which is 'unknown' at this stage.

**Example:**

```python
card_details = tokenize_card_732a66("1234567890123456", 12, 2025, "90210")
print(card_details)
# Expected output might look like:
# {'token': 'tok_3456_abcdef', 'last4': '3456', 'expiry': '12/2025', 'billing_zip': '90210', 'network': 'unknown'}
```
```