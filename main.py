from flask import Flask, render_template, request, url_for, redirect



app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def myapp():
    value = 0
    if request.method == 'POST':
        value = int(request.form['num'])
        value *= 5.5
    
    return render_template('index.html', val=value)

if __name__ == "__main__":
    app.run(debug=False)