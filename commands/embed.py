import interactions
from utils.embed import create_embed
from utils.user_utils import *



class Embed(interactions.Extension):
    @interactions.extension_command(name="embed", description='Permet de créer un embed',
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                 [
                     interactions.Option(
                         name="title",
                         description="Titre de l'Embed",
                         type=interactions.OptionType.STRING,
                         required=False,
                     ),
                     interactions.Option(
                         name="description",
                         description="description de l'Embed",
                         type=interactions.OptionType.STRING,
                         required=False,
                     ),
                     interactions.Option(
                         name="include_thumbnail",
                         description="Inclus une image ?",
                         type=interactions.OptionType.BOOLEAN,
                         required=False,
                     ),
                     interactions.Option(
                         name="thumbnail",
                         description="URL de l'image",
                         type=interactions.OptionType.STRING,
                         required=False,
                     ),
                     interactions.Option(
                         name="hidden",
                         description="Visible pour les autres ?",
                         type=interactions.OptionType.BOOLEAN,
                         required=False,
                     ),

                 ])
    async def embed(self,ctx: interactions.CommandContext, title: str = "", description: str = None,
                    include_thumbnail: bool = False, thumbnail: str = None, hidden: bool = False):
        Embed = create_embed(

            title=title,
            description=description,
            include_thumbnail=include_thumbnail,
            color=0x0000FF,
            thumbnail=thumbnail,

        )
        await ctx.send(embeds=Embed, ephemeral=hidden)


def setup(client: interactions.Client):
    Embed(client)