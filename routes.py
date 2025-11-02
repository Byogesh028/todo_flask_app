from flask import Blueprint, request, jsonify

todo_bp = Blueprint("todo", __name__)

@todo_bp.route("/api", methods=["GET"])
def get_api():
    return jsonify({"message": "Hello from API"})

@todo_bp.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.json
    # Simulate storing in MongoDB
    print(f"Received: {data}")
    return jsonify({"status": "success"})
