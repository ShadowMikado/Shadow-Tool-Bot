import api.databaseAPI.dbapi as DB
import sqlite3


con = DB.getDatabase()
cur = con.cursor()

def getChatGptTry(id: str) -> int|str:
    result = cur.execute(f"SELECT * FROM users WHERE identifier = '{id}'").fetchall()
    if not result:
        return "Cet utilisateur n'est pas enregistré dans la base de donnée !"
    else:
        return result[0][3]
    
def addChatGptTry(id: str):
    gptTry = getChatGptTry(id)
    if not isinstance(gptTry, int):
        return
    else:
        gptTry += 1
        try:
            cur.execute(f"UPDATE users SET warn = {gptTry} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    return

def removeChatGptTry(id: str, number: int):
    gptTry = getChatGptTry(id)
    if not isinstance(gptTry, int):
        return
    if number > gptTry:
        act = gptTry - gptTry
        try:
            cur.execute(f"UPDATE users SET warn = {act} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    else:
        act = gptTry - number
        try:
            cur.execute(f"UPDATE users SET warn = {act} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    return
