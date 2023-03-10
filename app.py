from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<name>')
def user(name):
    return render_template("index.html",content = ['a', 'b', 'c'])

@app.route('/admin')
def admin():
    return redirect(url_for("user", name = "Admin!"))  #Function name with parameter
    return redirect(url_for("index"))  #Function name



if __name__ == "__main__":
    app.run(debug=True)