from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home', methods = ['GET', 'POST'])
def find_thing():
    return render_template('home.html')