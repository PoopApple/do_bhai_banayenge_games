from flask import Flask, render_template, request,session
from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import datetime
from datetime import timedelta

uri = "mongodb+srv://Atriays:VRkDtlmnmxyYnQZM@do-bhai-banayenge-games.bmuo0ev.mongodb.net/?retryWrites=true&w=majority&appName=do-bhai-banayenge-games"

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
app.secret_key = 'pritish_aur_aryan_ka_secret_code_sex_sex_sex'
app.permanent_session_lifetime = timedelta(days=7)

#NOTE bhai isse env file me daaldio

@app.route('/')
def index():
    if('name' in session):
        return render_template('index.html',name = session['name'])
    return render_template('index.html')  # show the form
    
@app.route('/mainmenu', methods = ['POST','GET'])
def mainmenu():
    if ("name" not in session):
        session.permanent = True
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
    your_score = flappy_table.find({"name":session['name']}).sort("score",pymongo.DESCENDING).limit(1)[0]['score']
    score = int(request.form['hidden_score_val'] )
    sc_row = {"name" : session['name'] , "score" : score, "date_time" : datetime.datetime.now().strftime("%d %b %Y  %I:%M %p")}
    
    flappy_table_history.insert_one(sc_row)
    if(your_score < score):
        
        flappy_table.update_one(sc_row)
        return render_template('flappygameover.html', score = score,pb=score)
    
    return render_template('flappygameover.html', score = score,pb=your_score)  # pass it to result page

@app.route('/leaderboard',)
def leaderboardView():
    lb_scores = flappy_table.find().sort("score",pymongo.DESCENDING)
    your_score = flappy_table.find({"name":session['name']}).sort("score",pymongo.DESCENDING).limit(1)
    print(your_score[0])
    rank = flappy_table.count_documents({'score': {'$gt': your_score[0]["score"]}}) + 1
    return render_template('leaderboard.html' , scores = lb_scores, your_score=your_score[0],rank=rank)  # show the form

if __name__ == '__main__':
    app.run(debug=True)




