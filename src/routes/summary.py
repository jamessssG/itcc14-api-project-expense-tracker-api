from flask import Blueprint, jsonify
from db import transactions_collection

summary_bp = Blueprint("summary", __name__, url_prefix="/summary")


@summary_bp.get("")
def get_summary():
    """GET /summary -> total_income, total_expense, balance."""
    total_income = 0.0
    total_expense = 0.0

    for doc in transactions_collection.find():
        amount = float(doc.get("amount", 0))
        tx_type = doc.get("type")

        if tx_type == "income":
            total_income += amount
        elif tx_type == "expense":
            total_expense += amount

    balance = total_income - total_expense

    return jsonify(
        {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
        }
    )
