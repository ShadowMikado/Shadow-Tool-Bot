import random
import string

import interactions
import openai

from utils.embed import create_embed
from utils.user_utils import *


class Changenick(interactions.Extension):
    @interactions.extension_command(name="changenick", description="permet de changer le pseudo d'un utilisateur",
                                    default_member_permissions=interactions.Permissions.ADMINISTRATOR, options=
                                    [
                                        interactions.Option(
                                            name="user",
                                            description="Nom d'utilisateur demandé",
                                            type=interactions.OptionType.USER,
                                            required=True,
                                        ),
                                        interactions.Option(
                                            name="new_username",
                                            description="Nouveau pseudo",
                                            type=interactions.OptionType.STRING,
                                            required=False,
                                        ),
                                        interactions.Option(
                                            name="random_name",
                                            description="Aléatoire",
                                            type=interactions.OptionType.BOOLEAN,
                                            required=False,
                                        )
                                    ])
    async def changenick(self, ctx: interactions.CommandContext, user: interactions.Member, new_username: str = None, random_name: bool = False):

        if user.id == ctx.guild.owner_id:
            await ctx.send("Vous ne pouvez pas vous renommer vous même, utilisez la commande `/nick`")
            return

        try:
            if new_username is not None and random_name == False:
                await user.modify(nick=new_username)
                await ctx.send(f"Vous avez bien changé le pseudo de <@{user.id}>", ephemeral=True)
            elif new_username is None and random_name == False:
                await user.modify(nick=f"")
                await ctx.send(f"Vous avez réinitialisé le pseudo de <@{user.id}>", ephemeral=True)
            elif new_username is None and random_name == True:
                rdm = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
                await user.modify(nick=f"Default {rdm}")
                await ctx.send(f"Vous avez mis un nom aléatoire à <@{user.id}>", ephemeral=True)
            elif new_username is not None and random_name == True:
                await ctx.send(f"Vous ne pouvez pas mettre un nom aléatoire et un nom customisé !", ephemeral=True)
        except:
            await ctx.send("Erreur, sans doute de permissions, vérifier si les permissions du bot sont aux plus haut")
            return




def setup(client: interactions.Client):
    Changenick(client)
