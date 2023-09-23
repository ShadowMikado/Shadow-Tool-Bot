import os
import interactions
import json
import requests
from utils.user_utils import *
from utils.config import config
import api.userAPI.onJoin as joinAPI

token = f"{config('Token')}"
version = requests.get("https://raw.githubusercontent.com/ShadowMikado/Shadow-Tool-Bot/main/infos.json").json()[
    "version"]
status = requests.get("https://raw.githubusercontent.com/ShadowMikado/Shadow-Tool-Bot/main/infos.json").json()["status"]
bot = interactions.Client(token=token, intents=interactions.Intents.ALL)

saveUser("Null")

debug = config("Debug")

def load(path):
    loads = []
    loads_count = 0
    for filename in os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{path}")):
        if filename.startswith("__pycache__"): continue
        if filename.startswith("changestatus"): continue
        if filename.endswith(".py"):
            loads.append(filename.replace(".py", ""))
            loads_count += 1
        if debug:
            print(f"✅ {filename.replace('.py', '')}")

    print(f"\n{loads_count} {path} loaded !\n")
    [bot.load(f"{path}." + load) for load in loads]
    return

@bot.event
async def on_ready():
    print(f"Enregistré en tant que: {bot.me.name}#(ID: {bot.me.id}) Version {version}")
    print(f"La latence est de {round(bot.latency)} ms.")
    print(f"\nLe bot est sur le serveur: ")
    for guild in bot.guilds:
        print(f"{guild.name} Id: {guild.id}")
        members = await guild.get_all_members()
        for member in members:
            joinAPI.save(member.id)
            # print(member.name, member.id)
            # isSaved(member.id)

load("commands")
load("components")
load("events")


bot.start()

