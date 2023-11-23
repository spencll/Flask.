from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys
app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
RESPONSES = []

#surveys[satisfaction].questions = list of questions

@app.route('/')
def home():
    RESPONSES.clear()
    return render_template('home.html', surveys=surveys['satisfaction'], question_number=0)

@app.route('/start')
def start():
     return redirect('/questions/0')

#stores responses, goes to next question
@app.route('/answer',methods=["POST"])
def answer():
     RESPONSES.append(request.form['answer'])
     return redirect(f"/questions/{len(RESPONSES)}")

#listener and response
@app.route('/questions/<int:num>')
def question(num): 
        #If user enters wrong question number into url
        if len(RESPONSES) != num:
            flash(f"Invalid question id: {num}.")
            return redirect(f"/questions/{len(RESPONSES)}")
        #loads question
        return render_template('survey.html', question_number=num, surveys=surveys['satisfaction'], responses=RESPONSES)


#things to do
#question page: displays question + radio button + submit button to add to resposnes
#after submit, direct to next number question
#completion page: displays message

