import interactions
from utils.embed import *
from utils.user_utils import *


class Claim_ticket(interactions.Extension):
    @interactions.extension_component("claim_ticket")
    async def remove_ticket(ctx: interactions.ComponentContext):
        if ctx.author.permissions.ADMINISTRATOR:
            addTicket(int(ctx.author.id), int(ctx.channel_id))
            await ctx.send("Vous avez bien Claim le ticket", ephemeral=True)
        else:
            await ctx.send("Vous ne pouvez pas Claim ce ticket !", ephemeral=True)


def setup(client: interactions.Client):
    Claim_ticket(client)