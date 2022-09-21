from discord.ext import commands
from discord import Permissions
import discord

import random

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 523585610275880962  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

#-------Commands-------

#--'!name' command--
@bot.command(name='name')
async def name(ctx):
    print("Command '!name' invoked")
    await ctx.send(ctx.author)

#--'!d6' command--
@bot.command(name='d6')
async def d6(ctx):
    print("Command '!d6' invoked")
    await ctx.send(random.randint(1, 6))

#--'!admin' command--
@bot.command(name='admin')
async def admin(ctx, member : discord.Member):
    print("Command '!admin' invoked")
    # create role
    guild = ctx.guild
    await guild.create_role(name="admin", permissions=Permissions.all(), colour=discord.Colour(0xff0000))
    # give role
    role = discord.utils.get(ctx.guild.roles, name="admin")
    await member.add_roles(role)

#--'!ban' command--
@bot.command(name='ban')
async def ban(ctx, member : discord.Member):
    print("Command '!ban' invoked")
    await member.ban()

#--'Salut tout le monde' command--
@bot.event
async def on_message(message):
    if message.content == 'Salut tout le monde':
        await message.channel.send("Salut tout seul " + message.author.mention)
    await bot.process_commands(message)

#--'!count' command--
@bot.command(name='count')
async def count(ctx):
    print("Command '!count' invoked")
    online_count = 0
    offline_count = 0
    idle_count = 0
    dnd_count = 0
    for member in ctx.guild.members:
        if member.status == discord.Status.online:
            online_count += 1
        if member.status == discord.Status.offline:
            offline_count += 1
        if member.status == discord.Status.idle:
            idle_count += 1
        if member.status == discord.Status.dnd:
            dnd_count += 1
    await ctx.send(str(online_count) + " members online, " + str(offline_count) + " members offline, " + str(idle_count) + " members idle, " + str(dnd_count) + " members dnd")

#-------Commands-------

token = "your_token_here"
bot.run(token)  # Starts the bot