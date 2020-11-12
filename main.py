from flask import Flask, request, redirect, url_for, render_template
import smtplib
from flask_mobility import Mobility
from firebase import firebase

# firebase = firebase.FirebaseApplication('https://abj-website.firebaseio.com/')

# result = firebase.post('/data', data)


app = Flask(__name__)
Mobility(app)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/about')
def about():
    return render_template("about2.html")

@app.route('/suggestions', methods = ["POST", "GET"])
def suggestions():
    if request.method == "POST":
        stuff = request.form["sug"]
        print(stuff)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('suggestabj@gmail.com', 'P@@ssword123')

            subject = "suggestion"
            body = str(stuff)

            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail('suggestabj@gmail.com', 'agentbobjelly@gmail.com', msg)
    return render_template("suggestions2.html")

@app.route('/products')
def products():
    return render_template("products.html")


if __name__ == "__main__":
    app.run(debug=False)