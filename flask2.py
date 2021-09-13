from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    '''Handles GET requests / returns Welcome '''
    return 'Welcome'


@app.route('/welcome/home')
def welcome_home():
    '''Handles GET requests / returns Welcome Home '''
    return 'Welcome Home'


@app.route('/welcome/back')
def welcome_back():
    '''Handles GET requests / returns Welcome Back '''
    return 'Welcome Back'
