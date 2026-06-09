def validate_crypto_response(data):
    """Check if crypto response has required structure"""

    if not isinstance(data, dict):
        return False, "Invalid response format"

    if "quotes" not in data:
        return False, "Missing 'quotes' key"

    if "USD" not in data["quotes"]:
        return False, "Missing 'USD' data"

    return True, "Valid response"