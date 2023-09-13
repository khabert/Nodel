This web application is called COMMUNITY FOOD SECURITY AND NUTRITION INITIATIVE and it is designed by Kabagambe Herbert an ALX student 2023 cohort 11.
Deployed site http://3.83.253.201/, Blog article https://cfsni.blogspot.com/2023/09/the-community-food-security-and.html, linkedIn https://www.linkedin.com/in/kabagambe-herbert-499050270
This web application is to help people especially in Uganda to know and access nutrious food and teache them about balanced diet.
In a quaint Ugandan village, I grew up alongside my neighbor, David. Our families, like many others, had access to farmland but struggled with understanding balanced nutrition. Despite my agricultural studies at a local university, it was apparent that our community needed a solution. Inspired by my roots and the desire to bridge this gap, I embarked on the journey of creating the Community Food Initiative. This platform aimed to provide valuable information on balanced diets, educate on growing nutritious crops, and connect locals with nearby food sources. Through dedication and a deep understanding of agriculture and nutrition, the project became a reality, transforming not only my village but also the lives of many others. My story underscores the profound impact that combining personal passion with a commitment to address societal challenges can achieve, as the Community Food Initiative continues to make a meaningful difference.
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
    
    return render_template('login.html', error=None) this helped me to redirect user's after logging in to the dashboard because before it was failing.
