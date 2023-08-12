import sqlite3

def connect():
    connection = sqlite3.connect("conspect.db")
    print(connection.total_changes)
