import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # Sets the bot's presence to idle and status then logs.
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="lewd.tritan.dev"))
        print('[STARTING] --> Status has been set.')
        print('[READY] --> Client is logged in, uwu time to help get people off!')

def setup(client):
    client.add_cog(Events(client))
