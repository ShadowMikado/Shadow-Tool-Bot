import interactions

from utils.config import config
from utils.embed import create_embed
from utils.user_utils import *
import requests


class Say(interactions.Extension):
    @interactions.extension_command(name="say", description='Permet de faire dire quelque chose au bot', options=
    [
        interactions.Option(
            name="words",
            description="Mot à faire dire au bot",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="webhook",
            description="Avec Webhook ?",
            type=interactions.OptionType.BOOLEAN,
            required=False,
        )

    ])
    async def say(self,ctx: interactions.CommandContext, words: str, webhook: bool = None):

        if webhook and webhook == True:
            await ctx.defer(ephemeral=True)

            webhook = await interactions.Webhook.create(channel_id=int(ctx.channel_id),
                                                        name=str(ctx.author.username), client=self.client._http)
            url = f"https://discord.com/api/webhooks/{webhook.id}/{webhook.token}"
            content = str(words)

            requests.post(url, json={
                "avatar_url": f"{ctx.author.avatar_url}",
                "content": f"{content}"
            })

            await webhook.delete()
            await ctx.send("Vous avez bien envoyé un webhook !", ephemeral=True)

        elif webhook and webhook == False:
            await ctx.send(str(words))

        else:
            await ctx.send(str(words))

def setup(client: interactions.Client):
    Say(client)