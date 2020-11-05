
  
from random import choice, randint
from discord.ext import commands
import discord
import aiohttp
import random
from senpai import bot


class Fun(commands.Cog):
	def __init__(self, client):
		self.bot = client


	@commands.command(aliases=['8ball'])
	@commands.guild_only()
	async def _8ball(self, ctx, *, question):
		responses = ['It Is Certain.',
					 'It Is Decidedly So.',
					 'Without A Doubt.',
					 'Yes – Definitely.',
					 'You May Rely On It.',
					 'As I See It, Yes.',
					 'Most Likely.',
					 'Outlook Good.',
					 'Yes.',
					 'Signs Point To Yes.',
					 'Reply Hazy, Try Again.',
					 'Ask Again Later.',
					 'Better Not Tell You Now.',
					 'Cannot Predict Now.',
					 'Concentrate And Ask Again.',
					 'Dont Count On It.',
					 'My Reply Is No.',
					 'My Sources Say No.',
					 'Outlook Not So Good.',
					 'Very Doubtful.', 
					 'You have answered your own quesiton.',]

		embed = discord.Embed(
		colour = 0x00ffff,
		title = 'You Have **Challenged** The 8Ball',
		description = f'**Qeustion**\n{question}\n**Answer**\n{random.choice(responses)}',
		)
		await ctx.send(embed=embed)



	@commands.command()
	@commands.guild_only()
	async def poke(self, ctx, arg):
		members = [x for x in ctx.guild.members if not x.bot]
		if arg.lower() == 'random':
			embed = discord.Embed(
			colour = 0x2F3136,
			title = 'You Got Poked',
			description = f'👋 Hey {choice(members).mention}',
			)
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(
			colour = 0x2F3136,
			title = 'You Got Poked',
			description = f'👋 Hey {choice(members).mention}',
			)
			await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	async def coin(self, ctx, arg):
		if arg.lower() == 'heads' or arg.lower() == 'tails':
			piece = choice(['heads', 'tails'])
			if arg.lower() in piece:
				embed = discord.Embed(
				colour = 0x2F3136,
				title = 'Heads Or Tails',
				description = f'**{piece}**!\n \n ✅ You Won',
				)
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(
				colour = 0x2F3136,
				title = 'Heads Or Tails',
				description = f'**{piece}**!\n \n ❌ You Lost',
				)
				await ctx.send(embed=embed)
		else:
			embed = discord.Embed(
			colour = 0x2F3136,
			title = 'Heads Or Tails Error',
			description = 'You Must Input Either `heads` or `tails`',
			)
			await ctx.send(embed=embed)
			return
   
	
	@commands.command()
	@commands.guild_only()
	async def roll(self, ctx, arg):
		try:
			float(arg)
		except:
			embed = discord.Embed(
			colour = 0x2F3136,
			title = 'Roll Error',
			description = '❌ You Must Input An Integer',
			)
			await ctx.send(embed=embed)
		else:
			number = randint(1, int(arg))
			embed = discord.Embed(
			colour = 0x2F3136,
			title = 'Roll',
			description = f'🎲 You Rolled A **{number}**',
			)
			await ctx.send(embed=embed)
			return


	


def setup(client):
	client.add_cog(Fun(client))