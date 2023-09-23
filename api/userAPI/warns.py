import api.databaseAPI.dbapi as DB

con = DB.getDatabase()
cur = con.cursor()

def getWarn(id: str) -> int|str:
    result = cur.execute(f"SELECT * FROM users WHERE identifier = '{id}'").fetchall()
    if not result:
        return "Cet utilisateur n'est pas enregistré dans la base de donnée !"
    else:
        return result[0][2]
    
def addWarn(id: str):
    warn = getWarn(id)
    if not isinstance(warn, int):
        return
    else:
        warn += 1
        try:
            cur.execute(f"UPDATE users SET warn = {warn} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    return


def removeWarn(id: str, number: int):
    warn = getWarn(id)
    if not isinstance(warn, int):
        return
    if number > warn:
        act = warn - warn
        try:
            cur.execute(f"UPDATE users SET warn = {act} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    else:
        act = warn - number
        try:
            cur.execute(f"UPDATE users SET warn = {act} WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    return











