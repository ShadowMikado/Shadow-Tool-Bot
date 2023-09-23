import api.databaseAPI.dbapi as DB
import sqlite3

con = DB.getDatabase() #sqlite3.connect(f"./database/database.sqlite")
cur = con.cursor()


def isSaved(id: str) -> bool:
    result = cur.execute(f"SELECT * FROM users WHERE identifier = '{id}'").fetchall()
    if not result:
        return False
    else:
        return True
    
def save(id: str):
    if not isSaved(id):
        try:
            cur.execute("INSERT INTO users (identifier, warn, chatgpt, dalle) VALUES (?, 0, 0, 0)", (id,))
            con.commit()
            print(f"Saved user {id}")
        except Exception as e:
            con.rollback()
            print(e)
    else:
        print(f"User {id} is already saved !")
    return