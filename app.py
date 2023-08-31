from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Khabertkey'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

  # Create database tables

@app.route('/')
def index():
     user = None
     if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
     return render_template('index.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            session['user_id'] = user.id  # Store user's ID in session
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials. Please try again."
            return render_template('login.html', error=error)
    
    return render_template('login.html', error=None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('signup.html', error=None)
@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()
    return render_template('logout.html')
@app.route('/kampala.html')
def kampala():
    return render_template('kampala.html')

if __name__ == '__main__':
    with app.app_context():
     db.create_all()
    app.run(debug=True)