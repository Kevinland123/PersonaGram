"""
ALA index (main) view.
"""
import flask
import os
from flask import render_template
import ala
import stripe
from flask_mail import Message, Mail


mail = Mail()
ala.app.config["MAIL_SERVER"] = "smtp.gmail.com"
ala.app.config["MAIL_PORT"] = 465
ala.app.config["MAIL_USE_SSL"] = True
ala.app.config["MAIL_USERNAME"] = os.getenv('EMAIL_USERNAME')
ala.app.config["MAIL_PASSWORD"] = os.getenv('EMAIL_PASSWORD')
mail.init_app(ala.app)


stripe_keys = { 
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
}

stripe.api_key = stripe_keys["secret_key"]


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
    questions = [
        ['What’s inside each box?',                      '''It can contain anything from snacks to trinkets to discount codes; anything
                                                            that we think your friend might like! We will arrange the box just like we
                                                            would for our own friends.'''], 
        ['How does PersonaGram’s delivery system work?', '''We will hand-deliver the box to the recipient depending on the location.
                                                            Otherwise, we will ship the box.'''], 
        ['How can we contact you?',                      '''For any inquiries, email us at info.personagram@gmail.com!'''], 
        ['How affordable are the boxes?',                '''The boxes are very affordable! You will spend $10 on a gift box
                                                            which is worth a lot more!'''], 
        ['Is shipping included?',                        '''Shipping is included in the total price!'''], 
        ['Will my friend know who it’s from?',           '''The gift box will be completely anonymous, although you have
                                                            the option to include a note'''], 
        ['I didn’t receive any confirmation email. What do I do?',
                                                         '''Check your spam folder! If you still don’t have any communication
                                                            from us, be sure to reach out to us at info.personagram@gmail.com.'''],
        ['Can I refund/exchange my box if I’m not satisfied?',
                                                         '''Unfortunately, we cannot offer any refunds or exchanges since our boxes are personalized.'''],
        ['Can I buy a box for myself?',                  '''Of course! Regardless of who the box is intended for, we will only
                                                            look at the answers to the quiz questions to make sure the box is personalized.'''],
        ['What type of payment does PersonaGram Accept?','''At PersonaGram, we make it easy for you to process your payment.
                                                            We’ve integrated Stripe within our payment, allowing you to
                                                            securely process any payments using VISA, VISA DEBIT,
                                                            MASTERCARD, DISCOVER, and AMERICAN EXPRESS.''']
    ]
    context = {'faqs': questions}
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


@ala.app.route('/quiz/info/', methods=['GET'])
def show_personal_info():
    """Display / route."""
    context = {}
    return render_template("quiz_personal_info.html", **context)


@ala.app.route('/quiz/<question>/', methods=['GET'])
def show_quiz():
    """Display / route."""
    context = {}
    return render_template("quiz_start.html", **context)


def show_quiz_success():
    """Display / route"""

    return render_template("quiz_success.html")
