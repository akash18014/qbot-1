import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv('.env')

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')

pounce_channel = None

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
	print(ctx.author.name)
	if ctx.author.id != 278051799020339201:
		ctx.channel.send(f'You cannot use this command!')
		return None
	for channel in ctx.guild.text_channels:
		if str(channel) == 'pounce':
			pounce_channel = channel
			await pounce_channel.send(f'Pounce channel initialised')
			return None


@bot.command(name='hello')
async def hello(ctx):
	await ctx.send('Hello')

@bot.command()
async def p(ctx,*args):
	if 'team' in str(ctx.channel).lower():
		await pounce_channel.send('{} pounced {}'.format(ctx.author.mention,' '.join(args)))
		await ctx.channel.send('{} pounced {} and has been sent!'.format(ctx.author.mention,' '.join(args)))
	else:
		await ctx.channel.send('Need to be in a team text channel to pounce!')

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