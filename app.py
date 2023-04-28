from flask import Flask,flash, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'fashion_database'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def home():
    return render_template('loginpage.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = User.query.all()

        for user in users:
            print(user.username,user.password)
        user = User.query.filter_by(username=username).first()

        print("user",user)
        if user is not None and user.password == password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('loginpage.html', error=error)

    return render_template('loginpage.html')

@app.route('/product_kid')
def product_kid():
    return render_template('product_kid.html')


@app.route('/product_women')
def product_women():
    return render_template('product_women.html')

@app.route('/product_men')
def product_men():
    return render_template('products_men.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # new_users = [
        # User(username='santosh', password='ainumpudi'),
        # User(username='sravya', password='dama'),
        # User(username='sudeshna', password='mullaguru'),
        # User(username='monisha', password='lanka')
        # ]
        # db.session.add_all(new_users)
        # db.session.commit()
        
    app.run(debug=True)