import os
import subprocess

# Create a new directory for the project
project_name = 'todo_flask_app'
if not os.path.exists(project_name):
    os.makedirs(project_name)

# Change to project directory
os.chdir(project_name)

# Initialize git repository
subprocess.run(['git', 'init'])

# Create a basic Flask app structure
os.makedirs('app', exist_ok=True)
with open('app/__init__.py', 'w') as f:
    f.write('from flask import Flask\n\ndef create_app():\n    app = Flask(__name__)\n    return app\n')

with open('app/routes.py', 'w') as f:
    f.write('from flask import Blueprint, request, jsonify\n\ntodo_bp = Blueprint("todo", __name__)\n\n@todo_bp.route("/api", methods=["GET"])
def get_api():\n    return jsonify({"message": "Hello from API"})\n\n@todo_bp.route("/submittodoitem", methods=["POST"])
def submit_todo_item():\n    data = request.json\n    # Simulate storing in MongoDB\n    print(f"Received: {data}")\n    return jsonify({"status": "success"})\n')

with open('app/models.py', 'w') as f:
    f.write('class TodoItem:\n    def __init__(self, item_name, item_description):\n        self.item_name = item_name\n        self.item_description = item_description\n')

with open('run.py', 'w') as f:
    f.write('from app import create_app\nfrom app.routes import todo_bp\n\napp = create_app()\napp.register_blueprint(todo_bp)\n\nif __name__ == "__main__":\n    app.run(debug=True)\n')

# Create a sample JSON file for API
with open('data.json', 'w') as f:
    f.write('{"api_message": "Hello from API"}')

# Create a basic frontend HTML file
os.makedirs('templates', exist_ok=True)
with open('templates/todo.html', 'w') as f:
    f.write('''
<!DOCTYPE html>
<html>
<head>
    <title>To-Do Page</title>
</head>
<body>
    <h1>To-Do Page</h1>
    <form id="todoForm">
        <label>Item Name:</label>
        <input type="text" name="itemName" required><br>
        <label>Item Description:</label>
        <textarea name="itemDescription" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
''')

# Create requirements.txt
with open('requirements.txt', 'w') as f:
    f.write('Flask\npymongo\n')

# Print current directory structure for verification
subprocess.run(['ls', '-R'])
