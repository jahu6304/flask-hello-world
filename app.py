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

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgresql://jhello_user:77TALs6OnzU517oI6xqY1xWhaMCuebsA@dpg-cves002n91rc73apnhp0-a/jhello")
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                Values
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated Successfully"

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgresql://jhello_user:77TALs6OnzU517oI6xqY1xWhaMCuebsA@dpg-cves002n91rc73apnhp0-a/jhello")
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM Basketball;
                ''')
    
    #capture results of query
    records = cur.fetchall()
    conn.close()
    table_html_build = "<table>"
    for player_row in records:
        response_string += "<tr>"
        for info_column in player_row:
            table_html_build += "<td>{}</td>".format(info)
        table_html_build += "</tr>"
    table_html_build += "</table>"
    return table_html_build