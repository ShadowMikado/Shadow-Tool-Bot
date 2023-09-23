import datetime
import interactions
from utils.embed import create_embed
from utils.time_to_epoch import *
from utils.user_utils import *


tz = tz()
class Changelog(interactions.Extension):
    @interactions.extension_command(name="changelog", description="permet de créer un changelog",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                 [

                     interactions.Option(
                         name="add",
                         description="Ajouts",
                         type=interactions.OptionType.STRING,
                         required=False,
                     ),
                     interactions.Option(
                         name="change",
                         description="Changements",
                         type=interactions.OptionType.STRING,
                         required=False,
                     ),
                     interactions.Option(
                         name="remove",
                         description="Suppressions",
                         type=interactions.OptionType.STRING,
                         required=False,
                     )
                 ])
    async def changelog(self,ctx: interactions.CommandContext, add: str = None, change: str = None, remove: str = None):

        day = datetime.date.today().day
        month = datetime.date.today().month
        year = datetime.date.today().year
        hour = datetime.datetime.today().hour
        min = datetime.datetime.today().minute
        print(min)
        """if not add and not change and not remove:
            await ctx.send("Vous n'avez pas fournis d'arguments ! (Les arguments doivent être séparé par un `;`)",ephemeral=    True)"""
        authoravatar = f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.webp?size=128"
        Embed = create_embed(
            title=f"Changelog du <t:{time_to_epoch(year, month, day, hour, min, tz)}:D>",
            color=0x0000FF,
            footer_text=f"Créé par {ctx.user.username}#{ctx.user.discriminator}",
            footer_image=authoravatar
        )
        if add == None and change == None and remove == None:
            await ctx.send("Vous n'avez pas fournis d'arguments ! (Les arguments doivent être séparé par un `;`)",
                           ephemeral=True)

        else:
            if add:
                # print(str(add))
                liste_add = add.split(";")
                char_add = '<:add:1077239700277956690> '
                for i in range(len(liste_add)):
                    # print(str(liste_add[i]))
                    liste_add[i] = char_add + liste_add[i].strip() + f"\n"

                final_add = ''.join(liste_add)
                Embed.add_field(name="**__Ajouts__**", value=f"{final_add}")
                # print(str(final_add))
            else:
                Embed.add_field(name="**__Ajouts__**", value=f"❌ Aucuns Ajouts")
            if change:
                liste_change = change.split(";")
                char_change = '<:change:1077239677117005934> '
                for i in range(len(liste_change)):
                    liste_change[i] = char_change + liste_change[i] + f"\n"
                final_change = ''.join(liste_change)
                Embed.add_field(name="**__Changements__**", value=f"{final_change}")
            else:
                Embed.add_field(name="**__Changements__**", value=f"❌ Aucuns Changements")
            if remove:
                liste_remove = remove.split(";")
                char_remove = '<:remove:1077239628177870920> '
                for i in range(len(liste_remove)):
                    liste_remove[i] = char_remove + liste_remove[i] + f"\n"
                final_remove = ''.join(liste_remove)
                Embed.add_field(name="**__Suppressions__**", value=f"{final_remove}")
            else:
                Embed.add_field(name="**__Suppressions__**", value=f"❌ Aucunes Suppressions")

            await ctx.send(embeds=Embed)

def setup(client: interactions.Client):
    Changelog(client)