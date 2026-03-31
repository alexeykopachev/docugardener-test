### `login(user, password, mfa_token=None, provider='local')`

Authenticate a user with optional Multi-Factor Authentication (MFA) and by specifying an SSO provider.

#### Parameters

*   **`user`** (`str`): The username for authentication. For the 'local' provider, authentication succeeds only if this is 'admin'.
*   **`password`** (`str`): The user's password. *Note: For the 'local' provider, this parameter is currently accepted but not used in the authentication logic.*
*   **`mfa_token`** (`str`, optional): An MFA token required for certain authentication providers. Defaults to `None`. For the 'local' provider, authentication succeeds only if this is not `None`.
*   **`provider`** (`str`, optional): The authentication provider to use. Defaults to `'local'`.

#### Returns

*   **`bool`**: `True` if authentication is successful, `False` otherwise.

#### Details

The `login` function now supports different authentication providers and optional MFA.

*   **Local Provider (`provider='local'`)**:
    *   Authentication succeeds if `user` is `'admin'` AND `mfa_token` is provided (i.e., not `None`).
    *   The `password` parameter is accepted but does not influence the authentication outcome for the 'local' provider.
*   **Other Providers**:
    *   For any `provider` value other than `'local'`, the function currently always returns `False`.

#### Examples

```python
# Successful local login with MFA
login('admin', 'any_password', mfa_token='123456')
# Expected: True

# Failed local login: incorrect user
login('guest', 'any_password', mfa_token='123456')
# Expected: False

# Failed local login: missing MFA token
login('admin', 'any_password')
# Expected: False

# Failed local login: missing MFA token (explicitly None)
login('admin', 'any_password', mfa_token=None)
# Expected: False

# Failed login with an unsupported provider
login('user', 'password', provider='sso_provider')
# Expected: False
```