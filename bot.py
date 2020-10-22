import discord
from discord.ext import commands
# from dotenv import load_dotenv
import os
# load_dotenv('.env')

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='.')

pounce_channel = None
team_channels = []

CAN_POUNCE = False
'''@bot.event
async def on_message(message):
	print(str(message.guild))
	channel = bot.get_channel(766579138630778912)
	valid_channels=["commands"]
	if str(message.channel) in valid_channels:
		await channel.send(f'{message.author.mention} said \'{message.content}\' in {message.channel}')
'''
@bot.command()
async def start(ctx):
	global pounce_channel
	global team_channels
	team_channels = []
	print(ctx.author.name)
	if ctx.author.id not in [278051799020339201,745555850323820545]:
		ctx.channel.send(f'You cannot use this command!')
	for channel in ctx.guild.text_channels:
		if str(channel) == 'pounce':
			pounce_channel = channel
			await pounce_channel.send(f'Pounce channel initialised')
		if 'team' in str(channel):
			team_channels.append(channel)


@bot.command(name='hello')
async def hello(ctx):
	await ctx.send('Hello')

@bot.command()
async def ping(ctx):
	await ctx.send('{}ms'.format(round(bot.latency*1000)))


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
async def hint(ctx,*args):
	if ctx.author.id not in [278051799020339201,745555850323820545]:
		await ctx.channel.send(f'You cannot use this command!')
	else:
		for channel in team_channels:
			await channel.send("**HINT : {}**".format(' '.join(args)))


@bot.command()
async def sp(ctx,*args):
	global CAN_POUNCE
	CAN_POUNCE = True
	if ctx.author.id not in [278051799020339201,745555850323820545]:
		await ctx.channel.send(f'You cannot use this command!')
	else:
		for channel in team_channels:
			await channel.send('**Pounce is open!**')


@bot.command()
async def cp(ctx,*args):
	global CAN_POUNCE
	CAN_POUNCE = False
	if ctx.author.id not in [278051799020339201,745555850323820545]:
		await ctx.channel.send(f'You cannot use this command!')
	else:
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


@bot.command()
async def sendq(ctx,*args):
	with open(args[1] + '.png','rb') as fp:
		for channel in team_channels:
			await channel.send('Q{} : '.format(args[0]), file = discord.File(fp,args[1]+'.png'))
			fp.seek(0)



bot.run(DISCORD_TOKEN)
'''

import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run(TOKEN)
'''