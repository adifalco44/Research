# -*- coding: utf-8 -*-
"""
    First Flask db Demo
    ~~~~~~~~

    A program that reads in a hard-coded static db and retrieves via qeuery

"""
import os, string
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash


# configuration
DATABASE = '/tmp/index.db'
#PER_PAGE = 30
#DEBUG = True
#SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

app = Flask('first')
app.config.from_object(__name__)
#app.config.from_envvar('MINITWIT_SETTINGS', silent=True)


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db


@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    print('db Initialized')
    db.execute('insert into Students (Student_id, First, Last) values (?, ?, ?)',
              [1,"Brandon","RichardWebster"])
    db.commit()
    db.execute('insert into Students (Student_id, First, Last) values (?, ?, ?)',
              [2,"Joel","Brogan"])
    db.commit()
    db.execute('insert into Students (Student_id, First, Last) values (?, ?, ?)',
              [3,"Andrey","Kuekhamp"])
    db.commit()
    db.execute('insert into Classes (Class_id, Name, Credits) values (?, ?, ?)',
              [1,"Databases",3])
    db.commit()
    db.execute('insert into Classes (Class_id, Name, Credits) values (?, ?, ?)',
              [2,"Algorithms",4])
    db.commit()
    db.execute('insert into Classes (Class_id, Name, Credits) values (?, ?, ?)',
              [3,"Operating Systems",4])
    db.commit()
    db.execute('insert into Schedule (Schedule_id, Students_id, Class_id) values (?, ?, ?)',
              [1,1,1])
    db.commit()
    db.execute('insert into Schedule (Schedule_id, Students_id, Class_id) values (?, ?, ?)',
              [2,1,3])
    db.commit()
    db.execute('insert into Schedule (Schedule_id, Students_id, Class_id) values (?, ?, ?)',
              [3,2,2])
    db.commit()
    db.execute('insert into Schedule (Schedule_id, Students_id, Class_id) values (?, ?, ?)',
              [4,3,1])
    db.commit()
    db.execute('insert into Schedule (Schedule_id, Students_id, Class_id) values (?, ?, ?)',
              [5,3,2])
    db.commit()
    db.execute('insert into Schedule (Schedule_id, Students_id, Class_id) values (?, ?, ?)',
              [6,3,3])
    db.commit()
    print('DB udpated')

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()

    print('Initialized the database.')

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv

@app.route('/Students')
def students_page():
    db = get_db()
    query = query_db('''select * from Students''')
    return render_template('Students.html',data=query)

@app.route('/Classes')
def classes_page():
    db = get_db()
    query = query_db('''select * from Classes''')
    return render_template('Classes.html',data=query)

@app.route('/Schedule')
def schedule_page():
    db = get_db()
    query = query_db('''select * from Schedule''')
    return render_template('Schedule.html',data=query)

@app.route('/AppendDB',methods=['GET','POST'])
def append_db_page():
        if request.method == 'GET':
            return render_template('Append_Db.html')
        if request.method == 'POST':
            db = get_db()
            db.execute('''insert into Classes (Class_id,Name,Credits) values (?,?,?)''',
                    [request.form['Class_id'],request.form['Name'],request.form['Credits']])
            db.commit()

@app.route('/Results')
def watchman():
    csv_file = 'first/temp.csv'
    db = get_db()
    print("In watchman")
    class_id = []
    name = []
    credits = []
    with open(csv_file,"r+") as file_desc:
        i = 0
        for line in file_desc:
            if (i==0):
                class_id = line.split(',')
            if (i==1):
                name = line.split(',')
            if(i==2):
                credits = line.split(',')
            i=i+1
    for i in range(0,len(class_id)):
        db.execute('insert into Classes (Class_id,Name,Credits) values (?,?,?)',
                    [int(class_id[int(i)]),str(name[int(i)]),int(credits[int(i)])])
        db.commit()
    os.remove(csv_file)
    print("Database successfully updated")
    query = query_db('''select * from Classes''')
    return render_template('Classes.html',data=query)

