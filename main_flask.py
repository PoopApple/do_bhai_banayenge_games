from flask import Flask, render_template, request,session
from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import datetime
from datetime import timedelta

import os
from dotenv import load_dotenv


load_dotenv()

uri = os.getenv("MONGO_URL")

myclient = MongoClient(uri, server_api=ServerApi('1'))

db_name = "games_all"
flappy_table_name = "flappy_leaderboard"
simon_table_name = "simonsays_leaderboard"

mydb = myclient[db_name]
flappy_table = mydb[flappy_table_name]
#flappy_table_history = mydb[ftable_name+"_history"]
simon_table = mydb[simon_table_name]

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
app.secret_key = os.getenv('COOKIE_SECRET_KEY')
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
    
    #flappy_table_history.insert_one(sc_row.copy())
    if(your_score < score):
        flappy_table.update_one(
            {"name": session['name']},           # filter: which document to update
            {"$set": sc_row.copy()},      # update: what to change
            upsert=True                          # optional: insert if not found
        )
        return render_template('flappygameover.html', score = score,pb=score)
    
    return render_template('flappygameover.html', score = score,pb=your_score)  # pass it to result page

@app.route('/fb_leaderboard',)
def flappyleaderboard():
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


@app.route('/simongameover', methods = ['POST'])
def simongameover():
    entry = simon_table.find_one({"name":session['name']})
    if entry:
        your_score = entry['score']
    else:
        your_score = -1
    score = int(request.form['hidden_score_val'] )
    print(score)
    sc_row = {"name" : session['name'] , "score" : score, "date_time" : datetime.datetime.now().strftime("%d %b %Y  %I:%M %p")}
    
    #flappy_table_history.insert_one(sc_row.copy())
    if(your_score < score):
        simon_table.update_one(
            {"name": session['name']},           
            {"$set": sc_row.copy()},      
            upsert=True            # agar nhi h toh insert
        )
        return render_template('simonsays_gameover.html', score = score,pb=score)
    
    return render_template('simonsays_gameover.html', score = score,pb=your_score)  

@app.route('/ss_leaderboard',)
def simonleaderboard():
    lb_scores = simon_table.find().sort("score",pymongo.DESCENDING)
    your_score = simon_table.find_one({"name":session['name']})
    if your_score:
        rank = simon_table.count_documents({'score': {'$gt': your_score["score"]}}) + 1
    else:
        rank = "-"
    return render_template('simonsays_leaderboard.html' , scores = lb_scores, your_score=your_score,rank=rank)  # show the form



if __name__ == '__main__':
    app.run(debug=True)




