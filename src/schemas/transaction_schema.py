from datetime import datetime
from models import Transaction


def parse_transaction_input(data: dict) -> Transaction:
    """
    Convert JSON body into a validated Transaction object.
    Raises ValueError if something is invalid.
    """
    required_fields = ["description", "amount", "category", "type", "date"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    description = str(data["description"])
    amount_raw = data["amount"]
    category = str(data["category"])
    type_str = str(data["type"]).lower()
    date_str = str(data["date"])

    if type_str not in ("income", "expense"):
        raise ValueError("type must be 'income' or 'expense'")

    try:
        amount = float(amount_raw)
    except ValueError:
        raise ValueError("amount must be a number")

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("date must be in YYYY-MM-DD format (YYYY-MM-DD)")

    if not description.strip():
        raise ValueError("description cannot be empty")
    if not category.strip():
        raise ValueError("category cannot be empty")

    return Transaction(
        description=description.strip(),
        amount=amount,
        category=category.strip(),
        type=type_str,
        date=date_obj,
    )
