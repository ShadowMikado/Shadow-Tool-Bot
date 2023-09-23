import interactions
from utils.embed import create_embed



class Roles(interactions.Extension):
    @interactions.extension_command(name="roles", description="permet de voir tous les rôles du serveur")
    async def roles(self,ctx: interactions.CommandContext):
        authoravatar = f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.webp?size=128"
        Embed = create_embed(
            title=f"",
            description="",
            color=0x0000FF,
            include_thumbnail=True,
            footer_text=f"Demandé par {ctx.user.username}#{ctx.user.discriminator}",
            footer_image=authoravatar
        )
        roles = []
        for role in ctx.guild.roles:
            roles.append(f"<@&{role.id}>\n")
        # print(' '.join(roles))
        Embed.add_field("**Rôles :**", ''.join(roles))

        await ctx.send(embeds=Embed)


def setup(client: interactions.Client):
    Roles(client)