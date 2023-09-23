import interactions
from utils.embed import create_embed
from utils.config import config

class Addrole(interactions.Extension):

    @interactions.extension_command(name="addrole", description="permet d'ajouter un rôle a un utilisateur",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                 [
                     interactions.Option(
                         name="username",
                         description="Nom d'utilisateur demandé",
                         type=interactions.OptionType.USER,
                         required=True,
                     ),
                     interactions.Option(
                         name="role",
                         description="Role",
                         type=interactions.OptionType.ROLE,
                         required=True,
                     )
                 ])
    async def addrole(self,ctx: interactions.CommandContext, username: interactions.Member, role: interactions.Role):
        await username.add_role(role.id)
        await ctx.send(f"Vous avez ajoué le rôle <@&{role.id}> à <@{username.id}>", ephemeral=True)


def setup(client: interactions.Client):
    Addrole(client)