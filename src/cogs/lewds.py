import discord
import requests
from discord.ext import commands

class Lewds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name='yaoi', description='Returns a random yaoi image or gif.')
    async def yaoi(self, ctx):
        # Yaoi slash command, grabs from api and replies with an ephimeral message.
        try:
            response = requests.get(
                "https://lewd.tritan.dev/api/v1/yaoi").json()
            embed = discord.Embed(
                title="Here's some yaoi!~", description="Provided by our [yaoi api.](https://lewd.tritan.dev)", color=0x5865F2)
            embed.set_image(url=response["url"])
            await ctx.respond(embed=embed,  ephemeral=True)
            # Catch errors lazily
        except Exception as e:
            await ctx.respond("Something went wrong. Please try again later.")
            print(e)

    @commands.slash_command(name='shower', description='Returns a shower yaoi image or gif.')
    async def shower(self, ctx):
        # Shower slash command, grabs from api and replies with an ephimeral message.
        try:
            response = requests.get(
                "https://lewd.tritan.dev/api/v1/shower").json()
            embed = discord.Embed(
                title="Here's some shower yaoi!~", description="Provided by our [yaoi api.](https://lewd.tritan.dev)", color=0x5865F2)
            embed.set_image(url=response["url"])
            await ctx.respond(embed=embed,  ephemeral=True)
            # Catch errors lazily
        except Exception as e:
            await ctx.respond("Something went wrong. Please try again later.")
            print(e)

    @commands.slash_command(name='gif', description='Returns a yaoi gif.')
    async def gif(self, ctx):
        # Gif slash command, grabs from api and replies with an ephimeral message.
        try:
            response = requests.get(
                "https://lewd.tritan.dev/api/v1/gifs").json()
            embed = discord.Embed(
                title="Here's some yaoi gifs!~", description="Provided by our [yaoi api.](https://lewd.tritan.dev)", color=0x5865F2)
            embed.set_image(url=response["url"])
            await ctx.respond(embed=embed,  ephemeral=True)
            # Catch errors lazily
        except Exception as e:
            await ctx.respond("Something went wrong. Please try again later.")
            print(e)

    @commands.slash_command(name='blowjob', description='Returns a blowjob yaoi image or gif.')
    async def blowjob(self, ctx):
        # Gif slash command, grabs from api and replies with an ephimeral message.
        try:
            response = requests.get(
                "https://lewd.tritan.dev/api/v1/blowjob").json()
            embed = discord.Embed(
                title="Here's some bj yaoi!~", description="Provided by our [yaoi api.](https://lewd.tritan.dev)", color=0x5865F2)
            embed.set_image(url=response["url"])
            await ctx.respond(embed=embed,  ephemeral=True)
            # Catch errors lazily
        except Exception as e:
            await ctx.respond("Something went wrong. Please try again later.")
            print(e)

def setup(client):
    client.add_cog(Lewds(client))
