import interactions
from utils.embed import create_embed
from utils.user_utils import *
import api.userAPI.onJoin as joinAPI
import api.userAPI.warns as warnAPI




class Getwarn(interactions.Extension):
    @interactions.extension_command(name="getwarn", description="permet de voir le nombre d'avertissements d'un utilisateur",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                 [
                     interactions.Option(
                         name="username",
                         description="Nom d'utilisateur demandé",
                         type=interactions.OptionType.USER,
                         required=True,
                     )
                 ])
    async def getwarn(self,ctx: interactions.CommandContext, username: interactions.Member):
        joinAPI.save(username.id)
        await ctx.send(f"L'utilisateur <@{username.id}> à {warnAPI.getWarn(username.id)} avertissement(s)", ephemeral=True)


def setup(client: interactions.Client):
    Getwarn(client)