import discord
from discord.ext import commands
from random import shuffle
from discord_components import *

def get_card(card):
    number = card % 13

    if number == 1:
        number = 'Ace'
    elif number == 0:
        number = 'King'
    elif number == 11:
        number = 'Jack'
    elif number == 12:
        number = 'Queen'

    type = card // 13
    if card % 13 == 0:
        type -= 1

    if type == 0:
        type = 'Hearts'
    elif type == 1:
        type = 'Diamonds'
    elif type == 2:
        type = 'Spades'
    elif type == 3:
        type = 'Clubs'

    return (number, type)

def cmp(num1, num2):
    num1 %= 13
    num2 %= 13

    if num1 == 0:
        num1 += 52

    if num2 == 0:
        num2 += 52

    if num1 == num2:
        return 0
    elif num1 < num2:
        return 1
    else:
        return -1


class Poker(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['cards'])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def highlow(self, ctx):

        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                 51, 52]

        shuffle(cards)

        mycard1 = get_card(cards[0])

        mycard2 = get_card(cards[1])

        status = cmp(cards[0], cards[1])

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title="Higher-lower game",
            description=f'Your card is {mycard1[0]} of {mycard1[1]}. How is the next card going to be?'
        )

        m = await ctx.send(embed = embed,
                       components = ActionRow([
                                               Button(label = "Higher", style = ButtonStyle.green),
                                               Button(label = "Lower", style = ButtonStyle.red),
                                               Button(label = "Tie")
                                               ]),
                       )

        def check(res):
            return res.user == ctx.author and res.channel == ctx.channel

        try:
            response = await self.client.wait_for("button_click", check = check, timeout = 10)
            chosen = response.component.label

            if (status == 0 and chosen == 'Tie') or (status == 1 and chosen == 'Higher') or (status == -1 and chosen == 'Lower'):
                text = 'You won!!!'
            else:
                text = 'You lost!!!'

            embed.description = f'The first card was {mycard1[0]} of {mycard1[1]}. The second card is {mycard2[0]} of {mycard2[1]}. {text}'

            await m.edit(embed = embed, components=[])

        except:
            embed.description = 'Time is up. You need to provide an answer in 10 seconds. Try again!'
            await m.edit(embed = embed, components=[])


def setup(client):
    client.add_cog(Poker(client))