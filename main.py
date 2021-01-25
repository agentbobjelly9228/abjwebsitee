from flask import Flask, request, redirect, url_for, render_template
import smtplib
from flask_mobility import Mobility
from firebase import firebase
firebase = firebase.FirebaseApplication('https://abj-website-coming.firebaseio.com/', None)
# data = {
#     'coming soon': ]
#         'placeholder',
#         {'test': 'https://images-na.ssl-images-amazon.com/images/I/512dVKB22QL._AC_UL600_SR600,600_.png'} 
#         ]
# }
# result = firebase.post('/data', data)
result = firebase.get('/data/-MM-Fk81Pb_-is1HFBre/coming soon', '')
print(result)

app = Flask(__name__)
Mobility(app)

@app.route('/')
def index():
    return render_template('index2.html', coming=result)

@app.route('/about')
def about():
    return render_template("about2.html")

@app.route('/suggestions', methods = ["POST", "GET"])
def suggestions():
    if request.method == "POST":
        try:
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
        except Exception as e:
            return str(e)
    return render_template("suggestions2.html")

@app.route('/products')
def products():
    return render_template("products.html")


if __name__ == "__main__":
    app.run(debug=False)