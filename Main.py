import discord
from discord.ext import commands
from commands import tasks

# Hardcoded bot token (use with caution)
TOKEN = "YOUR_TOKEN_HERE"

# Create a bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    try:
        await tasks.init(bot=bot)  # Initialize tasks
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

bot.run(TOKEN)
