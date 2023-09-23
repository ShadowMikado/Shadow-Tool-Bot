import interactions
from utils.embed import create_embed



class Avatar(interactions.Extension):
    @interactions.extension_command(name="avatar", description="permet de voir l'avatar' d'un utilisateur", options=
    [

        interactions.Option(
            name="username",
            description="Nom de l'utilisateur demandé",
            type=interactions.OptionType.USER,
            required=True,
        )
    ])
    async def avatar(self,ctx: interactions.CommandContext, username: interactions.Member):
        authoravatar = f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.webp?size=128"
        memberavatar = f"https://cdn.discordapp.com/avatars/{username.id}/{username.avatar}.webp?size=512"
        Embed = create_embed(
            title=f"",
            color=0x0000FF,
            image=memberavatar,
            include_author=True,
            # author_icon_url=memberavatar,
            author_name=f"Avatar de {username.user.username}#{username.user.discriminator}",
            footer_text=f"Demandé par {ctx.user.username}#{ctx.user.discriminator}",
            footer_image=authoravatar
        )

        await ctx.send(embeds=Embed)


def setup(client: interactions.Client):
    Avatar(client)