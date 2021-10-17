from logging import debug
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.wrappers import response 
from surveys import Question, satisfaction_survey as survey 




app = Flask(__name__)
app.config['SECRET_KEY'] = 'shsboi33'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

RESPONSES_KEY = 'responses' 



@app.route('/')
def start_survey():

    return render_template('home.html')

@app.route('/session-answer', methods=['POST'])
def start_surveys():
        session[RESPONSES_KEY] = []
        return redirect('/questions/0')


@app.route('/questions/<int:qid>')
def second_question(qid):
    responses = session.get(RESPONSES_KEY)

    if (len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")
        
    question = survey.questions[qid]
    return render_template('question_two.html', question_num=qid, question=question)


@app.route('/answer', methods=['POST'])
def add_answer():
    answer = request.form['answer']
    responses = session[RESPONSES_KEY]
    responses.append(answer)
    session[RESPONSES_KEY] = responses
    
    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(responses)}")


@app.route('/complete')
def complete():
    return render_template('complete.html')