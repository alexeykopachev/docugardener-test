```markdown
### verify_webhook_signature

```python
def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool
```

Verify an incoming payment webhook signature.

Compares the provided HMAC-SHA256 signature against a locally
computed digest using the shared secret. Returns True if valid.

**Parameters:**

*   `payload` (bytes): The raw webhook request body as bytes.
*   `signature` (str): The signature provided in the `X-Signature` header.
*   `secret` (str): Your shared secret key.

**Returns:**

*   `bool`: True if the signature is valid, False otherwise.

**Example:**

```python
payload = b'{"event": "payment.received", "data": {...}}'
signature = "sha256=..."
secret = "your_secret"

if verify_webhook_signature(payload, signature, secret):
    print("Valid signature!")
else:
    print("Invalid signature!")
```
