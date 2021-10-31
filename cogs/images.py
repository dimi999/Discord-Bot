from discord.ext import commands
import requests

class Images(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def dog(self, ctx):
        response = requests.get("https://random.dog/woof.json")
        dog = response.json()
        await ctx.send(dog['url'])

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def cat(self, ctx):
        response = requests.get("https://aws.random.cat/meow")
        cat = response.json()
        await ctx.send(cat['file'])

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def fox(self, ctx):
        response = requests.get("https://randomfox.ca/floof/")
        fox = response.json()
        await ctx.send(fox['image'])


def setup(client):
    client.add_cog(Images(client))
