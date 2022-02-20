from discord.ext import commands


class DaddyJSK(commands.Cog):
    def __init__(self, client):
        self.client = client

        client.load_extension('jishaku')


def setup(client):
    client.add_cog(DaddyJSK(client))
