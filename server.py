from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask import Flask, flash, redirect, render_template, request, session, abort
from json import dumps
import os
from sqlalchemy.orm import sessionmaker
from tablelogin import *
import pandas as pd

engine = create_engine('sqlite:///logindata.db', echo=True)
db_connect = create_engine('sqlite:///imdb.db')
app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss! you are logout"


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template('movies.html')
    else:
        flash('wrong password!')
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/movies",methods=['POST'])
#class Movies(Resource):
#    def get(self):
def movies():
    conn = db_connect.connect()  # connect to database
    query = conn.execute("SELECT * FROM MOVIES; ")  # This line performs query and returns json result
    return {'movies': [i[1] for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID




@app.route("/moviesid",methods=['POST'])
#class Movies_Name(Resource):
#    def get(self, ID):
def moviesid():
    ID = str(request.form['id'])
    conn = db_connect.connect()
    query = conn.execute("select * from MOVIES where ID =%d" %int(ID))
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)
@app.route("/sortbyname",methods=['POST'])
#class sortbyname(Resource):
#    def get(self):
def sortbyname():
    conn = db_connect.connect()
    query = conn.execute("select * from MOVIES ORDER BY TITLE ASC")
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)
@app.route("/sortbyrating",methods=['POST'])
#class sortbyrating(Resource):
#    def get(self):
def sortbyrating():
    conn = db_connect.connect()
    query = conn.execute("select * from MOVIES ORDER BY RATING DESC")
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)
@app.route("/sortbyrd",methods=['POST'])
def sortbyrd():
    conn = db_connect.connect()
    query = conn.execute("select * from MOVIES ORDER BY RELEASEDATE ASC")
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)
@app.route("/sortbyduration",methods=['POST'])
def sortbyduration():
    conn = db_connect.connect()
    query = conn.execute("select * from MOVIES ORDER BY DURATION ASC")
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)



@app.route("/search",methods=['POST'])
#class Search(Resource):
#    def get(self, data):
def search():
    data=str(request.form['data'])
    conn = db_connect.connect()
    query = conn.execute("select * from MOVIES where TITLE OR DESCRIPTION LIKE ? ",("%"+data+"%",))
        #sql="""select * from MOVIES where TITLE LIKE '%'+{}+'%'""".format(data)
        #newquery=pd.read_sql_query(sql,conn)
        #print(newquery)
    print("hello")
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)
#api.add_resource(Movies, '/movies')  # Route_1

#api.add_resource(Movies_Name, '/movies/<ID>')  # Route_3
#api.add_resource(sortbyname,'/sortbyname')
#api.add_resource(sortbyrating,'/sortbyrating')
#api.add_resource(sortbyduration,'/sortbyduration')
#api.add_resource(Search, '/search/<data>')
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)