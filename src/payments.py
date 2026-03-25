def init_payment(amount: float, currency: str = "USD") -> dict:
    """Initiate a payment transaction."""
    return {"transaction_id": "txn_123", "status": "pending", "currency": currency}


def refund_payment(transaction_id: str, reason: str = "") -> dict:
    """Refund a previously initiated payment."""
    return {"transaction_id": transaction_id, "status": "refunded", "reason": reason}
