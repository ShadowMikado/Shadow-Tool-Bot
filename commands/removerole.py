import interactions
from utils.embed import create_embed
from utils.config import config

muteId = config('Mute Id')
cmdError = config('Commands Error')
class Removerole(interactions.Extension):

    @interactions.extension_command(name="removerole", description="permet d'enlever un rôle a un utilisateur",
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
                         required=False,
                     )
                 ])
    async def removerole(self,ctx: interactions.CommandContext, username: interactions.Member,
                         role: interactions.Role = None):
        aaa = []
        for role1 in username.roles:
            aaa.append(role1)
        print(aaa)

        if role != None and int(role.id) in aaa:
            await username.remove_role(int(role.id))
            await ctx.send(f"Vous avez retiré le rôle <@&{role.id}> à <@{username.id}>", ephemeral=True)
        elif role == None:
            for role2 in aaa:
                await username.remove_role(int(role2))
            await ctx.send(f"Vous avez enlevé tout les roles de <@{username.id}>", ephemeral=True)
        else:
            await ctx.send(f"L'utilisateur <@{username.id}> ne possède pas le rôle <@&{role.id}>", ephemeral=True)


def setup(client: interactions.Client):
    Removerole(client)