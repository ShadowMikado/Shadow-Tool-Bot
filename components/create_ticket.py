import interactions
from utils.embed import *
from utils.user_utils import *


class Create_ticket(interactions.Extension):
    @interactions.extension_component("create_ticket")
    async def on_click(self,ctx: interactions.ComponentContext):
        Embed = create_embed(
            title=f"Ticket de {ctx.author.name}",
            description=f"Un Staff va s'occuper de votre ticket très rapidement, veuillez patienter",
            color=0x0000FF
        )
        button1 = interactions.Button(
            custom_id="remove_ticket",
            style=interactions.ButtonStyle.DANGER,
            label="Close Ticket",
            emoji=interactions.Emoji(
                name='🔒'
            )

        )
        button2 = interactions.Button(
            custom_id="claim_ticket",
            style=interactions.ButtonStyle.SECONDARY,
            label="Claim Ticket",
            emoji=interactions.Emoji(
                name='🖐'
            )

        )
        guild = ctx.guild
        if getTicketId(ctx.author.id) != 0:
            await ctx.send(f"Vous avez déja un ticket ! (<#{getTicketId(ctx.author.id)}>)", ephemeral=True)
        else:
            channel = await guild.create_channel(f"ticket - {ctx.author.name}",
                                                 type=interactions.ChannelType.GUILD_TEXT,

                                                 permission_overwrites=[interactions.Overwrite(
                                                     id=int(ctx.author.id),
                                                     type=1,
                                                     allow=interactions.Permissions.VIEW_CHANNEL | interactions.Permissions.SEND_MESSAGES | interactions.Permissions.ATTACH_FILES
                                                 )])

            await channel.send(embeds=Embed, components=[button1, button2])
            await ctx.send(f"Vous avez bien créé un ticket ! (<#{int(channel.id)}>)", ephemeral=True)
            addTicket(ctx.author.id, int(channel.id))

def setup(client: interactions.Client):
    Create_ticket(client)