from boggle import Boggle
from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

#main page
@app.route('/')
def main():
    session['board'] = boggle_game.make_board()
    high_score = session.get("high_score", 0)
    nplays = session.get("nplays", 0)
    return render_template("home.html", board = session['board'], highscore = high_score, nplays=nplays)

#uses server guess route to return validity 
@app.route('/guess')
def guess():
    word = request.args['input']
    board = session['board']
    response = boggle_game.check_valid_word(board, word)
    return jsonify({'result': response, 'word':word})

#stores post into session high score
@app.route('/score',methods=['POST'])
def score():
    session['score'] = int(request.json['score'])
    high_score = session.get("high_score", 0)
    nplays = session.get("nplays", 0)
    
    session['nplays'] = nplays +1
    session['high_score'] = max(session['score'],high_score)

    return jsonify({'high_score': session['high_score']})
    

