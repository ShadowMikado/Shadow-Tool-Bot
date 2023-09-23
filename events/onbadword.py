import random

import interactions
import requests

from utils.config import config
from utils.user_utils import *

banned2 = config('Banned Words')


class Onbadword(interactions.Extension):
    @interactions.extension_listener(name="on_message_create")
    async def onBadWord(self, message: interactions.Message):
        banned = banned2
        # banned = ["discord.gg/","dsc.gg/","https://discord.gg/",".gg/","https://dsc.gg/"]
        if message.author.bot: return
        #for guild in self.client.guilds:
            #if message.author.id == guild.owner_id: return
            #if message.author.id == 783739472079880243:
             #await message.member.remove_role(989607801812844634)
            # await message.member.add_role(990680856446242888)
        for i in banned:
            if message.content.find(f"{i}") != -1:
                if "/" in message.content:
                    content_string = message.content.split(i)[1]

                    msg = i + content_string.split()[0]
                    count = len(msg)
                    l = r"#?æ£%ß&!@€"
                    rdm = ''.join([random.choice(l) for i in range(count)])

                    webhook = await interactions.Webhook.create(channel_id=int(message.channel_id),
                                                                name=str(message.author.username),
                                                                client=self.client._http)
                    url = f"https://discord.com/api/webhooks/{webhook.id}/{webhook.token}"
                    content = message.content.replace(msg, f"`{rdm}`")

                    requests.post(url, json={
                        "avatar_url": f"{message.author.avatar_url}",
                        "content": f"{content}"
                    })

                    await webhook.delete()
                    await message.delete()

                    await message.author.send(
                        f"Vous n'avez pas le droit d'envoyer des messages de type `{i}` <@{message.author.id}>")
                    isSaved(message.author.id)
                    addWarn(message.author.id)
                    # await message.reply(f"Vous n'avez pas le droit d'envoyer des messages de type `{i}` <@{message.author.id}>")
                    print(f"Message de {message.author.username}: {message.content}")
                else:
                    count = len(i)
                    l = r"#?æ£%ß&!@€"
                    rdm = ''.join([random.choice(l) for i in range(count)])
                    webhook = await interactions.Webhook.create(channel_id=int(message.channel_id),
                                                                name=str(message.author.username),
                                                                client=self.client._http)
                    url = f"https://discord.com/api/webhooks/{webhook.id}/{webhook.token}"
                    content = message.content.replace(i, f"`{rdm}`")

                    requests.post(url, json={
                        "avatar_url": f"{message.author.avatar_url}",
                        "content": f"{content}"
                    })

                    await webhook.delete()
                    await message.delete()

                    await message.author.send(
                        f"Vous n'avez pas le droit d'envoyer des messages de type `{i}` <@{message.author.id}>")
                    isSaved(message.author.id)
                    addWarn(message.author.id)
                    # await message.reply(f"Vous n'avez pas le droit d'envoyer des messages de type `{i}` <@{message.author.id}>")
                    print(f"Message de {message.author.username}: {message.content}")


def setup(client: interactions.Client):
    Onbadword(client)
