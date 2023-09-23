import interactions
from utils.embed import create_embed
from utils.user_utils import *



class Purge(interactions.Extension):
    @interactions.extension_command(name="purge", description="permet de supprimer un nombre de message donné",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                 [
                     interactions.Option(
                         name="number",
                         description="Nombre de message à supprimer",
                         type=interactions.OptionType.INTEGER,
                         required=True,
                     ),
                     interactions.Option(
                         name="channel",
                         description="Salon demandé",
                         type=interactions.OptionType.CHANNEL,
                         required=False,
                     )
                 ])
    async def purge(self,ctx: interactions.CommandContext, number: int, channel: interactions.Channel = None):
        if channel:
            await channel.purge(amount=number)
            await ctx.send(f"{number} messages ont été supprimés dans le salon <#{channel.id}>", ephemeral=True)

        else:
            await ctx.channel.purge(amount=number)
            await ctx.send(f"{number} messages ont été supprimés dans le salon <#{ctx.channel.id}>", ephemeral=True)


def setup(client: interactions.Client):
    Purge(client)