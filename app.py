from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from jahu6304 in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://jhello_user:77TALs6OnzU517oI6xqY1xWhaMCuebsA@dpg-cves002n91rc73apnhp0-a/jhello")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgresql://jhello_user:77TALs6OnzU517oI6xqY1xWhaMCuebsA@dpg-cves002n91rc73apnhp0-a/jhello")
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Basketball(
                    First varchar(255),
                    Last varchar(255),
                    City varchar(255),
                    Name varchar(255),
                    Number Int                
                    );
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"