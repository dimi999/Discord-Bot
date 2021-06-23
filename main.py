import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix= '*')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('*Bonjour'))
    print('Sunt online!!!!!!!!')

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount):

    if len(amount) >= 4:
        await ctx.send('Numar prea mare')
    else:
        if amount == 'all':
            amount = 1000
        amount = int(amount)
        await ctx.channel.purge(limit = amount)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send('This command does not exist! Check *tutorial.')
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Missing an argument! Check *tutorial.')
    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        await ctx.send('You lack permissions to execute the command!')
    elif isinstance(error, discord.errors.ClientException):
        await ctx.send('Already playing audio. Please wait!')
    elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You lack permission to do this action!')
    else:
        print(error)
        await ctx.send('Error!')

@client.command(aliases = ['tutorial'])
async def helppp(ctx):
    await ctx.send(file = discord.File('help.txt'))

#@client.command()
#async def dictionary(ctx, word, type):
 #   response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{word}/{type}")
  #  answer = response.json()
   # await ctx.send(answer[type])


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('ODM4Nzc1MTgzNjc0MDQ4NTQz.YJAAQw.WvBlQKdQLj_xOKRBwMj-Ae19AUg')