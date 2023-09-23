import interactions
from utils.embed import create_embed


class Emojis(interactions.Extension):
    @interactions.extension_command(name="emojis", description="permet de voir tous les émojis du serveur")
    async def emojis(self, ctx: interactions.CommandContext):
        authoravatar = f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.webp?size=128"
        Embed = create_embed(
            title=f"",
            description="",
            color=0x0000FF,
            include_thumbnail=True,
            footer_text=f"Demandé par {ctx.user.username}#{ctx.user.discriminator}",
            footer_image=authoravatar
        )
        emojis_list = []
        for emoji in ctx.guild.emojis:
            emojis_list.append(f"<:{emoji.name}:{emoji.id}>")
        # print(' '.join(roles))
        Embed.add_field("**Émojis :**", ''.join(emojis_list))

        await ctx.send(embeds=Embed)

    # logs
    # add <:add:1077239700277956690>
    # remove <:remove:1077239628177870920>
    # change <:change:1077239677117005934>
    # new user <:new:1061711725973491733>
    # owner <:owner2:1077669013104111687>
    # hype squad logo <:hype_squad_2:10 &77937763569107034>
    # emoji logo <:emoji_logo:1077942830514839624>
    # users <:all_users:1077956536787271820>


def setup(client: interactions.Client):
    Emojis(client)
