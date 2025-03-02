from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate



# db = SQLAlchemy()
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./kavydb.db'
# app.secret_key = 'your_secret_key'

# migrate = Migrate(app,db)

# db.init_app(app)
users = {}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            return render_template("home.html")
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists', 'error')
        else:
            users[username] = generate_password_hash(password)
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contect")
def contect():
    return render_template("contect.html")

if __name__ == '__main__':
    app.run(debug=True)