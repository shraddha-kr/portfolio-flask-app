#from flask import Flask, render_template, request, escape, flash
from flask import *
from vsearch.vsearch import search4letters
from contactform import ContactForm
from flask_mail import Message, Mail


app = Flask(__name__)
app.secret_key ='srk development portfolio'


# Main App
@app.route('/')
@app.route('/index')
def index_page() -> 'html':
    return render_template('index.html',
                           the_title='Shraddha Kharangate')


@app.route('/projects')
def projects_page() -> 'html':
    return render_template('projects.html',
                           the_title=' Project List')

@app.route('/toBeDone')
def toBeDone_page() -> 'html':
    return render_template('thankyou.html',
                           the_title='To Be Done')

# Vowel Search App
@app.route('/vsearch/entry')
def entry_page() -> 'html':
    return render_template('/vsearch/entry.html',
                           the_title='Search For Vowels')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = 'aeiou'
    title = 'Search Results'
    # Formatting result
    results = str(search4letters(phrase, letters)).strip('{}')
    results = results.replace("'", "")
    return render_template('/vsearch/results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)

# ContactMe & Mail setup
mail = Mail()

app.config["MAIL_SERVER"]= "smtp.gmail.com"
app.config["MAIL_PORT"]= 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"]= 'shraddha.krs@gmail.com'
app.config["MAIL_PASSWORD"]= 'pingoo123'

mail.init_app(app)

@app.route('/contactme',  methods=['GET', 'POST'])
def contactme_page():
    form = ContactForm()
    print("Validating Form....")
    if form.validate_on_submit():
        print('[form.subject.data]', form.subject.data)
        msg = Message(form.subject.data, sender=form.email.data,
                      recipients=['shraddha.krs@gmail.com'])
        msg.body = """
        From:-
        Name: %s
        Email: <%s>
        Subject: %s
        Message: %s
        """ % (form.name.data, form.email.data, form.subject.data, form.message.data)
        mail.send(msg)

        return render_template('thankyou.html',
                                the_title='Thank You!',
                                form=form)
    return render_template('contactme.html',
                            the_title='Contact Me',
                            form=form)


if __name__ == '__main__':
    app.run(debug=True)
