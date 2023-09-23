import interactions
from utils.embed import create_embed
from utils.config import config

muteId = config('Mute Id')
cmdError = config('Commands Error')
class Mute(interactions.Extension):

    @interactions.extension_command(name="mute", description="permet de rendre muet un utilisateur",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=[
            interactions.Option(
                name="username",
                description="Nom d'utilisateur demandé",
                type=interactions.OptionType.USER,
                required=True,
            )])
    async def mute(self,ctx: interactions.CommandContext, username: interactions.Member):
        await ctx.send(f"Vous avez bien rendu muet <@{username.id}>", ephemeral=True)
        await username.add_role(role=muteId)

def setup(client: interactions.Client):
    Mute(client)