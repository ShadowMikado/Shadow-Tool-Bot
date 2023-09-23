import interactions
from utils.embed import create_embed
from utils.user_utils import *



class Ping(interactions.Extension):
    @interactions.extension_command(name="ping", description="permet de voir la latence du bot")
    async def ping(self,ctx: interactions.CommandContext):
        await ctx.send(f"La latence du bot est de {round(self.client.latency)} ms",ephemeral=True)


def setup(client: interactions.Client):
    Ping(client)