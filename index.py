from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def about():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# @app.route('/login_info', methods=['POST'])
# def login_info():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     return "the email is {} and th password is {}" .format(email,password)

if __name__=="__main__":
    app.run(debug=True)
