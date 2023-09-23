import interactions
from utils.embed import create_embed
from utils.user_utils import *


class Warn(interactions.Extension):
    @interactions.extension_command(name="warn", description="permet d'avertir un utilisateur",
                                    default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=[
            interactions.Option(
                name="username",
                description="Nom d'utilisateur demandé",
                type=interactions.OptionType.USER,
                required=True,
            )])
    async def warn(self, ctx: interactions.CommandContext, username: interactions.Member):
        isSaved(username.id)
        addWarn(username.id)
        await ctx.send(
            f"Vous avez bien averti l'utilisateur <@{username.id}>, qui a maintenant {getWarn(username.id)} avertissement(s)",
            ephemeral=True)


def setup(client: interactions.Client):
    Warn(client)
