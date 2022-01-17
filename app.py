from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/prices")
def prices():
    return render_template('prices.html')

@app.route("/T-and-C")
def tandc():
    return render_template('T-and-C.html')

if (__name__ == "__main__"):
    app.run(debug=True)