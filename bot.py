import discord
from discord.ext import commands
# from dotenv import load_dotenv
import os
# load_dotenv('.env')

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.',intents=intents)

pounce_channel = None
general_channel = None
team_channels = []

CAN_POUNCE = True

@bot.command()
@commands.has_role('QM')
async def start(ctx):
	global pounce_channel
	global team_channels
	team_channels = []
	for channel in ctx.guild.text_channels:
		if str(channel) == 'pounce':
			pounce_channel = channel
			await pounce_channel.send(f'Pounce channel initialised')
		if 'team' in str(channel):
			team_channels.append(channel)

@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingRole):
		await ctx.send('You do not have the required role!')


@bot.command(name='hello')
async def hello(ctx):
	await ctx.send('Hello')


@bot.command()
async def ping(ctx):
	await ctx.send('{}ms'.format(round(bot.latency*1000)))


@bot.command()
async def join(ctx,*args):
    team_no = args[0]
    role_name = "team-"+team_no
    testrole = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
    await ctx.send('{} joined Team {}'.format(ctx.author.mention,team_no))
    await ctx.author.add_roles(testrole)

@bot.command()
async def p(ctx,*args):
	if CAN_POUNCE:
		if 'team' in str(ctx.channel).lower():
			team_no = str(ctx.channel).split('-')[1]
			await pounce_channel.send('{} from Team {} pounced {}'.format(ctx.author.mention, team_no, ' '.join(args)))
			await ctx.channel.send('{} pounced {} and has been sent!'.format(ctx.author.mention,' '.join(args)))
		else:
			await ctx.channel.send('Need to be in a team text channel to pounce!')
	else:
		await ctx.channel.send('{} pounce is closed!'.format(ctx.author.mention))


@bot.command()
@commands.has_role('QM')
async def hint(ctx,*args):
	for channel in team_channels:
		await channel.send("**HINT : {}**".format(' '.join(args)))


@bot.command()
@commands.has_role('QM')
async def sp(ctx,*args):
	global CAN_POUNCE
	CAN_POUNCE = True
	for channel in team_channels:
		await channel.send('**Pounce is open!**')


@bot.command()
@commands.has_role('QM')
async def cp(ctx,*args):
	global CAN_POUNCE
	CAN_POUNCE = False
	for channel in team_channels:
		await channel.send('**Pounce is closed!**')

@bot.command()
async def clues(ctx,*args):
	team_no = str(ctx.channel).split('-')[1]
	await pounce_channel.send('Team {} wants a clue!'.format(team_no))


@bot.command()
async def object(ctx,*args):
	team_no = str(ctx.channel).split('-')[1]
	await pounce_channel.send('Team {} objects to clues!'.format(team_no))


@bot.event
async def on_raw_reaction_add(payload):
	msg_id = payload.message_id

	roleDict = {"1️⃣":"1","2️⃣":"2","3️⃣":"3","4️⃣":"4","5️⃣":"5","6️⃣":"6","7️⃣":"7","8️⃣":"8","9️⃣":"9"}
	print(msg_id)
	if msg_id == 884048131233292319:
		guild_id = payload.guild_id
		print(guild_id)
		guild = discord.utils.find(lambda g: g.id== guild_id,bot.guilds)
		print("here")
		print("team-"+roleDict[payload.emoji.name])
		role = discord.utils.get(guild.roles,name="team-"+roleDict[payload.emoji.name])

		if role is not None:
			for i in guild.members:
				print(i.name,i.id)
			print(payload.user_id)

			member = guild.get_member(payload.user_id)
			print(member.roles)
			if member is not None and len(member.roles)==1:
				await member.add_roles(role)
				print("done")
			else:
				print("member not found")
		else:
			print("Role not found")

		print("end")


@bot.event
async def on_raw_reaction_remove(payload):
	msg_id = payload.message_id

	roleDict = {"1️⃣":"1","2️⃣":"2","3️⃣":"3","4️⃣":"4","5️⃣":"5","6️⃣":"6","7️⃣":"7","8️⃣":"8","9️⃣":"9"}
	print(msg_id)
	if msg_id == 884048131233292319:
		guild_id = payload.guild_id
		print(guild_id)
		guild = discord.utils.find(lambda g: g.id== guild_id,bot.guilds)
		print("here")
		print("team-"+roleDict[payload.emoji.name])
		role = discord.utils.get(guild.roles,name="team-"+roleDict[payload.emoji.name])

		if role is not None:
			for i in guild.members:
				print(i.name,i.id)
			print(payload.user_id)

			member = guild.get_member(payload.user_id)
			if member is not None:
				await member.remove_roles(role)
				print("done")
			else:
				print("member not found")
		else:
			print("Role not found")

		print("end")


bot.run(DISCORD_TOKEN)
