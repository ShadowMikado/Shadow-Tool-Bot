import api.databaseAPI.dbapi as DB
import sqlite3


con = DB.getDatabase()
cur = con.cursor()

def getDallETry(id: str) -> int|str:
    result = cur.execute(f"SELECT * FROM users WHERE identifier = '{id}'").fetchall()
    if not result:
        return "Cet utilisateur n'est pas enregistré dans la base de donnée !"
    else:
        return result[0][4]
    
def addDallETry(id: str):
    dalleTry = getDallETry(id)
    if not isinstance(dalleTry, int):
        return
    else:
        dalleTry += 1
        try:
            cur.execute(f"UPDATE users SET warn = {dalleTry} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    return

def removeDallETry(id: str, number: int):
    dalleTry = getDallETry(id)
    if not isinstance(dalleTry, int):
        return
    if number > dalleTry:
        act = dalleTry - dalleTry
        try:
            cur.execute(f"UPDATE users SET warn = {act} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    else:
        act = dalleTry - number
        try:
            cur.execute(f"UPDATE users SET warn = {act} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    return
