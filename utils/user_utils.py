import json

def saveUser(id):
    with open("./users_datas.json", "r") as users_datas:
        try:
            data = json.load(users_datas)
        except json.JSONDecodeError:
            data = {}
    data[str(id)] = {'warn': 0,'ticket':{'number':0,'id':0},'AI':{'chat_gpt':0,'dall_e':0}}

    with open("./users_datas.json", "w") as users_datas:
        json.dump(data, users_datas, indent=4)
    return


def getWarn(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
    # print(datas[str(id)]["warn"])
    return data[str(id)]["warn"]


def addWarn(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        warn = getWarn(id)
        data[str(id)]["warn"] = warn + 1
    with open("./users_datas.json", "w") as users_datas:
        json.dump(data, users_datas, indent=4)
        users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return


def removeWarn(id, number: int):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        warn = getWarn(id)
        if number > warn:
            data[str(id)]["warn"] = warn - warn
        else:
            data[str(id)]["warn"] = warn - number
        with open("./users_datas.json", "w") as users_datas:
            json.dump(data, users_datas, indent=4)
            users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return



def getTicketNumber(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
    # print(datas[str(id)]["warn"])
    return data[str(id)]["ticket"]["number"]

def getTicketId(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
    # print(datas[str(id)]["warn"])
    return data[str(id)]["ticket"]["id"]

def addTicket(id,ticket_id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        ticket_number = getTicketNumber(id)
        data[str(id)]["ticket"]["number"] = ticket_number + 1
        data[str(id)]["ticket"]["id"] = ticket_id
    with open("./users_datas.json", "w") as users_datas:
        json.dump(data, users_datas, indent=4)
        users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return


def removeTicket(id, number: int):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        ticket = getTicketNumber(id)
        if number > ticket:
            data[str(id)]["ticket"]["number"] = ticket - ticket
            data[str(id)]["ticket"]["id"] = 0
        else:
            data[str(id)]["ticket"]["number"] = ticket - number
            data[str(id)]["ticket"]["id"] = 0
        with open("./users_datas.json", "w") as users_datas:
            json.dump(data, users_datas, indent=4)
            users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return

def hasTicket(id:int,channel_id:int):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        #print(data[str(id)]["ticket"]["id"])
        if channel_id == data[str(id)]["ticket"]['id']:
            return True
        else:
            return False




def isSaved(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        if str(id) in data:
            return
        else:
            saveUser(id)
    return


def getChatGptTry(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
    # print(datas[str(id)]["warn"])
    return data[str(id)]['AI']["chat_gpt"]


def addChatGptTry(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        chatgpttry = getChatGptTry(id)
        data[str(id)]['AI']["chat_gpt"] = chatgpttry + 1
    with open("./users_datas.json", "w") as users_datas:
        json.dump(data, users_datas, indent=4)
        users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return

def removeChatGptTry(id, number: int):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        chatgpttry = getChatGptTry(id)
        if number > chatgpttry:
            data[str(id)]['AI']["chat_gpt"] = chatgpttry - chatgpttry
        else:
            data[str(id)]['AI']["chat_gpt"] = chatgpttry - number
        with open("./users_datas.json", "w") as users_datas:
            json.dump(data, users_datas, indent=4)
            users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return

def getDalleTry(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
    # print(datas[str(id)]["warn"])
    return data[str(id)]['AI']["dall_e"]


def addDalleTry(id):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        dalletry = getDalleTry(id)
        data[str(id)]['AI']["dall_e"] = dalletry + 1
    with open("./users_datas.json", "w") as users_datas:
        json.dump(data, users_datas, indent=4)
        users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return

def removeDalleTry(id, number: int):
    with open("./users_datas.json") as users_datas:
        data = json.load(users_datas)
        dalletry = getDalleTry(id)
        if number > dalletry:
            data[str(id)]['AI']["dall_e"] = dalletry - dalletry
        else:
            data[str(id)]['AI']["dall_e"] = dalletry - number
        with open("./users_datas.json", "w") as users_datas:
            json.dump(data, users_datas, indent=4)
            users_datas.close()
        # json.dump(data,users_datas)
    # print(datas[str(id)]["warn"])
    return