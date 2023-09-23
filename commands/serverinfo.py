import interactions
from utils.embed import create_embed
from utils.time_to_epoch import *

tz = tz()
class Serverinfo(interactions.Extension):
    @interactions.extension_command(name="serverinfo", description="Permet de voir les informations du serveur")
    async def serverinfo(self,ctx: interactions.CommandContext):
        guild = ctx.guild
        # guild2 = await get(client=bot,obj=interactions.Guild,object_id=int(guild.id))
        guild_avatar = guild.icon_url
        emojis = guild.emojis
        emoji_nb = 0
        owner = guild.owner_id
        channels = guild.channels
        channel_nb = 0
        roles = guild.roles
        role_nb = 0
        members = guild.members
        member_nb = 0
        online = "En Dev"
        # online = await guild2.approximate_presence_count

        Embed = create_embed(
            # title=f"Information de {guild.name} ({guild.id})",
            include_author=True,
            author_name=f"Information de {guild.name} ({guild.id})",
            include_thumbnail=True,
            thumbnail=f"{guild_avatar}",
        )
        for emoji in emojis:
            emoji_nb += 1
        for channel in channels:
            channel_nb += 1

        for role in roles:
            role_nb += 1

        for member in members:
            member_nb += 1

        # await guild.create_sticker(interactions.File("logo - Copie.png"),"Test","test")

        day = guild.created_at.day
        month = guild.created_at.month
        year = guild.created_at.year
        hour = guild.created_at.hour
        min = guild.created_at.minute

        Embed.add_field("<:owner2:1077669013104111687> Propriétaire:", f"<@{owner}> ({owner})")
        Embed.add_field("<:emoji_logo:1077942830514839624> Emojis: ", f"**{emoji_nb}/50** utilisés", True)
        Embed.add_field("🔗 Salons: ", f"**{channel_nb}/500** utilisés", True)
        Embed.add_field("<:hype_squad_2:1077937763569107034> Roles: ", f"**{role_nb}/250** utilisés", True)
        Embed.add_field("<:all_users:1077956536787271820> Membres: ",
                        f"**{member_nb}** Total\n**...** En Ligne\n**...** Hors Ligne", True)
        Embed.add_field("<:new_user:1077651700934004746> Création:",
                        f"<t:{time_to_epoch(year, month, day, hour, min, tz)}:D>\n╰<t:{time_to_epoch(year, month, day, hour, min, tz)}:R>")

        # await guild.create_emoji(interactions.Image("gif.gif"),"gif")
        await ctx.send(embeds=Embed)


def setup(client: interactions.Client):
    Serverinfo(client)
