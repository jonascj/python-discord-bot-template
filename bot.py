import logging
import os
import sys

import discord
from discord.ext import commands
import dotenv

# Load variables from .env file
dotenv.load_dotenv()


# Configure logging
LOG_LVL = os.getenv('LOG_LVL')
log = logging.getLogger(__name__)
if not LOG_LVL:
    LOG_LVL = 'DEBUG'

log = logging.getLogger(__name__)
h = logging.StreamHandler(sys.stdout)
h.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(h)
log.setLevel(LOG_LVL)


# Bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    log.error('`DISCORD_TOKEN` must be set in .env file')
    sys.exit()


# Create bot
intents = discord.Intents.none()
intents.messages = True
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)
#bot.remove_command('help')


@bot.event
async def on_ready():
    log.info('Bot logged in as `%s` (id %s)', bot.user, bot.user.id)
    log.info('Member of the following servers/guilds:')
    for guild in bot.guilds:
        log.info('  %s', guild.name)


@bot.command(name='hello', aliases=['yo'], help='hello world test command')
async def helloworld(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")




#@bot.command(name='help')
#async def help(ctx):
#
#    about_text = ('A simple bot which handles a simple (fifo) queue '
#                 'for help / support / private discussion requests.\n\n'
#                 'One or more admin members can dequeue members from the queue '
#                 'to offer help / support / private discussion '
#                 'in an orderly fashion.')
#
#    embed = discord.Embed(colour = discord.Colour.blue())
#    embed.set_author(name='Help')
#    embed.add_field(name='About', value=about_text, inline=False)
#                          
#    embed.add_field(name='`!qu [msg]` | `!needhelp [msg]`',
#                    value=('Queues you up for help with an optional message. '
#                           'Quote messages with space, e.g. *!qu "what ever"*.'),
#                    inline=False)
#
#    embed.add_field(name='`!ql` | `!nvm`',
#                    value='Leave the help queue',
#                    inline=False)
#
#    embed.add_field(name='`!qs` | `!show`',
#                    value='Show the queue',
#                    inline=False)
#
#    embed.add_field(name='`!qn`|`!next` (admin)',
#                    value='Help the next in line',
#                    inline=False)
#
#    embed.add_field(name='`!qe` (admin)',
#                    value='Empty the queue for this server/guild',
#                    inline=False)
#
#    await ctx.send(embed=embed)

# Start bot
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure:
    log.error('Bot login failed, improper/invalid token')
    sys.exit()
