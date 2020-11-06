

import discord
import os
import time


start_time = time.time()
from discord.ext import commands
from keep_alive import keep_alive


def get_prefix(client, message):

    prefixes = ['sp!', 'SP!', 'Sp!', 'sP!']   

    if not message.guild:
        prefixes = ['sp!']   

   

    return commands.when_mentioned_or(*prefixes)(client, message)


bot =  commands.Bot(                                         
   
    command_prefix=get_prefix, prefix=os.getenv('prefix'),
	  pm_help=True,
    description='bruh',          
    owner_id=700609775838298113,  command_attrs=dict(hidden=True),      
     case_intents=True
		)






@bot.event
async def command_prefix(bot, message):
 if message.author.id == 700609775838298113:
  return ''
 else:
  return 'sp!' 


bot.snipes = {}



@bot.event
async def on_message_delete(message):
    bot.snipes[message.channel.id] = message

@bot.command()
async def snipe(ctx, *, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    try:
        msg = bot.snipes[channel.id]
    except KeyError:
        return await ctx.send("There is nothing to snipe!")
    await ctx.send(embed=discord.Embed(description=msg.content, color=0xffff00).set_author(name=str(msg.author), icon_url=str(msg.author.avatar_url)))
@bot.event
async def on_ready():
  
    print(
        f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: sp!\n-----"
    )
    activity = discord.Activity(name='Anime', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

    


	


bot.colors = {
    "WHITE": 0xFFFFFF,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "RED": 0xE74C3C,
    "NAVY": 0x34495E,
    "DARK_AQUA": 0x11806A,
    "DARK_GREEN": 0x1F8B4C,
    "DARK_BLUE": 0x206694,
    "DARK_PURPLE": 0x71368A,
    "DARK_VIVID_PINK": 0xAD1457,
    "DARK_GOLD": 0xC27C0E,
    "DARK_ORANGE": 0xA84300,
    "DARK_RED": 0x992D22,
    "DARK_NAVY": 0x2C3E50,
		"CYAN": 0x00FFF,
}
bot.color_list = [c for c in bot.colors.values()]

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "true"
os.environ["JISHAKU_NO_UNDERSCORE"] = "true"


bot.load_extension('jishaku')

for extension in os.listdir('./cogs/'):
 if extension.endswith('.py'):
   bot.load_extension(f"cogs.{extension.replace('.py', '')}")

	






	
			

keep_alive()
bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)


