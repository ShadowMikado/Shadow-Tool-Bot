import asyncio
import random
import interactions
import requests


async def change(nb, client: interactions.Client = interactions.Client):
    version = requests.get("https://raw.githubusercontent.com/ShadowMikado/Shadow-Tool-Bot/main/infos.json").json()["version"]
    status = requests.get("https://raw.githubusercontent.com/ShadowMikado/Shadow-Tool-Bot/main/infos.json").json()["status"]

    guilds_nb = 0
    for n in client.guilds:
        guilds_nb += 1

    member_nb = 0
    for a in client.guilds:
        mem = await a.get_all_members()
        for z in mem:
            member_nb += 1

    pr1 = interactions.ClientPresence(
        status=interactions.StatusType.ONLINE,
        activities=[
            interactions.PresenceActivity(name=f"{guilds_nb} Serveurs !",
                                          type=interactions.PresenceActivityType.WATCHING)
        ]
    )

    pr2 = interactions.ClientPresence(
        status=interactions.StatusType.ONLINE,
        activities=[
            interactions.PresenceActivity(name=f"{member_nb} Membres !",
                                          type=interactions.PresenceActivityType.WATCHING)
        ]
    )

    pr3 = interactions.ClientPresence(
        status=interactions.StatusType.ONLINE,
        activities=[
            interactions.PresenceActivity(name=f"{status} | v{version}",
                                          type=interactions.PresenceActivityType.GAME)
        ]
    )

    pr4 = interactions.ClientPresence(
        status=interactions.StatusType.ONLINE,
        activities=[
            interactions.PresenceActivity(name=f"/help",
                                          type=interactions.PresenceActivityType.GAME)
        ]
    )

    pr5 = interactions.ClientPresence(
        status=interactions.StatusType.ONLINE,
        activities=[
            interactions.PresenceActivity(name=f"AntiRaid",
                                          type=interactions.PresenceActivityType.STREAMING)
        ]
    )

    pr6 = interactions.ClientPresence(
        status=interactions.StatusType.ONLINE,
        activities=[
            interactions.PresenceActivity(name=f"ShadowMikado",
                                          type=interactions.PresenceActivityType.LISTENING)
        ]
    )
    rand = [pr1, pr2, pr3, pr4, pr5, pr6]
    await client.change_presence(random.choice(rand))
    await asyncio.sleep(30)



class Changestatus(interactions.Extension):
    @interactions.extension_listener(name="on_start")
    async def change2(self):
        tasks = [asyncio.create_task(change(i)) for i in range(1051300)]
        for task in tasks:
            await task


def setup(client: interactions.Client):
    Changestatus(client)
