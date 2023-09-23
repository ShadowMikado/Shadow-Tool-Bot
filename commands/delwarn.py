import interactions
from utils.embed import create_embed
from utils.user_utils import *
import api.userAPI.onJoin as joinAPI
import api.userAPI.warns as warnAPI



class Delwarn(interactions.Extension):
    @interactions.extension_command(name="delwarn", description="permet de supprimer un nombre d'avertissements d'un utilisateur",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                 [
                     interactions.Option(
                         name="username",
                         description="Nom d'utilisateur demandé",
                         type=interactions.OptionType.USER,
                         required=True,
                     ),
                     interactions.Option(
                         name="number",
                         description="Nombre de warn a retirer",
                         type=interactions.OptionType.INTEGER,
                         required=True,
                     )
                 ])
    async def delwarn(self,ctx: interactions.CommandContext, username: interactions.Member, number: int):
        joinAPI.save(username.id)
        warnAPI.removeWarn(username.id, number)
        await ctx.send(
            f"Vous avez bien retiré {number} avertissement(s) à <@{username.id}>, il a maintenant {warnAPI.getWarn(username.id)} avertissement(s)",
            ephemeral=True)


def setup(client: interactions.Client):
    Delwarn(client)