import discord
from discord.ext import commands
import os


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



	@commands.command()
	@commands.is_owner()

	async def guilds(self, ctx):
		guild_names = ""
		for guild in self.bot.guilds:
			guild_names += f"● {guild.name} \n"

		embed = discord.Embed(
		colour = 0x00ffff,
		title = 'Bot Guild Infomation',
		description= f'**Amount Of Bot Guilds**\n{len(self.bot.guilds)}\n\n**Guild Names**\n{guild_names}',
		)
		await ctx.send(embed=embed)

	@commands.command(aliases=['cl'])
	@commands.is_owner()
	@commands.guild_only()
	async def cogs_load(self, ctx, name: str):

		embed = discord.Embed(
		colour = 0x2F3136,
		title = 'Loading',
		description = f'Loading {name} Extension',
		)

		await ctx.send(embed=embed)
		self.bot.load_extension(f'cogs.{name}')
		await ctx.channel.purge(limit=1)

		embed = discord.Embed(
		colour = 0x2F3136,
		title = 'Loaded',
		description = f'Loaded {name} Extension',
		)
		await ctx.send(embed=embed)


	@commands.command(aliases=['cu'])
	@commands.is_owner()
	@commands.guild_only()
	async def cogs_unload(self, ctx, name: str):

		embed = discord.Embed(
		colour = 0x2F3136,
		title = 'Unloading',
		description = f'Unloading {name} Extension',
		)

		await ctx.send(embed=embed)
		self.bot.unload_extension(f'cogs.{name}')
		await ctx.channel.purge(limit=1)

		embed = discord.Embed(
		colour = 0x2F3136,
		title = 'Unloaded',
		description = f'Unloaded {name} Extension',
		)
		await ctx.send(embed=embed)


	@commands.command(aliases=['cr'])
	@commands.is_owner()
	@commands.guild_only()
	async def cogs_reload(self, ctx, name: str):

		embed = discord.Embed(
		colour = 0x2F3136,
		title = 'Reloading',
		description = f'Reloading {name} Extension',
		)

		await ctx.send(embed=embed)
		self.bot.reload_extension(f'cogs.{name}')
		await ctx.channel.purge(limit=1)

		embed = discord.Embed(
		colour = 0x2F3136,
		title = 'Reloaded',
		description = f'Reloaded {name} Extension',
		)
		await ctx.send(embed=embed)

		

		


def setup(bot):
	bot.add_cog(Owner(bot))