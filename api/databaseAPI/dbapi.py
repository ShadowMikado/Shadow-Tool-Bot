import sqlite3

dbname = "database.sqlite"

# sqlite3.connect(f"../../database/{dbname}");


def getDatabase() -> sqlite3.Connection:
    return sqlite3.connect(f"./database/{dbname}")


def getCursor() -> sqlite3.Cursor:
    return getDatabase().cursor()



