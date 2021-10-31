import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from random import randint
import ctypes
import ctypes.util

class Audio(commands.Cog):

    def __init__ (self, client):
        self.client = client

    async def load_audio(self):
        print("ctypes - Find opus:")  #####doar pt linux, pe windows nu functioneaza
        a = ctypes.util.find_library('opus')
        print(a)

        print("Discord - Load Opus:")
        b = discord.opus.load_opus(a)
        print(b)

        print("Discord - Is loaded:")
        c = discord.opus.is_loaded()
        print(c)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def join(self, ctx):
        try:
            if not ctx.voice_client:
                channel = ctx.message.author.voice.channel
                await channel.connect()
            else:
                await ctx.send('Already connected.')
        except:
            await ctx.send('You must be in a voice channel!')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send('I am not connected.')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def capsipajura(self, ctx):

        await self.load_audio()

        try:
            if not ctx.voice_client:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
            else:
                voice = ctx.voice_client

            source = FFmpegPCMAudio(f'audio/cap&pajura.mp3')
            player = voice.play(source)
        except:
            await ctx.send('You must be in a voice channel!')


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def haha(self, ctx):

        await self.load_audio()

        try:
            if not ctx.voice_client:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
            else:
                voice = ctx.voice_client

            source = FFmpegPCMAudio(f'audio/laugh.mp3')
            player = voice.play(source)
        except:
            await ctx.send('You must be in a voice channel!')



    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def audio(self, ctx):

        await self.load_audio()

        try:
            if not ctx.voice_client:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
            else:
                voice = ctx.voice_client

            val = randint(1, 13)
            print(val)
            source = FFmpegPCMAudio(f'audio/audio{val}.mp3')
            player = voice.play(source)
        except:
            await ctx.send('You must be in a voice channel!')



def setup(client):
    client.add_cog(Audio(client))