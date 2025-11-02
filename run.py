from app import create_app
from app.routes import todo_bp

app = create_app()
app.register_blueprint(todo_bp)

if __name__ == "__main__":
    app.run(debug=True)
