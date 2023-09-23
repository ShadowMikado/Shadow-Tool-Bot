import datetime
import interactions
from utils.embed import create_embed
from utils.time_to_epoch import *
from utils.user_utils import *


class Ticket(interactions.Extension):
    @interactions.extension_command(name="ticket", description='Créer un ticket',
                                    default_member_permissions=interactions.Permissions.ADMINISTRATOR)
    async def ticket(self, ctx: interactions.CommandContext):
        Embed = create_embed(
            title="Créer un Ticket!",
            color=0x0000FF
        )
        button1 = interactions.Button(
            custom_id="create_ticket",
            style=interactions.ButtonStyle.PRIMARY,
            label="Ticket !",
            emoji=interactions.Emoji(
                name='🔓'
            )
        )
        await ctx.send("", embeds=Embed, ephemeral=False, components=button1)


def setup(client: interactions.Client):
    Ticket(client)
