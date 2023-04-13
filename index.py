# from flask import Flask, render_template, request, url_for
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login')
# def about():
#     return render_template('login.html')

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# # @app.route('/login_info', methods=['POST'])
# # def login_info():
# #     email = request.form.get('email')
# #     password = request.form.get('password')
# #     return "the email is {} and th password is {}" .format(email,password)

# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask , request , jsonify
import pickle
import numpy as np
model = pickle.load(open('model.pk1','rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return "hello"

@app.route('/predict' ,methods=['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')

    input_query = np.array([[cgpa,iq,profile_score]])

    result = model.predict(input_query)[0]

    return jsonify({'placement':str(result)})

if __name__ == '__main__':
    app.run(debug=True)


