import interactions
from utils.embed import create_embed
from utils.config import config
import requests

class Search(interactions.Extension):

    @interactions.extension_command(name="search", description="permet de chercher sur le web",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                 [
                     interactions.Option(
                         name="search",
                         description="recherche",
                         type=interactions.OptionType.STRING,
                         required=True,
                     )
                 ])
    async def addrole(self,ctx: interactions.CommandContext, search:str):

        embed = create_embed(
            title=f"Résultats pour {search}",
            description="",
        )
        req = requests.get(
            f"https://www.googleapis.com/customsearch/v1?key=AIzaSyAH7k9OWw20DI2_dBnjazQutqMdHOOGbEk&cx=017576662512468239146:omuauf_lfve&q={search}").json()
        # print(aa['url'])
        ba = req['items']
        for items in ba:
            # print(items['formattedUrl'])
            # print(items)
            formated = f"[{items['title']}]({items['link']})"
            embed.add_field(f"",f"{formated}")
            #print(formated)
        await ctx.send("",embeds=embed)


def setup(client: interactions.Client):
    Search(client)