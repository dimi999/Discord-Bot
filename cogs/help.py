import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.orange(),
            title = "Help",
            description = "A brief description of all the commands",
        )

        embed.set_thumbnail(url = 'https://inclusive-dance.ru/images/2017/06/20/help-me-help---1130801.jpeg')
        embed.set_author(name = 'Imid', icon_url = 'https://image.freepik.com/free-vector/cute-funny-white-robot-chat-bot-modern-flat-cartoon-character-illustration-isolated-blue-background-voice-support-service-chat-bot-virtual-online-help-customer-support_92289-946.jpg')

        embed.add_field(name = 'Join', value = 'Bot joins the voice channel you are in', inline = False)
        embed.add_field(name='Leave', value='Bot leaves the voice channel it is in', inline=False)
        embed.add_field(name='Capsipajura', value='You can enjoy some Romanian traditional music. You must be in a voice channel', inline=False)
        embed.add_field(name='Haha', value='Do you a have a funny friend in a voice channel? Show it to him/her', inline=False)
        embed.add_field(name='Audio', value='Just a random audio meme', inline=False)
        embed.add_field(name='Flip/Toss/Coin [no. of times; default = 1]', value='Just for serious decisions in life. Toss a coin to decide your future', inline=False)
        embed.add_field(name='Dog', value='Random photo of a dog', inline=False)
        embed.add_field(name='Cat', value='Random photo of a cat', inline=False)
        embed.add_field(name='Fox', value='Random photo of a fox', inline=False)
        embed.add_field(name='Cards/Highlow', value='You can play a basic Higher-Lower game with cards', inline=False)
        embed.add_field(name='Hi', value='Hello there', inline=False)
        embed.add_field(name='Ping', value='Check the ping of our bot', inline=False)
        embed.add_field(name='Insult', value='Random insult', inline=False)
        embed.add_field(name='Admin', value='If you are an admin, everybody should know it', inline=False)
        embed.add_field(name='Clear [no. of messages; default = 1]', value='Erase messages, just for certain roles', inline=False)
        embed.set_footer(text = "[] - optional; {} - mandatory")


        await ctx.send(embed = embed)



def setup(client):
    client.add_cog(Help(client))