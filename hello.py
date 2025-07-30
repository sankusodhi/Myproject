# from flask import Flask
# from markupsafe import escape
# app = Flask(__name__)

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route('/price/<float:amount>')
# def show_price(amount):
#     return f'Price is ₹{amount:.2f}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f'Subpath: {escape(subpath)}'

# @app.route('/uuid/<uuid:item_id>')
# def show_uuid(item_id):
#     return f'UUID: {item_id}'
# @app.route('/')
# def index():
#     return '''
#     <h1>Welcome to My Flask Demo</h1>
#     <ul>
#         <li><a href="/user/sanku">/user/sanku</a></li>
#         <li><a href="/post/123">/post/123</a></li>
#         <li><a href="/price/99.99">/price/99.99</a></li>
#         <li><a href="/path/some/sub/path">/path/some/sub/path</a></li>
#         <li><a href="/uuid/123e4567-e89b-12d3-a456-426614174000">/uuid/123e4567-e89b-12d3-a456-426614174000</a></li>
#     </ul>
#     '''






# from flask import Flask

# app = Flask(__name__)
# @app.route('/projects/')
# def projects():
#     return 'This is the Projects page (folder-style with /)'
# @app.route('/about')
# def about():
#     return 'This is the About page (file-style, no slash)'
# @app.route('/')
# def index():
#     return '''
#     <h1>URL Routing Behavior in Flask</h1>
#     <ul>
#         <li><a href="/projects">/projects (redirects to /projects/)</a></li>
#         <li><a href="/projects/">/projects/ (direct match)</a></li>
#         <li><a href="/about">/about (direct match)</a></li>
#         <li><a href="/about/">/about/ (will show 404)</a></li>
#     </ul>
#     '''




# from flask import Flask, url_for

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return f'''
#     <h1>Welcome</h1>
#     <ul>
#         <li><a href="{url_for('login')}">Login</a></li>
#         <li><a href="{url_for('profile', username='sanku')}">Your Profile</a></li>
#     </ul>
#     '''

# @app.route('/login')
# def login():
#     return "Login Page"

# @app.route('/user/<username>')
# def profile(username):
#     return f"Hello, {username}!"





# from flask import Flask, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/login')
# def login():
#     return 'Login Page'

# @app.route('/user/<username>')
# def profile(username):
#     return f"{username}'s profile"

# with app.test_request_context():
#     print("Generated URLs using url_for():")
#     print(url_for('index'))                         
#     print(url_for('login'))                          
#     print(url_for('login', next='/'))               
#     print(url_for('profile', username='John Doe'))   





# from flask import Flask, url_for
# from markupsafe import escape

# app = Flask(__name__)

