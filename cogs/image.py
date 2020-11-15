import discord
from discord.ext import commands
import aiohttp, asyncio
from random import choice, randint


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="meme",
        description="get a meme image",
    )
    async def cat(self, ctx):
        async with ctx.channel.typing():

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://meme-api.herokuapp.com/gimme") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meme", color=0x00FFFF)
                    embed.set_image(url=data["url"])

                    await ctx.send(embed=embed)

    @commands.command(
        name="woof",
        description="get a dog image",
    )
    async def woof_command(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Woof", color=0x00FFFF)
                    embed.set_image(url=data["url"])
                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Images(bot))
