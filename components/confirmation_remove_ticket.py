import interactions

from utils.config import config
from utils.embed import *
from utils.user_utils import *

ticket_role_id = config("Ticket Access Role Id")
class Confirmation_remove_ticket(interactions.Extension):
    @interactions.extension_component("confirmation_remove_ticket")
    async def confirmation_remove_ticket(self,ctx: interactions.ComponentContext):
        guild = ctx.guild
        channel_id = getTicketId(ctx.author.id)
        for role_id in ticket_role_id:
            for role in ctx.author.roles:
                a = []
                a.append(role)
                if role_id in a:
                    await guild.delete_channel(int(ctx.channel_id))

        if hasTicket(int(ctx.author.id), int(ctx.channel_id)) == True:
            await guild.delete_channel(channel_id)
            removeTicket(ctx.author.id, 1)
        else:
            await ctx.send("Vous ne pouvez pas supprimer le ticket de quelqu'un !", ephemeral=True)


def setup(client: interactions.Client):
    Confirmation_remove_ticket(client)