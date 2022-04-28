from django import template
import sqlite3


register = template.Library()

def createConnections(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn


