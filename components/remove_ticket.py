import interactions
from utils.embed import *
from utils.user_utils import *


class Remove_ticket(interactions.Extension):
    @interactions.extension_component("remove_ticket")
    async def remove_ticket(self,ctx: interactions.ComponentContext):
        button1 = interactions.Button(
            custom_id="confirmation_remove_ticket",
            style=interactions.ButtonStyle.DANGER,
            label="Close Ticket",
            emoji=interactions.Emoji(
                name='🔒'
            )

        )
        await ctx.send("Êtes vous sur de vouloir fermer ce ticket ?", ephemeral=True, components=button1)


def setup(client: interactions.Client):
    Remove_ticket(client)