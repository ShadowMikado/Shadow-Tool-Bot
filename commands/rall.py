import interactions
from utils.embed import create_embed
from utils.user_utils import *
from utils.time_to_epoch import *
import random


class Rall(interactions.Extension):
    @interactions.extension_command(name="rall", description="permet de faire dire un nombre aléatoire", options=
    [
        interactions.Option(
            name="number1",
            description="Nombre 1",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
        interactions.Option(
            name="number2",
            description="Nombre 2",
            type=interactions.OptionType.INTEGER,
            required=True,
        )
    ]
                                    )
    async def rall(self, ctx: interactions.CommandContext, number1: int, number2: int):
        if number1 > number2:
            await ctx.send("Vous ne pouvez pouvez pas faire cela !",ephemeral=True)
            return
        rdm = random.randint(number1, number2)
        await ctx.send(str(rdm),ephemeral=True)


def setup(client: interactions.Client):
    Rall(client)
