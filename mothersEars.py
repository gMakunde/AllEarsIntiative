import os
import flask

app = flask.Flask(__name__)

@app.route('/questions')
def InitialQuestions():
    return flask.render_template('intitalquestions.html')
    
@app.route('/')
def Homepage():
    return flask.render_template('homepage.html')

@app.route('/dash')
def Dashboard():
    return flask.render_template('dashboard.html')
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)