# # -------------------------------
# # Section 1: Variable Rules
# # -------------------------------
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User: {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post ID: {post_id}'

# @app.route('/price/<float:amount>')
# def show_price(amount):
#     return f'Price is ₹{amount:.2f}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f'Subpath: {escape(subpath)}'

# @app.route('/uuid/<uuid:item_id>')
# def show_uuid(item_id):
#     return f'UUID: {item_id}'

# # -------------------------------
# # Section 2: Trailing Slash Routing Behavior
# # -------------------------------
# @app.route('/projects/')
# def projects():
#     return 'This is the Projects page (with trailing slash)'

# @app.route('/about')
# def about():
#     return 'This is the About page (no trailing slash)'

# # -------------------------------
# # Section 3: url_for() Demonstration on Homepage
# # -------------------------------
# @app.route('/')
# def index():
#     return f'''
#     <h1>Welcome to My Flask Demo</h1>
#     <h2> Variable Routes</h2>
#     <ul>
#         <li><a href="{url_for('show_user_profile', username='sanku')}">User Profile</a></li>
#         <li><a href="{url_for('show_post', post_id=123)}">Post ID</a></li>
#         <li><a href="{url_for('show_price', amount=99.99)}">Price</a></li>
#         <li><a href="{url_for('show_subpath', subpath='some/sub/path')}">Subpath</a></li>
#         <li><a href="{url_for('show_uuid', item_id='123e4567-e89b-12d3-a456-426614174000')}">UUID</a></li>
#     </ul>

#     <h2> Routing Behavior</h2>
#     <ul>
#         <li><a href="/projects">/projects (redirects to /projects/)</a></li>
#         <li><a href="/projects/">/projects/ (direct match)</a></li>
#         <li><a href="/about">/about (direct match)</a></li>
#         <li><a href="/about/">/about/ (404 expected)</a></li>
#     </ul>

#     <h2>🔗 URL Building using url_for()</h2>
#     <ul>
#         <li><a href="{url_for('login')}">Login</a></li>
#         <li><a href="{url_for('login', next='/')}">Login with ?next=/</a></li>
#         <li><a href="{url_for('profile', username='Sanku Sodhi')}">Profile: Sanku Sodhi</a></li>
#     </ul>
#     '''

# @app.route('/login')
# def login():
#     return 'Login Page'

# @app.route('/user/<username>')
# def profile(username):
#     return f"Hello, {escape(username)}!"

# # -------------------------------
# # Section 4: Print url_for() in shell context
# # -------------------------------
# with app.test_request_context():
#     print("\n Generated URLs using url_for():")
#     print(url_for('index'))                          
#     print(url_for('login'))                         
#     print(url_for('login', next='/'))                
#     print(url_for('profile', username='Sanku Sodhi'))   






# from flask import Flask, request, redirect, url_for

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return '<h2>Welcome to the Home Page!</h2><a href="/login">Go to Login</a>'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
        
#         return redirect(url_for('profile', username='Guest'))
#     return '''
#         <form method="post">
#             <h2>Login Page</h2>
#             <input type="submit" value="Login as Guest">
#         </form>
#     '''


# @app.route('/user/<username>')
# def profile(username):
#     return f'<h2>Welcome, {username}!</h2><a href="{url_for("index")}">Back to Home</a>'

# @app.route('/old-home')
# def old_home():

#     return redirect(url_for('index'))

# @app.route('/build-url')
# def build_url():
#     index_url = url_for('index')
#     login_url = url_for('login', next='/user/Guest')
#     profile_url = url_for('profile', username='John Doe')

#     return f'''
#         <h3>URL Building Examples:</h3>
#         <p>Home URL: {index_url}</p>
#         <p>Login URL with next param: {login_url}</p>
#         <p>Profile URL with space: {profile_url}</p>
#     '''

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, request, redirect, url_for

# app = Flask(__name__)


# users = {
#     'sanku': 'password123',
#     'mitlesh': 'bestfriend'
# }

# @app.route('/')
# def home():
#     return '''
#         <h1>Welcome to Flask Mini Project</h1>
#         <p><a href="/login">Login Here</a></p>
#     '''


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')

#         if users.get(username) == password:
#             return redirect(url_for('profile', username=username))
#         else:
#             return '''
#                 <h2>Login Failed</h2>
#                 <p><a href="/login">Try Again</a></p>
#             '''
    
#     return '''
#         <h2>Login Form</h2>
#         <form method="POST">
#             Username: <input name="username"><br>
#             Password: <input name="password" type="password"><br>
#             <input type="submit" value="Login">
#         </form>
#     '''

# @app.route('/profile/<username>')
# def profile(username):
#     return f'''
#         <h1>Welcome, {username}!</h1>
#         <p>This is your profile page.</p>
#         <a href="{url_for('home')}">Go Home</a>
#     '''


# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/user/<username>")
# def user_profile(username):
#     return f"User {username}"

from flask import Flask, render_template, request, session, redirect, url_for, abort

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(401)
def unauthorized_error(error):
    return '''
        <h2>401 Unauthorized</h2>
        <p>You are not authorized to access this page.</p>
        <p><a href="/form">Go to Form</a></p>
    ''', 401

@app.route('/form')
def form():
    return '''
        <form method="post" action="/hello">
            <input name="username" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
        <p><a href="/set?user=Sanku">Set Session via GET</a></p>
    '''

@app.route('/hello', methods=['POST'])
def hello():
    username = request.form['username']
    session['username'] = username  
    return render_template("hello.html", person=username)

@app.route('/set')
def set_session():
    user = request.args.get('user')
    if user:
        session['username'] = user
        return f"Session set for {user}"
    else:
        return "No user provided in query string."

@app.route('/get/')
def get_session():
    username = session.get('username', 'Guest')
    return f"Logged in as: {username}"

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return "Session cleared. You are logged out. <a href='/form'>Go to Form</a>"

if __name__ == '__main__':
    app.run(debug=True)
