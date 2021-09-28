"""
Insta485 index (main) view.

URLs include:
/
"""
import flask
from flask import render_template
import ala


@ala.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return render_template("index.html", **context)