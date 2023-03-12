from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:'adminroot@123'@localhost/crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #Doesnt display warnings

db = SQLAlchemy(app)




@app.route('/')
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)