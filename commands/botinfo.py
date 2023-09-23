import interactions
from utils.embed import create_embed
from utils.user_utils import *
from utils.time_to_epoch import *



class Botinfo(interactions.Extension):
    @interactions.extension_command(name="botinfo", description="permet de voir les informations du bot")

    async def botinfo(self,ctx: interactions.CommandContext):

        day = self.client.me.created_at.day
        month = self.client.me.created_at.month
        year = self.client.me.created_at.year
        hour = self.client.me.created_at.hour
        min = self.client.me.created_at.minute
        avatar = self.client.me.icon_url

        guild_number = 0
        for guild in self.client.guilds:
            guild_number +=1

        embed = create_embed(
            title="",
            description="",
            include_thumbnail=True,
            thumbnail=f"{avatar}",
            include_author=True,
            author_name=f"Information du bot {self.client.me.name}",
        )
        embed.add_field("<:owner2:1077669013104111687> Créateur:",f"<@783739472079880243> `Shadow 🙃 | ψ#0817`",True)
        embed.add_field("<:new_user:1077651700934004746> Création:",
                        f"<t:{time_to_epoch(year, month, day, hour, min, tz())}:D>\n╰<t:{time_to_epoch(year, month, day, hour, min, tz())}:R>",True)
        embed.add_field("<:logo_add:1086229509541474404> Divers:","Au départ j'ai voulus créer un bot AntiRaid, mais j'ai dérivé vers un bot utilitaire x)")
        embed.add_field("🔨 Nombre de Serveur:",f"**{guild_number}/100** utilisés")
        await ctx.send("",embeds=embed)


def setup(client: interactions.Client):
    Botinfo(client)