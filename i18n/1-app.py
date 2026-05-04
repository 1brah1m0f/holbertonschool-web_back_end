#!/bin/usr/env python3
"""1-app.py"""
from flask import Flask
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)

class Config:
    """Config class for Babel settings."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)  

@app.route('/')
def index():
    """Render the homepage."""
    return "Hello World"
if __name__ == "__main__":
    app.run(debug=True)
