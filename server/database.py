import sqlite3
import datetime
from flask import g

import server


DATABASE = "server/database.db"
TABLE_NAME = "weight_values"

CREATE_TABLE_QUERY = """CREATE TABLE """ + TABLE_NAME + """ (
    hour int,
    minute int,
    second int,
    day int,
    month int,
    year int,
    weight float,
	PRIMARY KEY("hour","minute","day","month","second","year")
    )"""

ADD_WEIGHT_VALUE_QUERY = """INSERT INTO """ + TABLE_NAME + """
    (hour, minute, second, day, month, year, weight)
    VALUES
    (?, ?, ?, ?, ?, ?, ?)
    """

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    try:
        cur = db.cursor()
        cur.execute(CREATE_TABLE_QUERY)
        db.commit()
    except sqlite3.OperationalError as ope:
        print("sqlite3.OperationalError: ", ope)
        print("The weight table seems to already exist.\nOther errors should not be ignored")
    return db

@server.flask_server.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
    
def insert_weight(weight):
    con = get_db()
    cur = con.cursor()
    time = datetime.datetime.now()
    entry = (time.hour, time.minute, time.second, time.day, time.month, time.year, weight)
    cur.execute(ADD_WEIGHT_VALUE_QUERY, entry)
    con.commit()

