from discord.ext import commands
import requests

class Text(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def salut(self, ctx):
        await ctx.send('Le baguette')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping: {self.client.latency * 1000} ms')

    @commands.command()
    async def insult(self, ctx):
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        insult = response.json()
        await ctx.send(insult['insult'])

    def is_admin(ctx):
        return ctx.author.guild_permissions.administrator

    @commands.command()
    @commands.check(is_admin)
    async def admin(self, ctx):
        await ctx.send(f'All hail our beloved admin {ctx.author.mention}')


def setup(client):
    client.add_cog(Text(client))