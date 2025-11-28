from typing import Optional, List, Dict
from flask import Blueprint, request, jsonify
from bson import ObjectId

from db import transactions_collection
from schemas.transaction_schema import parse_transaction_input

transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


def _serialize_transaction(doc: dict) -> dict:
    return {
        "id": str(doc["_id"]),
        "description": doc.get("description"),
        "amount": doc.get("amount"),
        "category": doc.get("category"),
        "type": doc.get("type"),
        "date": doc.get("date"),
    }


@transactions_bp.get("")
def list_transactions():
    """GET /transactions?category=...&type=..."""
    category: Optional[str] = request.args.get("category")
    type_: Optional[str] = request.args.get("type")

    query: dict = {}
    if category:
        query["category"] = category
    if type_:
        query["type"] = type_

    results: List[Dict] = []
    for doc in transactions_collection.find(query).sort("date", -1):
        results.append(_serialize_transaction(doc))

    return jsonify(results)


@transactions_bp.post("")
def create_transaction():
    """POST /transactions  with JSON body."""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON body"}), 400

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    try:
        tx = parse_transaction_input(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    to_insert = tx.to_dict()
    result = transactions_collection.insert_one(to_insert)
    created = transactions_collection.find_one({"_id": result.inserted_id})

    return jsonify(_serialize_transaction(created)), 201


@transactions_bp.delete("/<id_str>")
def delete_transaction(id_str: str):
    """DELETE /transactions/<id>"""
    if not ObjectId.is_valid(id_str):
        return jsonify({"error": "Invalid ID format"}), 400

    result = transactions_collection.delete_one({"_id": ObjectId(id_str)})
    if result.deleted_count == 0:
        return jsonify({"error": "Transaction not found"}), 404

    return jsonify({"message": "Transaction deleted successfully"})
