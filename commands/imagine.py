import datetime
import interactions
from utils.embed import create_embed
from utils.time_to_epoch import *
from utils.user_utils import *
import openai
from utils.config import config
from utils.url_to_image import *
import api.userAPI.dalle as dalleAPI

api_key = config("OpenAI API Key")



class Imagine(interactions.Extension):
    @interactions.extension_command(name="imagine", description="Permet de demander à DALL-E d'imaginer quelque chose",
                  options=
                 [
                     interactions.Option(
                         name="idea",
                         description="L'image a générer",
                         type=interactions.OptionType.STRING,
                         required=True,
                     )
                 ])
    async def imagine(self,ctx: interactions.CommandContext,idea:str):
        if dalleAPI.getDalleTry(ctx.author.id) >= 4:
            await ctx.send("Vous avez utilisé tout votre côta d'image a générer !")
        else:
            #await ctx.send("Cela peut durer un certain temps, ce n'est pas le bot qui bug ! x)",ephemeral=True)
            await ctx.defer()
            openai.api_key = api_key
            response = openai.Image.create(
                prompt=f"{idea}",
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            url_to_image(image_url)
            await ctx.send(content=f"{idea}",files=[interactions.File(filename=f'./image_file.png')])
            imgs = []
            for img in ctx.message.attachments:
                imgs.append(str(img.url))
            url = ctx.channel.url
            embed = create_embed(
                title=f"{idea}",
                include_thumbnail=True,
                thumbnail="".join(imgs)
            )
            embed.add_field("Channel Link:",f"{url}")
            await ctx.user.send(embeds=embed)
            dalleAPI.addDalleTry(ctx.author.id)


def setup(client: interactions.Client):
    Imagine(client)