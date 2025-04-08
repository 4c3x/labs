from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'secure_key_here'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add authentication logic here
        session['user'] = username
        return "Logged in!"
    return render_template('login.html')