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
    
@app.route('/feeling')
def Feeling():
    return flask.render_template('feeling.html')

@app.route('/community')
def Community():
    return flask.render_template('community.html')
    
@app.route('/doctor')
def Doctor():
    return flask.render_template('doctor.html')
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)