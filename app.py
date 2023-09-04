from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Khabertkey'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
# Create database tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
# Define a model for job applicants
class JobApplicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    qualifications = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=False)

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

@app.route('/kampala_initiatives')
def kampala_initiatives():
    return render_template('kampala_initiatives.html')
@app.route('/Eastern_ug')
def Eastern_ug():
    # Your code to render kampala_initiatives.html goes here
    return render_template('Eastern_ug.html')

@app.route('/Western_ug')
def Western_ug():
    return render_template('Western_ug.html')

@app.route('/Northen_ug')
def Northern_ug():
    return render_template('Northern_ug.html')

@app.route('/Southern_ug')
def Southern_ug():
    return render_template('Southern_ug.html')

# the route to the apply form
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        qualifications = request.form['qualifications']
        age = request.form['age']
        location = request.form['location']
        gender = request.form['gender']

        # Create a new job applicant and add to the database
        new_applicant = JobApplicant(name=name, email=email, qualifications=qualifications, age=age, location=location, gender=gender)
        db.session.add(new_applicant)
        db.session.commit()

        # Redirect to a the appropriate page
        return redirect(url_for('submit_application.html'))

    return render_template('job_application.html')

@app.route('/applicants')
def get_applicants():
    applicants = JobApplicant.query.all()
    return render_template('applicants.html', applicants=applicants)


@app.route('/submit_application', methods=['GET', 'POST'])
def submit_application():
    # Your code for handling the application submission
    return render_template('submit_application.html')

if __name__ == '__main__':
    with app.app_context():
     db.create_all()
    app.run(debug=True)