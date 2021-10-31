import discord
from discord.ext import commands
from random import randint
from random import seed
import time


class Flip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['toss', 'coin'])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def flip(self, ctx, amount=1):

        try:
            C = 0
            P = 0

            if amount > 1000000:
                await ctx.send('Number is too large!')
                return

            if amount <= 0:
                await ctx.send('Insert a positive number')
                return

            seed(time.time())

            for i in range(1, amount + 1):
                val = randint(0, 100001)
                if val % 2 == 0:
                    C = C + 1
                else:
                    P = P + 1
            if C > P:
                await ctx.send(file=discord.File("images/cap.png"))
                await ctx.send('Heads!')
            elif P > C:
                await ctx.send(file=discord.File("images/pajura.png"))
                await ctx.send('Tails!')
            else:
                await ctx.send('Tie!')
            await ctx.send(f'Heads: {C}; Tails: {P}')

        except:
            await ctx.send('E doar vina lui Dimi')

def setup(client):
    client.add_cog(Flip(client))