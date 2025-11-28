from dataclasses import dataclass
from datetime import date


@dataclass
class Transaction:
    description: str
    amount: float
    category: str
    type: str          # "income" or "expense"
    date: date

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "amount": float(self.amount),
            "category": self.category,
            "type": self.type,
            "date": self.date.isoformat(),
        }
