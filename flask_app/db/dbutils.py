import sqlite3, os
from flask import g

DATABASE = 'a_really_notable.db'


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def delete_old_db():
	""" We start with a fresh db everytime """
	if os.path.isfile(DATABASE):
		os.remove(DATABASE)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv



def exec_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    get_db().commit()
    cur.close()
