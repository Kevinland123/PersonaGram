"""
Insta485 index (main) view.
"""
import flask
from flask import render_template
import ala


@ala.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return render_template("index.html", **context)

@ala.app.route('/about/')
def show_about():
    """Display / route."""
    context = {}
    return render_template("about.html", **context)

@ala.app.route('/faq/')
def show_faq():
    """Display / route."""
    context = {}
    return render_template("faq.html", **context)

@ala.app.route('/contact/')
def contact():
    """Contact page."""
    context = {}
    return render_template("contact.html", **context)

@ala.app.route('/quiz/')
def show_quiz_start():
    """Display / route."""
    context = {}
    return render_template("quiz_start.html", **context)

@ala.app.route('/quiz/<question>')
def show_quiz():
    """Display / route."""
    context = {}
    return render_template("quiz_start.html", **context)

@ala.app.route('/information/')
def show_personal_info():
    """Display / route."""
    context = {}
    return render_template("personal_info.html", **context)
