```markdown
### New Function: `tokenize_card_87458c`

A new function `tokenize_card_87458c` has been added to the `src/payments.py` file.

#### `tokenize_card_87458c`

```python
def tokenize_card_87458c(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
```

This function tokenizes a credit card for secure, PCI-compliant storage. It replaces the full card number with a non-reversible opaque token. The token includes the last four digits of the card number for display purposes.

**Args:**

*   `card_number` (str): The full card number (Primary Account Number - PAN). This value is not stored after tokenization.
*   `expiry_month` (int): The card's expiry month, represented as an integer from 1 to 12.
*   `expiry_year` (int): The card's expiry year, represented as a 4-digit integer.
*   `billing_zip` (str): The cardholder's billing postal code, used for Address Verification System (AVS) checks.

**Returns:**

*   A dictionary containing the following keys:
    *   `token` (str): The generated opaque token.
    *   `last4` (str): The last four digits of the card number.
    *   `expiry` (str): The expiry date in "MM/YYYY" format.
    *   `billing_zip` (str): The provided billing zip code.
    *   `network` (str): The card network, which is initially set to "unknown" and resolved during authorization.

**Example:**

```python
token_data = tokenize_card_87458c("1234567890123456", 12, 2025, "90210")
print(token_data)
# Expected output (token will vary):
# {'token': 'tok_3456_abcdef', 'last4': '3456', 'expiry': '12/2025', 'billing_zip': '90210', 'network': 'unknown'}
```
```