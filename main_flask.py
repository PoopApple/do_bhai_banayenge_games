from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # show the form

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']  # get form input
    return render_template('result.html', name=name)  # pass it to result page

@app.route('/leaderboard')
def leaderboardView():
    return render_template('leaderboard.html')  # show the form

if __name__ == '__main__':
    app.run(debug=True)




