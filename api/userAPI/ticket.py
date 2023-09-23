import api.databaseAPI.dbapi as DB

con = DB.getDatabase()
cur = con.cursor()


def getTicketId(id: str) -> int|str|None:
    result = cur.execute(f"SELECT * FROM users WHERE identifier = '{id}'").fetchall()
    if not result:
        return "Cet utilisateur n'est pas enregistré dans la base de donnée !"
    else:
        if hasTicket(id):
            return result[0][5]
        else:
            return result[0][5]
    
def setTicket(id: str, ticket: str):
    if not hasTicket(id):
        try: 
            cur.execute(f"UPDATE users SET ticket_id = '{ticket}' WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    else:
        print(f"User {id} as already a ticket ({ticket})")


def removeTicket(id: str):
    if hasTicket(id):
        try: 
            cur.execute(f"UPDATE users SET ticket_id = NULL WHERE identifier = {id}")
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    else:
        print(f"User {id} doesn't have a ticket yet")

def hasTicket(id: str) -> bool:
    result = cur.execute(f"SELECT * FROM users WHERE identifier = '{id}'").fetchall()
    if result[0][5] is None:
        return False
    else:
        return True
