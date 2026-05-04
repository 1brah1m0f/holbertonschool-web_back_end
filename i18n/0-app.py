from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello HBNB!"  # ← burada "Welcome to Holberton" olmalıdır

if __name__ == "__main__":
    app.run()