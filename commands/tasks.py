import discord
from discord.ext import commands
from discord import app_commands

tasks = {}
async def init(bot):
    print("addint tasks")
    @bot.tree.command(name="taskadd", description="Add a task to complete")
    @app_commands.describe(key="The unique identifier for the task", task="The task description")
    async def task_add(interaction: discord.Interaction, key: str, task: str):
        tasks[key] = task
        await interaction.response.send_message(f"Task added under key '{key}': {task}")

    @bot.tree.command(name="taskget", description="Get a task by its key")
    @app_commands.describe(key="The unique identifier for the task")
    async def task_get(interaction: discord.Interaction, key: str):
        task = tasks.get(key)
        if task:
            await interaction.response.send_message(f"Task for '{key}': {task}")
        else:
            await interaction.response.send_message(f"No task found with key '{key}'")