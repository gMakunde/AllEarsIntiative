import os
import flask

app = flask.Flask(__name__)

@app.route('/a')
def InitialQuestions():
    return flask.render_template('intitalquestions.html')
    
@app.route('/')
def Dashboard():
    return flask.render_template('dashboard.html')
    
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)