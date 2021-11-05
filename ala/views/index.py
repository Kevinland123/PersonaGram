"""
ALA index (main) view.
"""
import flask
import os
from flask import render_template, redirect
import ala
import uuid
import stripe
from flask_mail import Message, Mail


mail = Mail()
ala.app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    # MAIL_USERNAME=os.getenv('EMAIL_USERNAME'),        # heroku can't read from os?
    MAIL_USERNAME='info.personagram@gmail.com',
    # MAIL_PASSWORD=os.getenv('EMAIL_PASSWORD'),
    MAIL_PASSWORD='GoBlueAla223',
)
mail.init_app(ala.app)


stripe_keys = {
    # "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "secret_key": 'sk_test_51JjS6DCN8bi5qyoSGcf9Qtqv8tDkr5HsGsworONzNjzdoelRhue5PDEMD6wjFhed6jHz7hjfn5BFiaGGLYIcOn5F00bexWmF63',
    "publishable_key": 'pk_test_51JjS6DCN8bi5qyoSHSPzD0Lc33W1OtQ1sWPrPE6VBh62hISfqJAYbrVJw5c4CisU7JM3Y8ZcKePoHkIkLPPOsS7F00wKVSSlSg'
    # "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
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
        ['How does PersonaGram’s delivery system work?', '''We will hand-deliver the box to the Ann Arbor vicinity, and we will send an email 
                                                            confirming our delivery date to the sender 1-2 days prior.'''],
        ['When will the box be available for pickup?',   '''We will have a few pickup dates on campus, date and time TBD via email to the reciever.'''],
        ['How can we contact you?',                      '''For any inquiries, email us at info.personagram@gmail.com!'''],
        ['How affordable are the boxes?',                '''The boxes are very affordable! You will spend $10 on a gift box
                                                            that is worth a lot more than its price!'''],
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


        body = """
        From: %s <%s> <%s>

        %s
        """ % (contact_name, contact_phone, contact_email, contact_message)

        msg = Message('Inquiry',
                      sender=('Contact Inquiry', 'info.personagram@gmail.com'),
                      recipients=['info.personagram@gmail.com'],
                      body=body)
        mail.send(msg)
        
        return render_template("contact.html", success=True)

    return render_template("contact.html")


@ala.app.route('/admin/adminPageForKevinToLookAtOnly/', methods=['GET'])
def admin():
    """Admin page."""
    connection = ala.model.get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM users "
    )
    users = cur.fetchall()
    cur = connection.execute(
        "SELECT * "
        "FROM answers "
    )
    answers = cur.fetchall()

    context = {
        'users': users,
        'answers': answers
    }

    return render_template("admin.html", **context)


@ala.app.route('/quiz/', methods=['GET'])
def show_quiz_start():
    """Display / route."""
    context = {}
    return render_template("quiz_start.html", **context)


@ala.app.route('/quiz/info/', methods=['GET', 'POST'])
def show_quiz_info():
    """Display / route."""
    if flask.request.method == 'POST':
        exid = str(uuid.uuid4())
        # flask.session['exid'] = exid
        sender_name = flask.request.form['sender_name']
        sender_email = flask.request.form['sender_email']
        sender_number = flask.request.form['sender_number']
        recipient_name = flask.request.form['recipient_name']
        recipient_email = flask.request.form['recipient_email']
        recipient_number = flask.request.form['recipient_number']
        recipient_email = flask.request.form['recipient_email']
        street = flask.request.form['street']
        city = flask.request.form['city']
        zipcode = flask.request.form['zipcode']
        method = flask.request.form['method']
        context = {
            'exid': exid,
            'sender_name': sender_name,
            'sender_email': sender_email,
            'sender_number': sender_number,
            'recipient_name': recipient_name,
            'recipient_email': recipient_email,
            'recipient_number': recipient_number,
            'street': street,
            'city': city,
            'zipcode': zipcode,
            'method': method,
            'paid': 0
        }
        print(context)

        # Create new SQL entry and get the ID
        connection = ala.model.get_db()
        connection.execute(
            "INSERT INTO "
            "users (exid, senderName, senderEmail, senderPhone, receiverName, receiverEmail, receiverPhone, street, city, zipcode, method)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
            (exid, sender_name,sender_email,sender_number, recipient_name, recipient_email, recipient_number, street, city, zipcode, method,)
        )

        # Redirect to quiz
        return redirect(flask.url_for('show_quiz', id=exid))
    return render_template("quiz_personal_info.html")


