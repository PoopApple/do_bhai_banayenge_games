from flask import Flask, render_template, request,session
from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import datetime
from datetime import timedelta

uri = "did a fuck and now im here changin all the god damned commits"

myclient = MongoClient(uri, server_api=ServerApi('1'))

db_name = "games_all"
table_name = "flappy_leaderboard"

mydb = myclient[db_name]
flappy_table = mydb[table_name]
flappy_table_history = mydb[table_name+"_history"]


try:
    myclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    
dblist = myclient.list_database_names()
if db_name in dblist:
  print("The database exists.")
else:
    print("not exists")
    




app = Flask(__name__)
app.secret_key = "did a fuck and now im here changin all the god damned commits"
app.permanent_session_lifetime = timedelta(days=7)

#NOTE bhai isse env file me daaldio

@app.route('/')
def index():
    return render_template('index.html')
    


@app.route('/getname')
def getname():
    if('name' in session):
        return render_template('getname.html',name = session['name'])
    return render_template('getname.html')  # show the form
    
@app.route('/mainmenu', methods = ['POST','GET'])
def mainmenu():
    if ("name" not in session):
        session.permanent = True
    if(request.method == 'POST'):
        session['name'] = request.form['name'] # store form input into session deets
    return render_template('mainmenu.html' )  # pass it to result page


@app.route('/flappyintro')
def flappyintro():
    return render_template('flappyintro.html' )  # pass it to result page

@app.route('/flappy')
def flappy():
    return render_template('flappy.html')  # pass it to result page

@app.route('/flappygameover', methods = ['POST'])
def flappygameover():
    entry = flappy_table.find_one({"name":session['name']})
    if entry:
        your_score = entry['score']
    else:
        your_score = -1
    score = int(request.form['hidden_score_val'] )
    sc_row = {"name" : session['name'] , "score" : score, "date_time" : datetime.datetime.now().strftime("%d %b %Y  %I:%M %p")}
    
    flappy_table_history.insert_one(sc_row)
    if(your_score < score):
        flappy_table.update_one(
            {"name": session['name']},           # filter: which document to update
            {"$set": sc_row},      # update: what to change
            upsert=True                          # optional: insert if not found
        )
        return render_template('flappygameover.html', score = score,pb=score)
    
    return render_template('flappygameover.html', score = score,pb=your_score)  # pass it to result page

@app.route('/leaderboard',)
def leaderboardView():
    lb_scores = flappy_table.find().sort("score",pymongo.DESCENDING)
    your_score = flappy_table.find_one({"name":session['name']})
    if your_score:
        rank = flappy_table.count_documents({'score': {'$gt': your_score["score"]}}) + 1
    else:
        rank = "-"
    return render_template('flappy_leaderboard.html' , scores = lb_scores, your_score=your_score,rank=rank)  # show the form


@app.route('/simonsays')
def simonsays():
    return render_template('simonsays.html')

@app.route('/simonintro')
def simonintro():
    return render_template('simonintro.html')


if __name__ == '__main__':
    app.run(debug=True)




