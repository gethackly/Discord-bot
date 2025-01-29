from discord import app_commands
from discord.ext import commands
async def init(bot):
    @bot.tree.command(name="test_channel", description="trying to create a channel")
    @app_commands.describe(name="the name for the thread", description="the description of the thread")
    async def make_channel(ctx:commands.Context, name:str, description:str):
        # Send a message first
        message = await ctx.channel.send(description)

    # Create a thread from the message
        thread = await message.create_thread(name=name, auto_archive_duration=60)
        
        
