import interactions
from utils.embed import create_embed
from utils.config import config

muteId = config('Mute Id')
cmdError = config('Commands Error')
class Unmute(interactions.Extension):

    @interactions.extension_command(name="unmute", description="permet de supprimer le mute d'un utilisateur",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=[
            interactions.Option(
                name="username",
                description="Nom d'utilisateur demandé",
                type=interactions.OptionType.USER,
                required=True,
            )])
    async def unmute(self,ctx: interactions.CommandContext, username: interactions.Member):
        # await ctx.send(f"{username}")

        if muteId in username.roles:
            await username.remove_role(role=muteId)
            await ctx.send(f"Vous avez bien supprimé le mute de <@{username.id}>", ephemeral=True)
        else:
            await ctx.send(f"L'utilisateur <@{username.id}> n'est pas muet!", ephemeral=True)

def setup(client: interactions.Client):
    Unmute(client)