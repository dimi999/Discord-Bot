from discord.ext import commands
from random import shuffle

class Poker(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['cards'])
    async def poker(self, ctx, player2='0', player3='0', player4='0'):

        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                 51, 52]

        player1 = ctx.message.author.mention
        player1 = player1
        dealer = 'dealer'
        players = [dealer, player1, player2, player3, player4]
        shuffle(cards)

        sums = [0, 0, 0, 0, 0]
        aces = [0, 0, 0, 0, 0]

        it = 0
        for i in range(0, 2):
            for player in range(0, 5):

                if players[player] == '0':
                    break

                if cards[it] % 13 == 1:
                    aces[player] = aces[player] + 1
                elif cards[it] % 14 >= 10:
                    sums[player] = sums[player] + 10
                else:
                    sums[player] = sums[player] + cards[it] % 13

                type = '0'
                value = '0'

                div = int(cards[it] / 13)

                if cards[it] % 13 == 0:
                    div = div - 1

                print(cards[it], div)

                if div == 0:
                    type = 'hearts'
                elif div == 1:
                    type = 'diamonds'
                elif div == 2:
                    type = 'spades'
                elif div == 3:
                    type = 'clubs'

                if cards[it] % 13 == 0:
                    value = 'K'
                elif cards[it] % 13 == 12:
                    value = 'Q'
                elif cards[it] % 13 == 11:
                    value = 'J'
                elif cards[it] % 13 == 1:
                    value = 'A'
                else:
                    value = str(cards[it] % 13)

                round = ''

                if i == 0:
                    round = 'first'
                else:
                    round = 'second'

                if player != 0 or i != 1:
                    await ctx.send(f"{players[player]}'s {round} card is {value} of {type}")
                it = it + 1

def setup(client):
    client.add_cog(Poker(client))