@ala.app.route('/quiz/questions/<id>', methods=['GET', 'POST'])
def show_quiz(id):
    """Display / route."""
    # check if session uuid is in database, else go back to home page
    connection = ala.model.get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM users "
        "WHERE exid = ?", (id, )
    )
    user = cur.fetchall()
    if len(user) == 0:
        print("Error: Invalid exid")
        return redirect(flask.url_for('show_index'))

    if flask.request.method == 'POST':
        cur = connection.execute(
            "SELECT id "
            "FROM users "
            "WHERE exid = ?", (id, )
        )

        userid = cur.fetchone()
        print(userid['ID'])

        q1 = flask.request.form['1']
        q2 = flask.request.form['2']
        q3 = flask.request.form['3']
        q4 = flask.request.form['4']
        q5 = flask.request.form['5']
        q6 = flask.request.form['6']
        q7 = flask.request.form['7']
        q8 = flask.request.form['8']
        q9 = flask.request.form['9']
        q10 = flask.request.form['10']
        q11 = flask.request.form['11']
        q12 = flask.request.form['12']
        q13 = flask.request.form['13']
        q14 = flask.request.form['14']
        q15 = flask.request.form['15']
        q16 = flask.request.form['16']

        check = {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'q6': q6,
            'q7': q7,
            'q8': q8,
            'q9': q9,
            'q10': q10,
            'q11': q11,
            'q12': q12,
            'q13': q13,
            'q14': q14,
            'q15': q15,
            'q16': q16,
        }

        print(check)
        connection = ala.model.get_db()

        # Cool SQL
        # For future, if answer already exist then update the answer instead
        connection.execute(
            "INSERT INTO "
            "answers (ID, answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12, answer13, answer14, answer15, answer16)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
            (userid['ID'],q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16)
        )

        # Redirect
        return redirect(flask.url_for('show_quiz_success', id=id))

    questions = [
        [0, "What's the receiver's favorite color?"],
        [1, "What is the receiver's ideal vacation?"],
        [2, "Which of the following best describe your giftee?"],
        [3, "It's finals season. The recipient doesn't have time to cook food so they grab something quick to eat. What would they grab to eat?"],
        [4, "What environment suits the receiver the most?"],
        [5, "What best describes the receiver's fashion sense?"],
        [6, "What kind of student is the receiver?"],
        [7, "Where is their favorite place to study?"],
        [8, "If your giftee was living in a movie, what genre would it be?"],
        [9, "Your giftee is on AUX. What genre is playing right now?"],
        [10, "You're traveling through an enchanted forest and come across four potions. Which one do you give to your receiver?"],
        [11, "What is your giftee's love language?"],
        [12, "What is the receiver's favorite holiday?"],
        [13, "How is your receiver spending their free time?"]
    ]
    answers = [
        ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"],
        ["Exploring a new city", "Anywhere with a beach", "Hiking in a national park", "They like to stay at home"],
        ["Morning bird", "Afternoon antelope", "Night owl"],
        ["Something healthy", "Something greasy", "Something sweet", "They won't eat until their exams are over :("],
        ["Their home", "The Union", "Rick's", "The Arb", "The beach"],
        ["Cottagecore", "E-girl", "Plain-Jane", "Groufit", "Athletic", "Comfy"],
        ["Clutch procrastinator", "Over-acheiver", "Doesn't take notes", "Organized"],
        ["At home/dorm", "Outside/The Diag", "Study lounges", "The UGLi"],
        ["Romance", "Mystery", "Drama", "Comedy", "Horror"],
        ["Rap", "Pop", "Country", "Rock", "Hip-Hop", "Classical"],
        ["The shimmering gold potion enchanted with the power of wealth", "The dark green frothing potion containing infinite knowledge", "The light pink potion filled with love", "The enriching potion that’s really a protein shake"],
        ["Words of affirmation", "Acts of service", "Receiving gifts", "Quality time", "Physical touch"],
        ["Halloween", "Christmas", "Thanksgiving", "New Year", "July 4th", "Their Birthday", "They hate fun"],
        ["Playing sports", "Reading a book", "Playing video games", "Going to the gym", "Doing arts & crafts", "Watching a movie"]
    ]

    context = { 'questions': questions,
                'answers': answers }
    return render_template("quiz.html", **context)


@ala.app.route('/quiz/success/<id>', methods=['GET', 'POST'])
def show_quiz_success(id):
    """Display / route"""
    # Check
    connection = ala.model.get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM users "
        "WHERE exid = ?", (id, )
    )
    user = cur.fetchall()
    if len(user) == 0:
        print("Error: Invalid exid")
        return redirect(flask.url_for('show_index'))

    context = {
        'id': id
    }

    return render_template("quiz_success.html", **context)


@ala.app.route("/config")
def get_publishable_key():
    """Stripe Public Key Config."""
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return flask.jsonify(stripe_config)


@ala.app.route("/create-checkout-session/<id>/")
def create_checkout_session(id):
    domain_url = "http://localhost:8000/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success/" + id + "/?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "quiz/success/" + id,
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


@ala.app.route("/success/<id>/", methods=['GET'])
def success(id):
    # Check if user exist
    connection = ala.model.get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM users "
        "WHERE exid = ?", (id, )
    )
    user = cur.fetchall()
    if len(user) == 0:
        print("Error: Invalid exid")
        return redirect(flask.url_for('show_index'))
    
    # Update paid
    connection.execute(
        "UPDATE users "
        "SET paid = ? "
        "WHERE exid = ?", (1, id, )
    )
    
    return render_template("payment_success.html")
