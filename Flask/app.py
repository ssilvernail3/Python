from flask import Flask, request 

app = Flask (__name__)

@app.route('/')
def home_page():
     '''Return a message that says hello!'''
     html = '''
     <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page!</p>
            <a href="/hello">Go To Hello Page!</a>
        </body> 
    </html>
     '''
     return html 

    
@app.route('/hello')
def say_hello():
    '''Return a message that says hello!'''

    html = '''
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page!</p>
            <a href="/">Home Page</a>
        </body> 
    </html>
    '''
    return html


@app.route('/goodbye')
def say_bye():
    return 'Say BYE!'


@app.route('/search')
def search():
    '''Handle GET requests like "/search"'''
    term = request.args['term']
    sort = request.args['sort']
    # use term to find database data that matches term 
    return f'<h1>Search Results for: {term}</h1> <p>Sorting by: {sort}</p>'

# @app.route('/post', methods=["POST"])
# def post_demo():
#     '''Handle POST requests for "/post"'''
#     return 'YOU MADE A POST REQUEST!'


# @app.route('/post', methods=["GET"])
# def get_demo():
#     '''Handle POST requests for "/post"'''
#     return 'YOU MADE A GET REQUEST!'


@app.route('/add-comment')
def add_comment_form():
    '''Show form for adding a comment'''
    return '''
    <h1>Add Comment</h1>
    <form method='POST'>
        <input type="text" placeholder="comment" name="comment"/>
        <input type="text" placeholder="username" name="username"/>
        <button>Submit</button>
    </form>
    '''

@app.route('/add-comment', methods=['POST'])
def save_comment():
    '''Handle adding comment'''
    comment = request.form['comment']
    username = request.form['username']
    return f'''
    <h1>Saved Your Comment !</h1>
    <ul>
        <li>Username:{username}</li>
        <li>Comment:{comment}</li>
    </ul>
    '''

@app.route('/r/<subreddit>')
# the variable in pararens <subreddit> will call as a arguemnt in the view function so the argument must match exactly
def show_subreddit(subreddit):
    return f'<h1>Browsing The {subreddit} Subreddit </h1>'


POSTS = {
    1: 'I LIKE CHICKEN TENDERS',
    2: 'I HATE MAYO',
    3: 'DOUBLE RAINBOW ALL THE WAY',
    4: 'YOLO OMG (kill me)'
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, 'POST NOT FOUND')
    return f'<p>{post}</p>'


@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f'<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit</h1>'
