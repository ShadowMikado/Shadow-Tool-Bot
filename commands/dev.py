import interactions
from utils.embed import create_embed
from utils.user_utils import *



class Dev(interactions.Extension):
    @interactions.extension_command(name="dev", description="in dev command",
                 default_member_permissions=interactions.Permissions.ADMINISTRATOR)
    async def dev(self,ctx: interactions.CommandContext):
        await ctx.send(content=f"Dev",files=[interactions.File(filename=f'./image_file.png')])
        for img in ctx.message.attachments:
            print(img.url)


def setup(client: interactions.Client):
    Dev(client)