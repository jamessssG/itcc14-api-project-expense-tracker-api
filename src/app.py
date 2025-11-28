from flask import Flask, jsonify
from flask_cors import CORS

from routes.transactions import transactions_bp
from routes.summary import summary_bp


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(transactions_bp)
    app.register_blueprint(summary_bp)

    @app.get("/")
    def root():
        return jsonify({"message": "Expense Tracker API (MongoDB + Flask) is running"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
