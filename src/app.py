import discord
import os
import sentry_sdk
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

def main():
    client = commands.Bot(command_prefix="y.", intents=intents)

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and not filename.startswith("_"):
            cog = filename[:-3]
            try:
                client.load_extension("cogs." + cog)
                print("[LOADING] --> Loaded {} cog.".format(cog))
            except Exception as cum:
                print("[LOADING] --> Failed to load {}\n{}: {}".format(
                    cog, type(cum).__name__, cum))

    client.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        traces_sample_rate=1.0
    )
    main()
