import discord
from discord.ext import commands
from types import FunctionType
from inspect import isasyncgenfunction
# Hardcoded bot token (use with caution)
TOKEN = "MTMzMTMyOTkxMjEyMDAyMTA4Mw.G6qKvC.HazoduILn4bAHcSrRfSUIZeHbdvhZLj03zmiNE"
# Create a bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
groups = []

def add_group(function):
    if isinstance(function, FunctionType):
        groups.append(function)
    else:
        print("Error: the argument of add_group should be a function")

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    try:
        for group in groups:
            if not isasyncgenfunction(group):
                await group(bot)
            else:
                print("Error, one of the group function not an async function")
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")
def run_bot():
    bot.run(TOKEN)
