## Function: `calculate_loyalty_discount_780469`

### Added

A new function `calculate_loyalty_discount_780469` has been added to the `payments` module. This function calculates a loyalty discount multiplier based on the number of previous purchases.

#### Description

Calculates a loyalty discount rate for a customer. The function returns a discount multiplier between 0.0 and 1.0, determined by the number of previous purchases. Customers with more than 10 purchases receive a discount equivalent to the `base_rate`. For customers with 10 or fewer purchases, the discount is a proportional fraction of the `base_rate`.

#### Parameters

*   **`purchases`** (`int`): The number of completed purchases by the customer.
*   **`base_rate`** (`float`): The maximum discount rate to apply, expected to be between 0.0 and 1.0.

#### Returns

*   **`float`**: A discount multiplier between 0.0 and 1.0, rounded to 4 decimal places.

#### Examples

```python
# Customer with 5 purchases, base rate of 0.10 (10%)
discount_rate = calculate_loyalty_discount_780469(purchases=5, base_rate=0.10)
# discount_rate will be 0.05 (5%)

# Customer with 15 purchases, base rate of 0.10 (10%)
discount_rate = calculate_loyalty_discount_780469(purchases=15, base_rate=0.10)
# discount_rate will be 0.10 (10%)

# Customer with 0 purchases
discount_rate = calculate_loyalty_discount_780469(purchases=0, base_rate=0.10)
# discount_rate will be 0.0
```