import discord
from discord.ext import commands
import aiohttp

class apis(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

  
						 
    @commands.command(
			name='ss'
		)
    async def ss(self, ctx, *, url: str, description='Get a screen shot of the web'):
     async with ctx.typing(), aiohttp.ClientSession() as session:
         screener = "http://magmachain.herokuapp.com/api/v1"
         async with session.post(screener, headers=dict(website=url)) as r:
             website = (await r.json())["snapshot"]
             e = discord.Embed(title='Not a webpeek',color=0x00FFFF)
     e.set_image(url=website)
     await ctx.send(embed=e)
	
				
def setup(bot):
    bot.add_cog(apis(bot))