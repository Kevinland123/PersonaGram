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
def show_quiz_info():
    """Display / route."""
    context = {}
    return render_template("quiz_personal_info.html", **context)


@ala.app.route('/quiz/questions/', methods=['GET', 'POST'])
def show_quiz():
    """Display / route."""
    questions = [
        [0, "What's the receiver's favorite color?"],
        [1, "What is the receiver's ideal vacation?"],
        [2, "Which of the following best describe your giftee?"],
        [3, "It's finals season. The recipient doesn't have time to cook food so they grab something quick to eat. What would they grab to eat?"]
        [4, "What environment suits the receiver the most?"]
        [5, "What best describes the receiver's fashion sense?"]
        [6, "What kind of student is the receiver?"]
        [7, "Where is their favorite place to study?"]
        [8, "If your giftee was living in a movie, what genre would it be?"]
        [9, "Your giftee is on AUX. What genre is playing right now?"]
        [10, "You're traveling through an enchanted forest and come across four potions. Which one do you give to your receiver?"]
        [11, "What is your giftee's love language?"],
        [12, "What is the receiver's favorite holiday?"],
        [13, "How is your receiver spending their free time?"]
    ]
    answers = [
        ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"],
        ["Exploring a new city", "Anywhere with a beach", "Hiking in a national park", "They like to stay at home"],
        ["Morning bird", "Afternoon antelope", "Night owl"]
        ["Something healthy", "Something greasy", "Something sweet", "They won't eat until their exams are over :("],
        ["Their home", "The Union", "Rick's", "The Arb", "The Beach"],
        ["Cottagecore", "E-girl", "Plain-Jane", "Groufit", "Athletic", "Comfy"],
        ["Clutch procrastinator", "Over-acheiver", "Doesn't take notes", "Organized"],
        ["At home/dorm", "Outside/The Diag", "Study lounges", "The UGLi"],
        ["Romance", "Mystery", "Drama", "Comedy", "Horror"],
        ["Rap", "Pop", "Country", "Rock", "Hip-Hop", "Classical"],
        ["The shimmering gold potion enchanted with the power of wealth", "The dark green frothing potion containing infinite knowledge", "The light pink potion filled with love", "The enriching potion that’s really a protein shake"],
        ["Words of affirmation", "Acts of service", "Receiving gifts", "Quality time", "Physical touch"],
        ["Halloween", "Christmas", "Thanksgiving", "New Year", "Their Birthday", "They hate fun"],
        ["Playing sports", "Reading a book", "Playing video games", "Doing Arts & Crafts", "Watching a movie"]


    ]
    context = { 'questions': questions,
                'answers': answers}
    return render_template("quiz.html", **context)


@ala.app.route('/quiz/success/', methods=['GET', 'POST'])
def show_quiz_success():
    """Display / route"""
    return render_template("quiz_success.html")


@ala.app.route("/config")
def get_publishable_key():
    """Stripe Public Key Config."""
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return flask.jsonify(stripe_config)


@ala.app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://localhost:8000/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - capture the payment later
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": "$10 Mystery Box",
                    "quantity": 1,
                    "currency": "usd",
                    "amount": "1000",
                }
            ]
        )
        return flask.jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return flask.jsonify(error=str(e)), 403


@ala.app.route("/success")
def success():
    return render_template("payment_success.html")


@ala.app.route("/cancelled")
def cancelled():
    return render_template("payment_cancelled.html")
