import interactions
from utils.embed import create_embed
from utils.config import config
import requests

class Wiki(interactions.Extension):

    @interactions.extension_command(name="wiki", description="permet de chercher des informations sur wikipedia",
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
            f"https://en.wikipedia.org/w/api.php?action=query&titles={search}&prop=extracts&format=json&exintro=1Search%20articles").json()
        # print(aa['url'])
        #https://en.wikipedia.org/w/api.php?action=query&titles=Minecraft&prop=extracts&format=json&exintro=1Search%20articles


def setup(client: interactions.Client):
    Wiki(client)