from flask import Flask, render_template, request
from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import datetime

uri = "mongodb+srv://Atriays:VRkDtlmnmxyYnQZM@do-bhai-banayenge-games.bmuo0ev.mongodb.net/?retryWrites=true&w=majority&appName=do-bhai-banayenge-games"

myclient = MongoClient(uri, server_api=ServerApi('1'))

db_name = "games_all"
table_name = "flappy_leaderboard"

mydb = myclient[db_name]
flappy_table = mydb[table_name]


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
    

time_of_score = datetime.datetime.now().strftime("%d %b %Y  %I:%M %p")
lb_trial = {"name" : "abcd" , "score" : 1223, "date_time" : time_of_score}
def ins():
    insert_id = flappy_table.insert_one(lb_trial)
    print(insert_id)

query = {"name": "abc"}




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
    lb_scores = flappy_table.find().sort("score",pymongo.DESCENDING)
    return render_template('leaderboard.html' , scores = lb_scores)  # show the form

if __name__ == '__main__':
    app.run(debug=True)




