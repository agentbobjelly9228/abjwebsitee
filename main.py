from flask import Flask



app = Flask(__name__)

@app.route('/')
def myapp():
    return '<h1>hi</h1>'

while __name__ == "__main__":
    app.run(debug=False)