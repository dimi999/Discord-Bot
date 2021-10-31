import discord
from discord.ext import commands
import os
from discord_components import *

client = commands.Bot(command_prefix= '*')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('*Bonjour'))
    print('Sunt online!!!!!!!!')
    DiscordComponents(client)


@client.command()
@commands.has_permissions(manage_messages = True)
@commands.cooldown(1, 5, commands.BucketType.guild)
async def clear(ctx, amount):

    if len(amount) > 4:
        await ctx.send('Your number is too big')
    else:
        if amount == 'all':
            amount = 9999
        amount = int(amount)
        await ctx.channel.purge(limit = amount)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send('This command does not exist! Check *help.')
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Missing an argument! Check the help command.')
    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        await ctx.send('You lack permissions to execute the command!')
    elif isinstance(error, discord.errors.ClientException):
        await ctx.send('Already playing audio. Please wait!')
    elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You lack permission to do this action!')
    elif isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        await ctx.send('Please wait at least 5 seconds between 2 commands of the same type!')
    elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('Bot missing permissions!')
    elif isinstance(error, discord.ext.commands.errors.NSFWChannelRequired):
        await ctx.send('This command is available only on NSFW channels')
    else:
        print(error)
        await ctx.send('Error!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('')