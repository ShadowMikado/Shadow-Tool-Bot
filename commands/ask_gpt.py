import interactions
import openai

from utils.embed import create_embed
from utils.user_utils import *
from utils.config import config
import api.userAPI.chatgpt as gptAPI

api_key = config("OpenAI API Key")



class Ask_gpt(interactions.Extension):
    @interactions.extension_command(name="ask-gpt", description="Permet de poser une question a ChatGPT", options=
    [

        interactions.Option(
            name="prompt",
            description="Question",
            type=interactions.OptionType.STRING,
            required=True,
        )])
    async def ask_gpt(self,ctx: interactions.CommandContext, prompt: str):
        if gptAPI.getChatGptTry(ctx.author.id) >= 10:
            await ctx.send("Vous avez utilisé tout votre côta de question !")
        else:
            openai.api_key = api_key
            Embed = create_embed(description=" ", title=" ", include_author=True, author_name="Question à Chat-GPT")
            await ctx.defer()

            prompt = prompt
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=60,
                n=1,
                stop=None,
                temperature=0.5,
            )

            message = response.choices[0].text.strip()
            Embed.add_field(f"Question:", str(prompt))
            Embed.add_field(f"Réponse:", message)

            await ctx.send("", embeds=Embed)
            gptAPI.addChatGptTry(ctx.author.id)
        # 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

def setup(client: interactions.Client):
    Ask_gpt(client)