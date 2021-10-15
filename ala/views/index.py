"""
ALA index (main) view.
"""
import flask
import os
from flask import render_template
import ala
from flask_mail import Message, Mail


mail = Mail()
ala.app.config["MAIL_SERVER"] = "smtp.gmail.com"
ala.app.config["MAIL_PORT"] = 465
ala.app.config["MAIL_USE_SSL"] = True
ala.app.config["MAIL_USERNAME"] = os.getenv('EMAIL_USERNAME')
ala.app.config["MAIL_PASSWORD"] = os.getenv('EMAIL_PASSWORD')
mail.init_app(ala.app)


@ala.app.route('/', methods=['GET'])
def show_index():
    """Display / route."""
    context = {}
    return render_template("index.html", **context)


@ala.app.route('/about/', methods=['GET'])
def show_about():
    """Display / route."""
    context = {}
    return render_template("about.html", **context)


@ala.app.route('/faq/', methods=['GET'])
def show_faq():
    """Display / route."""
    context = {}
    return render_template("faq.html", **context)


@ala.app.route('/contact/', methods=['GET', 'POST'])
def contact():
    """Contact page."""
    if flask.request.method == 'POST':
        contact_name = flask.request.form['name']
        contact_email = flask.request.form['email']
        contact_phone = flask.request.form['phone']
        contact_message = flask.request.form['message']
        msg = Message('Inquiry', 
                      sender=('Contact Inquiry', os.getenv('EMAIL_USERNAME')),
                      recipients=[os.getenv('EMAIL_USERNAME')])
        msg.body = """
        From: %s <%s> <%s>

        %s
        """ % (contact_name, contact_phone, contact_email, contact_message)
        mail.send(msg)
        return render_template("contact.html", success=True)

    return render_template("contact.html")


@ala.app.route('/quiz/', methods=['GET'])
def show_quiz_start():
    """Display / route."""
    context = {}
    return render_template("quiz_start.html", **context)


@ala.app.route('/quiz/<question>', methods=['GET'])
def show_quiz():
    """Display / route."""
    context = {}
    return render_template("quiz_start.html", **context)


@ala.app.route('/information/', methods=['GET'])
def show_personal_info():
    """Display / route."""
    context = {}
    return render_template("personal_info.html", **context)
