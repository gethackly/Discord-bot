import discord
import datetime
from discord.ext import commands
from discord import app_commands

# Hardcoded bot token (use with caution)
TOKEN = "YOUR_TOKEN_HERE"
tasks= {}
# Create a bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="hello", description="Replies with Hello, World!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, World!")

@bot.tree.command(name="goodnight", description="Have sweet dreams!")
async def goodnight(interaction: discord.Interaction):
    await interaction.response.send_message("GOOD NIGHT! HAVE LOTS OF SWEET DREAMS AND SLEEP TIGHT! BEEP BOOP!")

@bot.tree.command(name="time", description="shows time")
async def time(interaction: discord.Interaction):
    await interaction.response.send_message(str(datetime.datetime.now()))

@bot.tree.command(name="taskAdd", description="Add a task to complete")
@app_commands.describe(key="The unique identifier for the task", task="The task description")
async def task_add(interaction: discord.Interaction, key: str, task: str):
    tasks[key] = task
    await interaction.response.send_message(f"Task added under key '{key}': {task}")

@bot.tree.command(name="taskGet", description="Get a task by its key")
@app_commands.describe(key="The unique identifier for the task")
async def task_get(interaction: discord.Interaction, key: str):
    task = tasks.get(key)
    if task:
        await interaction.response.send_message(f"Task for '{key}': {task}")
    else:
        await interaction.response.send_message(f"No task found with key '{key}'")



# Run the bot
bot.run(TOKEN) 
