import discord
import time
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name='ping', description='Shows the bot\'s latency.')
    async def ping(self, ctx):
        # Pong!
        try:
            await ctx.respond('Please wait...')
            before = time.monotonic()
            before_ws = int(round(self.client.latency * 1000, 1))
            message = await ctx.send('Getting api latency... ')
            ping = (time.monotonic() - before) * 1000

            embed = discord.Embed(
                title='Ping',
                description=f'🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms',
                color=0x5865F2
            )
            await message.edit('', embed=embed)

        except Exception as e:
            await ctx.send("Something went wrong. Please try again later.")
            print(e)

    @commands.slash_command(name='invite', description='Get the invite link for this bot.')
    async def invite(self, ctx):
        try:
            embed = discord.Embed(
                title='Invite',
                description=f'[Click here to invite me to your server.](https://discord.com/api/oauth2/authorize?client_id=944203658881552404&permissions=8&scope=bot%20applications.commands)',
                color=0x5865F2
            )
            await ctx.send('', embed=embed)

        except Exception as e:
            await ctx.send("Something went wrong. Please try again later.")
            print(e)

def setup(client):
    client.add_cog(Info(client))
