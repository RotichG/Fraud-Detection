from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template('login.html')
@app.route("/index")
def index_page():
    return render_template('index.html')    

