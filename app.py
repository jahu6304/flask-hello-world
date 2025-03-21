from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from jahu6304 in 3308!'

@app.route('db_test')
def testing():
    conn = psycopg2.connect("postgresql://jhello_user:77TALs6OnzU517oI6xqY1xWhaMCuebsA@dpg-cves002n91rc73apnhp0-a/jhello")
    conn.close
    return "Database Connection Successful"