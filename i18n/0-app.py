#!/usr/bin/env python3
"""
0-app.py

Basic Flask application.
This module initializes a Flask app and renders a single HTML page.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Handles the root URL.

    Returns:
        str: Rendered HTML template for the homepage.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
