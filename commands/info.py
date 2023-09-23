import interactions
from utils.embed import create_embed
from utils.time_to_epoch import *
from utils.user_utils import *


tz = tz()
class Info(interactions.Extension):
    @interactions.extension_command(name="info", description="permet de voir les informations d'un utilisateur", options=
    [
        interactions.Option(
            name="username",
            description="Nom de l'utilisateur demandé",
            type=interactions.OptionType.USER,
            required=True,
        )
    ])
    async def info(self,ctx: interactions.CommandContext, username: interactions.Member):
        authoravatar = f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.webp?size=128"
        memberavatar = f"https://cdn.discordapp.com/avatars/{username.id}/{username.avatar}.webp?size=128"
        Embed = create_embed(
            title=f"",
            include_author=True,
            author_icon_url=memberavatar,
            author_name=f"{username.user.username}#{username.user.discriminator} ({username.id})",
            description="",
            color=0x0000FF,
            include_thumbnail=True,
            thumbnail=memberavatar,
            footer_text=f"Demandé par {ctx.user.username}#{ctx.user.discriminator}",
            footer_image=authoravatar
        )
        roles = []
        for role in username.roles:
            roles.append(f"<@&{role}>")
        # joinat = username.joined_at.strftime('%d/%m/%Y')
        joinat = time_to_epoch(username.joined_at.year, username.joined_at.month, username.joined_at.day,
                               username.joined_at.hour, username.joined_at.minute, tz)
        createat = time_to_epoch(username.user.created_at.year, username.user.created_at.month,
                                 username.user.created_at.day, username.user.created_at.hour,
                                 username.user.created_at.minute, tz)
        warns = getWarn(username.id)
        Embed.add_field("**Rôles :**", ' '.join(roles))
        Embed.add_field(f"**Membre Depuis :**", f"<t:{str(joinat)}:D>")
        Embed.add_field(f"**Compte Créé Le :**", f"<t:{str(createat)}:D>")
        Embed.add_field("**Nombre De Warns :**", warns)

        await ctx.send(embeds=Embed)

def setup(client: interactions.Client):
    Info(client)