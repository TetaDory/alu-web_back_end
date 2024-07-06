#!/usr/bin/env python3
"""
A Flask web application that mocks a user login system and displays.
"""

from flask import Flask, request, g, render_template
from typing import Optional, Dict, Any

app = Flask(__name__)

users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Get user by ID from the users dictionary.
    :return: A user dictionary if found, otherwise None.
    """
    try:
        login_as = int(request.args.get('login_as'))
        return users.get(login_as)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request() -> None:
    """
    this code sets user information globally before each request.
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    Render the index page.
    and return Rendered HTML content.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)