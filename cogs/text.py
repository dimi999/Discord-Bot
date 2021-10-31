from discord.ext import commands
import requests

class Text(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def hi(self, ctx):
        await ctx.send('Hello there!')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def ping(self, ctx):
        await ctx.send(f'Ping: {self.client.latency * 1000} ms')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.is_nsfw()
    async def insult(self, ctx):
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        insult = response.json()
        await ctx.send(insult['insult'])

    def is_admin(ctx):
        return ctx.author.guild_permissions.administrator

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.check(is_admin)
    async def admin(self, ctx):
        await ctx.send(f'All hail our beloved admin {ctx.author.mention}')


def setup(client):
    client.add_cog(Text(client))